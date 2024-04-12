import os
from dotenv import load_dotenv
from research_agent import research_agent
from scraper_agent import scraper_agent
from content_summariser_agent import content_summariser_agent
from publisher_agent import publisher_agent

load_dotenv()

def lambda_handler(event, context):

    print("Starting ArXiv paper summarization process...")

    # Research agent
    arxiv_urls = research_agent()

    # Scraper agent
    scraped_data = scraper_agent(arxiv_urls)

    # Content Summariser agent
    summaries = content_summariser_agent(scraped_data)

    # Publisher agent
    publisher_agent(summaries)
    
    print("ArXiv paper summarization process completed.")

    return {
        'statusCode': 200,
        'body': 'ArXiv papers summarized and published to Discord successfully.'
    }

if __name__ == "__main__":
    lambda_handler(None, None)
