from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
from langchain_groq import ChatGroq

from dotenv import load_dotenv
load_dotenv()


import asyncio


async def main():
    try:
        client = MultiServerMCPClient({
            "math": {
                "command": "python",
                "args": ["mathserver.py"],
                "transport": "stdio"
            },
            "weather": {
                "url": "http://localhost:8000/mcp",
                "transport": "streamable_http"
            }
        })

        import os
        os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

        tools = await client.get_tools()
        print("Tools loaded:", [tool.name for tool in tools])  # ✅ Debug print

        model = ChatGroq(model="qwen-qwq-32b")

        agent = create_react_agent(model, tools=tools)

        math_response = await agent.ainvoke({
            "messages": [{"role": "user", "content": "What is 5 + 3?"}]
        })

        print("Math response:", math_response["messages"][-1].content)

        weather_response = await agent.ainvoke({
            "messages": [{"role": "user", "content": "What's the weather in New York?"}]
        })
        print("Weather response:", weather_response["messages"][-1].content)    

    except Exception as e:
        print("❌ Error occurred:", e)

asyncio.run(main())