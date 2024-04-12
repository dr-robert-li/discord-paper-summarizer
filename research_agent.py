from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def research_agent():
    print("Starting research agent...")
    # Set up Selenium webdriver
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.3.1 Safari/605.1.1')

    driver = webdriver.Chrome(options=options)

    # Visit the daily papers URL
    driver.get("https://huggingface.co/papers")
    
    # Wait for 10 seconds to allow the page to load
    time.sleep(10)

    # Find all URLs on the page
    urls = driver.find_elements(By.XPATH, "//a[@href]")
    paper_urls = []
    for url in urls:
        href = url.get_attribute("href")
        if "/papers/" in href:
            paper_urls.append(href)
            print("Paper URL:", href)  # Print the paper URL

    arxiv_urls = []
    for paper_url in paper_urls:
        driver.get(paper_url)  # Navigate to the paper URL
        urls = driver.find_elements(By.XPATH, "//a[@href]")
        for url in urls:
            href = url.get_attribute("href")
            if "https://arxiv.org/pdf/" in href:
                arxiv_urls.append(href)
                print("arXiv URL:", href)  # Print the arXiv URL

    # Remove duplicates from arxiv_urls
    arxiv_urls = list(set(arxiv_urls))

    driver.quit()
    print(f"Found {len(arxiv_urls)} unique arXiv URLs.")
    return arxiv_urls
