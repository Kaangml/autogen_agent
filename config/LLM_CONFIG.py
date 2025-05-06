import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def get_env_variable(var_name):
    """Get the environment variable or raise an exception if not found."""
    try:
        return os.environ[var_name]
    except KeyError:
        raise EnvironmentError(f"Set the {var_name} environment variable.")
CONFIG_LIST =[
    {
        "model": "llama3.2:1b",  
        "api_base": get_env_variable("OLLAMA_API_BASE"),  
        "api_type": "ollama",
        "tags": ["llama","tiny_llm","local"], 
    },
    {
        "model": "gemini-2.0-flash",
        "api_key": get_env_variable("GEMINI_API_KEY"),
        "api_type": "google",
        "tags": ["gemini","base_llm","cloud"],
    }
]

"""
# Details:
#Print All Model Names
for config in CONFIG_LIST:
    print(config["model"])

#Filter Configurations by Tag
cloud_configs = [config for config in CONFIG_LIST if "cloud" in config["tags"]]
print(cloud_configs)

# Access Specific Configuration Details
CONFIG_LIST[0]["model"] = "llama3.2:1b"
CONFIG_LIST[1]["tags"] = ["gemini","base_llm","cloud"]

"""
