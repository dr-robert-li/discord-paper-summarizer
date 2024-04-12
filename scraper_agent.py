import io
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
import requests

def extract_text_from_pdf(pdf_url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.3.1 Safari/605.1.1"
    }
    response = requests.get(pdf_url, headers=headers)
    pdf_data = io.BytesIO(response.content)

    resource_manager = PDFResourceManager()
    fake_file_handle = io.StringIO()
    converter = TextConverter(resource_manager, fake_file_handle, laparams=LAParams())
    page_interpreter = PDFPageInterpreter(resource_manager, converter)

    for page in PDFPage.get_pages(pdf_data, caching=True, check_extractable=True):
        page_interpreter.process_page(page)

    text = fake_file_handle.getvalue()
    converter.close()
    fake_file_handle.close()

    return text

def scraper_agent(arxiv_urls):
    print("Starting scraper agent...")
    scraped_data = []

    for arxiv_url in arxiv_urls:
        try:
            # Extract text from the PDF
            text = extract_text_from_pdf(arxiv_url)

            # Print a preview of the extracted text
            preview_length = 500
            print(f"Preview of extracted text from {arxiv_url}:")
            print(text[:preview_length])
            print("...")

            # Append the scraped data to the list
            scraped_data.append({"url": arxiv_url, "text": text})
            print(f"Scraped data from: {arxiv_url}")

        except Exception as e:
            print(f"An error occurred while scraping: {arxiv_url}")
            print(f"Error message: {str(e)}")

    print(f"Scraped data from {len(scraped_data)} URLs.")
    return scraped_data
