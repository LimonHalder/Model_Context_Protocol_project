# Multi-Tool Chat Agent with LangChain, LangGraph, and MCP

This project demonstrates how to build a multi-tool conversational agent using:

- `langchain_mcp_adapters` for connecting multiple MCP (Modular Chat Protocol) tools
- `langgraph` prebuilt React agent
- `langchain_groq` for language model integration
- Async Python with asyncio

---

## Features

- Uses two tools: 
  - **Math tool**: a Python script responding to math queries via stdio transport
  - **Weather tool**: a FastMCP server responding over HTTP (streamable_http transport)
- Combines tools with an LLM (`qwen-qwq-32b`) to answer user queries
- Demonstrates invoking tools asynchronously with an agent

---

## Setup

1. Clone the repository:

```bash
git clone https://github.com/LimonHalder/Model_Context_Protocol_project.git
cd your-repo




pip install -r requirements.txt


GROQ_API_KEY=your_api_key_here

python weather.py
