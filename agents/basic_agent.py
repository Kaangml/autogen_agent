from autogen import AssistantAgent

from config.LLM_CONFIG import CONFIG_LIST

def create_basic_agent(name=None, config=None):
    """Create a basic agent."""
    if config is None:
        config = CONFIG_LIST[0]  # Default configuration if none is provided
    if name is None:
        name = config.get("name", "DefaultAgent")  # Default name if none is provided
    return AssistantAgent(
        name=name,
        llm_config=config,
    )
