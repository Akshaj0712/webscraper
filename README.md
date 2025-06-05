# Agentic Web Scraper
Idea: To scrape cotent using the mcp tool (very similar to api, difference in jargon) in scrape_dynamic_as_markdown.py; and use the llm model being called in app.py to improve the structure. In essence, scrape markdown content and prompting an LLM to have a second look.
## app.py
The main script to run. Edit model, API key and prompt in this script.

## scrape_dynamic_as_markdown.py
beautiful soup (html) + Selenium (javascript) scraper tool

## exa_search.py
ignore, copied from tutorial
caution:
1. have webdriver-manager installed
2. have chrome installed for Selenium to work
   
## python_tools
ignore, copied from tutorial

## Experiments

#### Extract temperature deviations from the past decade: tutorial
successfully extracting 10 datapoints (using exa_seach.py, uses exa-py a search engine) and produced a bar chart (using python_tools.py)

#### scrape content form https://www.idfcfirstbank.com/
failed, hit token limit, out of credits :"(

## Caution
anthropic/claude-3-opus was used in the experiment. 
LLMs that did NOT work: deepseek/deepseek-r1-0528-qwen3-8b & deepseek/deepseek-r1-0528-qwen3-8b:free. Endpoint: [OpenRouter](https://openrouter.ai/models)

Not all LLMs are capable of using MCP tools.
For MCPs, the following LLMs work.
openai/gpt-4-turbo	✅ Yes	Fast and fully tool-capable
openai/gpt-3.5-turbo	✅ Yes	Also supports tools
anthropic/claude-3-opus	✅ Yes	Claude 3, works with tools
mistralai/mixtral	⚠️ Partial	Not all endpoints support tools
