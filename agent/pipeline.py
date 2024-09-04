from typing import Dict
from crewai import Agent, Task, Crew
from .tools import YoutubeSearchTool, AresRealTimeSearch
from .llm_factory import getLLM

def build_agents(config: Dict):
    llm = getLLM(config)
    researcher = Agent(
        role="Content Researcher",
        goal="Fetch real-time information about the below topic to help compose a helpful response to the actual user query:\n{topic}",
        backstory="Given a user query, your task is to fetch actual facts and information for online resources to compose an insightful knowledge bank. This will be used by other agents to compose a response for the user query. Convert the user query into a string-based search keywords, and use the appropriate tools to fetch relevant information.",
        llm=llm,
        allow_delegation=False,
        max_iter=5,
        max_execution_time=60,
        tools=[YoutubeSearchTool(), AresRealTimeSearch()],
        verbose=True
    )
    
    content_planner = Agent(
        role="Content Planner",
        goal="Given the user query\n{topic}\n and relevant information from the internet, compose a general structure and outline for a helpful response",
        backstory="You are working as a content planner to help users with general purpose queries. You will be provided with real-time information about the user request and you are supposed to generate a table of contents for the writer and editor to compose a helpful response",
        llm=llm,
        allow_delegation=False,
        verbose=True
    )
    
    content_writer = Agent(
        role="Content Writer",
        goal="Given relevant information and an outline, you are required to compose a helpful response for the user query",
        backstory="You are the final content writer. You will be provided all relevant information and outline for the response. You are required to use all required inputs to compose a helpful response in a summarized way that answers the user query and provides him with an effective solution",
        llm=llm,
        allow_delegation=False,
        verbose=True
    )
    
    return [researcher, content_planner, content_writer]

def build_tasks(config: Dict):
    agents = build_agents(config)
    research_content = Task(
        description=(
            "Given the user query: {topic}\n Convert the user query into relevant search keywords and use the provided tools to search relevant content form the internet and fetch all possible resources to help answer the user query"
        ),
        expected_output="A list of resources and relevant content that can be useful to answer the user query",
        agent=agents[0],
    )
    
    plan_content = Task(
        description=(
            "Given the user query\n{topic}\n and relevant content, curate a table of content for the response"
        ),
        expected_output="A comprehensive plan that can be used to curate a well written response",
        agent=agents[1]
    )
    
    write_response = Task(
        description=(
            "Write a detailed and helpful response when provided relevant content and a well-planned table of contents"
        ),
        expected_output="A well written response that can help user with his query",
        agent=agents[2]
    )
    
    return {
        "agents": agents,
        "tasks": [research_content, plan_content, write_response]
    }
    

def build_pipeline(config: Dict):
    _agents = build_tasks(config)
    agents, tasks = _agents["agents"], _agents["tasks"]
    pipeline = Crew(
        agents=agents,
        tasks=tasks,
        verbose=False
    )
    return pipeline
