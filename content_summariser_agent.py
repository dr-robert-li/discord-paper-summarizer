import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()
client.api_key = os.getenv("OPENAI_API_KEY")

def content_summariser_agent(scraped_data):
    print("Starting content summariser agent...")

    summaries = []
    for index, data in enumerate(scraped_data, start=1):
        url = data["url"]
        content = data["text"]

        print(f"Processing paper {index} of {len(scraped_data)}...")

        # Use GPT-4 to determine the title of the paper
        print("Extracting title from the content using GPT-4...")
        title_prompt = f"""
        Please extract the title of the research paper from the following content. Return the title verbatim.
        
        Content: {content}
        """

        title_retry_count = 0
        while title_retry_count < 2:
            title_response = client.chat.completions.create(
                model="gpt-4-turbo-preview",
                messages=[
                    {"role": "system", "content": "You are an expert research assistant."},
                    {"role": "user", "content": title_prompt}
                ],
                max_tokens=150,
                n=1,
                stop=None,
                temperature=0,
            )

            title = title_response.choices[0].message.content.strip()
            if title.startswith("The title of the research paper is "):
                title = title[len("The title of the research paper is "):].strip()
            if not title.startswith("I'm sorry"):
                break
            title_retry_count += 1
            print(f"Retrying title extraction... (Attempt {title_retry_count})")

        if title_retry_count == 5:
            print("Title extraction failed after 2 attempts. Skipping this paper.")
            continue

        print(f"Extracted title: {title}")

        # Generate summary using GPT-4
        print("Generating summary using GPT-4...")
        summary_prompt = f"""
        Please summarize the following content.
         
        The content is a research paper from the ArXiv Computer Science, Artificial Intelligence repository.
         
        Pay close attention to any of the following sections: the abstract, methodology, results, discussion. 
        
        If these sections are not found, provide a general summary. 
        
        Summary MUST be less than 150 words.

        Do NOT use markdown formatting.

        This is the content:

       {content}
        """

        summary_retry_count = 0
        while summary_retry_count < 2:
            summary_response = client.chat.completions.create(
                model="gpt-4-turbo-preview",
                messages=[
                    {"role": "system", "content": "You are an expert research assistant."},
                    {"role": "user", "content": summary_prompt}
                ],
                max_tokens=4096,
                n=1,
                stop=None,
                temperature=0,
            )

            summary = summary_response.choices[0].message.content.strip()
            if not summary.startswith("I'm sorry"):
                break
            summary_retry_count += 1
            print(f"Retrying summary generation... (Attempt {summary_retry_count})")

        if summary_retry_count == 5:
            print("Summary generation failed after 2 attempts. Skipping this paper.")
            continue

        summaries.append({"url": url, "title": title, "summary": summary})

        print(f"URL: {url}")
        print(f"Title: {title}")
        print(f"Summary: {summary}")
        print("---")

    print(f"Generated summaries for {len(summaries)} papers.")
    return summaries
