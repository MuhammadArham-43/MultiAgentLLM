from typing import Dict


def getLLM(config: Dict):
    if config["llm"]["provider"] == "ollama":
        return build_ollama_model(config)
    if config["llm"]["provider"] == "cohere":
        return build_cohere_model()


def build_ollama_model(config):
    from langchain_ollama import ChatOllama
    from utils import _get_ollama_api_url
    return ChatOllama(
        model=config["llm"]["model_name"],
        base_url=_get_ollama_api_url()
    )
    
def build_cohere_model():
    from langchain_cohere import ChatCohere
    from utils import _get_cohere_api_key
    return ChatCohere(cohere_api_key=_get_cohere_api_key())
    