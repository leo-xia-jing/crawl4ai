import os
import time
from crawl4ai.web_crawler import WebCrawler
from crawl4ai.chunking_strategy import *
from crawl4ai.extraction_strategy import *
from crawl4ai.crawler_strategy import *

url = r'https://www.nbcnews.com/business'

crawler = WebCrawler()
crawler.warmup()

result = crawler.run(
        url=url,
        extraction_strategy=LLMExtractionStrategy(
            # provider="openai/gpt-4o",
            # api_token=os.getenv('OPENAI_API_KEY'),
            instruction="Extract only content related to technology"
        ),
    bypass_cache=True,
    )

model_fees = json.loads(result.extracted_content)

print(len(model_fees))

with open(".data/data.json", "w", encoding="utf-8") as f:
    f.write(result.extracted_content)