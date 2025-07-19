import os
from langchain_openai import ChatOpenAI
from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
from langgraph.checkpoint.memory import InMemorySaver
from dotenv import load_dotenv

load_dotenv()

def build_llm(model_name: str, temperature: float = 0.0) -> ChatOpenAI:
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OPENAI_API_KEY not found in environment variables.")
    return ChatOpenAI(
        model=model_name,
        temperature=temperature,
        max_tokens=512,
        openai_api_key=api_key
    )

async def create_mcp_agent():
    client = MultiServerMCPClient({
        "cars": {
            "url": "http://server:8000/mcp",
            "transport": "sse",
        }
    })
    tools = await client.get_tools()
    llm = build_llm("gpt-4o")
    checkpointer = InMemorySaver()
    agent = create_react_agent(model=llm, tools=tools, checkpointer=checkpointer)
    return agent