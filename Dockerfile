# 使用多阶段构建来获取 Node.js
FROM node:20-bookworm-slim AS node_base
FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim

# 1. 🚀 基础环境：Node.js 部署与 PATH 设置
COPY --from=node_base /usr/local/bin/node /usr/local/bin/
COPY --from=node_base /usr/local/lib/node_modules /usr/local/lib/node_modules
RUN ln -s /usr/local/lib/node_modules/npm/bin/npm-cli.js /usr/local/bin/npm && \
    ln -s /usr/local/lib/node_modules/npm/bin/npx-cli.js /usr/local/bin/npx

# 确保 Node.js 在环境变量中
ENV PATH="/usr/local/bin:$PATH"

# 2. ⚡ 换源并安装最基础工具
RUN sed -i 's/deb.debian.org/mirrors.aliyun.com/g' /etc/apt/sources.list.d/debian.sources && \
    apt-get update && \
    apt-get install -y --no-install-recommends curl git && \
    git config --global url."https://github.com/".insteadOf ssh://git@github.com/ && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

# 3. 安装 Python 依赖 (缓存层)
COPY pyproject.toml README.md LICENSE ./
RUN mkdir -p nanobot bridge && touch nanobot/__init__.py && \
    uv pip install --system --no-cache --index-url https://pypi.tuna.tsinghua.edu.cn/simple . && \
    rm -rf nanobot bridge

# 4. 拷贝源码并安装
COPY nanobot/ nanobot/
COPY bridge/ bridge/
RUN uv pip install --system --no-cache --index-url https://pypi.tuna.tsinghua.edu.cn/simple .

# 5. 编译 WhatsApp 桥接
WORKDIR /app/bridge
RUN npm config set registry https://registry.npmmirror.com && \
    npm install && \
    npm run build
WORKDIR /app

RUN mkdir -p /root/.nanobot
EXPOSE 18790

ENTRYPOINT ["nanobot"]
CMD ["status"]
