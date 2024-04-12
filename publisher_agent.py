# publisher_agent.py
import requests
import time
import json

DISCORD_WEBHOOK_URL = "https://discord.com/api/webhooks/1222642972785512478/9LllR8NjUGD49z5RfLzW5CsMXAM-J3echr57MC1qV6hLoUvz8XzsONQel_QTWTNAS2bq"

def publisher_agent(summaries):
    print("Starting publisher agent...")
    for data in summaries:
        url = str(data["url"])
        title = str(data["title"])
        summary = str(data["summary"])

        # Strip "https://" from the URL
        url = url.replace("https://", "")

        payload = {
            "content": f"**{title}**\n\n{summary}\n\nFind the full paper here - URL: {url}"
        }
        
        retry_count = 0
        while True:
            if retry_count >= 5:
                print("Skipped after 5 retries")
                break
                
            response = requests.post(DISCORD_WEBHOOK_URL, json=payload)
            print(f"Sending message to Discord. Status code: {response.status_code}")

            if response.status_code == 204:
                print("Message sent successfully.")
                break
            else:
                print(f"Failed to send message to Discord. Status code: {response.status_code}")
                retry_count += 1
                print(f"Retrying in 5 seconds... Attempt {retry_count}")
                time.sleep(5)
                
            
    print(f"Published {len(summaries)} summaries to Discord.")

