from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
from langchain_groq import ChatGroq
from dotenv import load_dotenv
load_dotenv()

import asyncio

async def main():
    client = MultiServerMCPClient(
        {
            "math":{
                "command": "python",
                "args": ["mathserver.py"],
                "transport": "stdio"
            },
            "weather":{
                "url": "http://localhost:8001/mcp",
                "transport": "streamable-http"
            }
        }
    )
    
    import os
    os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

    tools = await client.get_tools()
    model = ChatGroq(model="gwen-qwq-32b")
    agent = create_react_agent(model, tools)

    # math_response = await agent.ainvoke{
    #     "messages": [
    #         ("user", "What is 10 + 20?")
    #     ]
    # }
    # print(math_response)

    weather_response = await agent.ainvoke({"messages": [("user", "What is the weather in Tokyo?")]})
    print(weather_response)
    
asyncio.run(main())