from agents.basic_agent import create_basic_agent
from config.LLM_CONFIG import CONFIG_LIST

def main():
    # Define the agent with the configuration
    #config = CONFIG_LIST[0]  # Select the first configuration for the agent
    #config.pop("api_base", None)
    #agent = create_basic_agent(name="LocalLLMAgent", config=config)
    
    config = CONFIG_LIST[1]  # Use the second configuration (e.g., Gemini)
    agent = create_basic_agent(name="CloudAgent", config=config)

    # Start a conversation with the agent
    user_input = "How many planet in the solar systems?"
    
    # Response from the agent
    print(f"Agent: Hello! I am a {agent.name}. How can I assist you today?")
    reply = agent.generate_reply(messages=[{"role": "user", "content": user_input}])

    print(f"Answer: {reply['content']}")

if __name__ == "__main__":
    main()
