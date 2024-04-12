# Discord Paper Summarizer

This project consists of a set of Python scripts that work together to summarize research papers from the ArXiv Computer Science, Artificial Intelligence repository and publish the summaries to a Discord channel using a webhook.

## Overview
The project is divided into four main components:

1. Research Agent: Searches for relevant research papers on the ArXiv website and extracts their URLs.
2. Scraper Agent: Scrapes the content of the research papers from the extracted URLs.
3. Content Summariser Agent: Uses OpenAI's GPT-4 to generate concise summaries of the scraped research papers.
4. Publisher Agent: Publishes the generated summaries to a Discord channel using a webhook.

## Requirements
To run this project, you need the following:

* Python 3.6 or higher
* Selenium WebDriver (Chrome)
* OpenAI API key
* Discord webhook URL

## Installation
Clone the repository:

```
git clone https://github.com/your-username/arxiv-paper-summarization.git
cd arxiv-paper-summarization
```

Install the required Python packages:

```
pip install -r requirements.txt
```

Set up the environment variables:

* Create a .env file in the project root directory.
* Add the following variables to the .env file:

```
OPENAI_API_KEY=your_openai_api_key
DISCORD_WEBHOOK_URL=your_discord_webhook_url
```

Download and set up the Selenium WebDriver for Chrome:

*Download the appropriate version of ChromeDriver from here.
* Place the downloaded chromedriver executable in a directory that is in your system's PATH.

## Usage
To run the project, execute the app.py script:

```
python app.py
```

The script will perform the following steps:

1. The Research Agent will search for relevant research papers on the ArXiv website and extract their URLs.
2. The Scraper Agent will scrape the content of the research papers from the extracted URLs.
3. The Content Summariser Agent will use OpenAI's GPT-4 to generate concise summaries of the scraped research papers.
4. The Publisher Agent will publish the generated summaries to the specified Discord channel using the provided webhook.

## File Structure
* `app.py`: The main script that orchestrates the entire process.
* `research_agent.py`: Contains the code for the Research Agent.
* `scraper_agent.py`: Contains the code for the Scraper Agent.
* `content_summariser_agent.py`: Contains the code for the Content Summariser Agent.
* `publisher_agent.py`: Contains the code for the Publisher Agent.
* `requirements.txt`: Lists the required Python packages.
* `.env`: Stores the environment variables (OpenAI API key and Discord webhook URL).

## Contributing
If you'd like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them with descriptive commit messages.
4. Push your changes to your forked repository.
5. Submit a pull request to the main repository.