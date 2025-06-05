import os
import asyncio
from pydantic_ai import Agent
from pydantic_ai.mcp import MCPServerStdio

from pydantic_ai.models.openai import OpenAIModel
from pydantic_ai.providers.openai import OpenAIProvider

# Set your OpenRouter API key
api_key = "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"

# Initialize the OpenAIProvider with OpenRouter's base URL
provider = OpenAIProvider(
    api_key=api_key,
    base_url="https://openrouter.ai/api/v1"
)

# Initialize the OpenAIModel with the desired DeepSeek model
deepseek_chat_model = OpenAIModel(
    "anthropic/claude-3-opus",
    provider=provider
)

# Define the MCP Servers
exa_server = MCPServerStdio(
    'python',
    ['exa_search.py']
)

python_tools_server = MCPServerStdio(
    'python',
    ['python_tools.py']
)


scrape_dynamic_as_markdown = MCPServerStdio(
    'python',
    ['scrape_dynamic_as_markdown.py']
)

# Define the Agent with both MCP servers
agent = Agent(
    deepseek_chat_model, 
    mcp_servers=[scrape_dynamic_as_markdown,exa_server, python_tools_server],
    retries=3
)

# Main async function
async def main():
    async with agent.run_mcp_servers():
        result = await agent.run("""
        scrape content from https://www.idfcfirstbank.com/ as markdown. 
        only use the first 10K tokens from the markdown. 
        refine the markdown to form in to structured data. 
        do not add or subtract add that is not present, 
        except if it is very likely that the action of scraping data has noise 
        and add or subtracting bits of data will restore struccture.
        """)
        print(result)

# Run the async function
if __name__ == "__main__":
    asyncio.run(main())