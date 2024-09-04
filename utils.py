import os

def _get_env_var(key: str):
    if key in os.environ:
        return os.environ[key]
    raise ValueError(f"Environment Variable Does Not Exist: Key Error for {key}")


def _get_youtube_api_url():
    return _get_env_var("YOUTUBE_API_URL")

def _get_youtube_api_key():
    return _get_env_var("YOUTUBE_API_KEY")

def _get_ollama_api_url():
    return _get_env_var("OLLAMA_API_URL")

def _get_ares_api_url():
    return _get_env_var("ARES_API_URL")

def _get_ares_api_key():
    return _get_env_var("ARES_API_KEY")

def _get_cohere_api_key():
    return _get_env_var("COHERE_API_KEY")