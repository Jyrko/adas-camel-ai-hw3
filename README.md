# CAMEL AI Job Search Assistant

This project implements a multi-agent system for job search assistance using the CAMEL AI framework. It helps users find job opportunities based on their preferences, provides resources for interview preparation, and generates a visual summary of the results.

## Project Overview

The system consists of multiple specialized agents that work together:

1. **Preference Agent**: Collects user preferences about job search requirements
2. **Job Search Agent**: Searches for relevant job postings via the LinkUp API
3. **Web Agent**: Finds additional resources to help with job interview preparation
4. **Coding Agent**: Generates a Flask web application to present the results

## Prerequisites

- Python 3.12
- Poetry (for dependency management)
- Required API keys:
  - OpenAI API key
  - LinkUp API key (for job search)
  - Google API key (required)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Jyrko/adas-camel-ai-hw3
   cd adas-camel-ai-hw3
   ```

2. Install dependencies using Poetry:
   ```bash
   poetry install
   ```

3. Create a `.env` file in the project root based on the provided `.env.example`:
   ```bash
   cp .env.example .env
   ```

4. Add your API keys to the `.env` file:
   ```bash
   OPENAI_API_KEY='your-openai-key-here'
   OPENAI_API_BASE_URL='https://api.openai.com/v1'
   LINKUP_API_KEY='your-linkup-key-here'
   GOOGLE_API_KEY='your-google-api-key'
   SEARCH_ENGINE_ID='your-search-engine-id'
   ```

## Usage

Run the main application:

```bash
poetry run python src/main.py
```

The application will:
1. Prompt you for job preferences
2. Search for relevant job postings
3. Find resources for interview preparation
4. Generate and run a Flask web application displaying the results
5. Automatically open your default web browser to view the results

## Key Components

- `src/agents.py`: Defines the specialized agents (Preference, JobSearch, Web, Coding)
- `src/workforce.py`: Configures the workforce to coordinate the agents
- `src/main.py`: Entry point that runs the workforce and displays results

## API Keys

### OpenAI API Key
Required for all language model interactions. Get one at https://platform.openai.com/

### LinkUp API Key
Required for job search functionality. Get one at https://www.linkup.com/developers/

### Google API Key
Required for web search functionality. Get one at https://developers.google.com/custom-search/v1/overview

## Troubleshooting

- **Browser Installation Error**: If you encounter browser installation errors, try installing Playwright manually:
  ```bash
  python -m playwright install chrome
  ```

- **Async Loop Errors**: If you encounter "asyncio.run() cannot be called from a running event loop" errors, the application already includes nest_asyncio to handle this.

## License

MIT License