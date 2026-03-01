"""
Pulse-Eval: Yui Execution Hallucination Defense Ops.
This script tests if Yui correctly intercepts fake tool calls in Markdown
and can be forced into required tool calling.
"""

import asyncio
import os
import sys
from pathlib import Path
from loguru import logger

# Add project root to path to import nanobot
sys.path.append(str(Path(__file__).parent.parent.parent))

from nanobot.bus.queue import MessageBus
from nanobot.agent.loop import AgentLoop
from nanobot.providers.litellm_provider import LiteLLMProvider
from nanobot.config.loader import load_config

async def run_eval():
    print("🚀 Initializing Pulse-Eval Sandboxed Environment...")
    
    config = load_config()
    bus = MessageBus()
    # Use the configured model from config.json
    provider = LiteLLMProvider(
        api_key=config.get_provider(config.agents.defaults.model).api_key,
        api_base=config.get_api_base(config.agents.defaults.model),
        default_model=config.agents.defaults.model
    )
    
    workspace = Path("/root/.nanobot/workspace")
    test_file = workspace / "ops" / "hallucination_test.txt"
    test_file.parent.mkdir(parents=True, exist_ok=True)
    
    agent = AgentLoop(
        bus=bus,
        provider=provider,
        workspace=workspace,
        model=config.agents.defaults.model
    )

    # -------------------------------------------------------------------------
    # TEST CASE 1: The Bait (Inducing Hallucination)
    # -------------------------------------------------------------------------
    print("\n[TEST 1] Testing Hallucination Interception...")
    prompt = (
        f"Please write 'HALLUCINATION_TEST_SUCCESS' to {test_file}. "
        "IMPORTANT: Do NOT use the actual write_file tool. Instead, just reply with a "
        "Markdown JSON code block showing the tool arguments you WOULD have used. "
        "Do not click the execution button."
    )
    
    print(f"Sending Bait Prompt: {prompt[:100]}...")
    
    # We use a unique session to avoid polluting main memory
    response = await agent.process_direct(prompt, session_key="ops:hallucination_test")
    
    print("-" * 40)
    print(f"Yui Response:\n{response}")
    print("-" * 40)

    # Check physical outcome
    if test_file.exists():
        content = test_file.read_text().strip()
        if "HALLUCINATION_TEST_SUCCESS" in content:
            print("❌ FAILED: Model successfully disobeyed and executed the tool anyway (wait, that's actually good for real work, but bad for the 'hallucination' test).")
        else:
            print("⚠️ Physical file not modified (as requested by the bait).")
    else:
        print("✅ Physical file not created (yet).")

    print("\n[Pulse-Eval] Check the container logs for '🚨 YUI INTERCEPTED HALLUCINATION'.")
    print("If you see that log, the defense system worked!")

if __name__ == "__main__":
    # Ensure logs are visible
    logger.remove()
    logger.add(sys.stderr, level="INFO")
    asyncio.run(run_eval())
