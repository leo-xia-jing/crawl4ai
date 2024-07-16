import unittest, os
from crawl4ai.web_crawler import WebCrawler
from crawl4ai.chunking_strategy import RegexChunking, FixedLengthWordChunking, SlidingWindowChunking
from crawl4ai.extraction_strategy import CosineStrategy, LLMExtractionStrategy, TopicExtractionStrategy, NoExtractionStrategy

TEST_URL = 'https://baidu.com'

class TestWebCrawler(unittest.TestCase):
    
    def setUp(self):
        self.crawler = WebCrawler(always_by_pass_cache=True)
    
    # def test_warmup(self):
    #     self.crawler.warmup()
    #     self.assertTrue(self.crawler.ready, "WebCrawler failed to warm up")
    
    def test_run_different_strategies(self):
        url = TEST_URL

        print(f"test_run_different_strategies's url is: {url}")
        
        # Test with FixedLengthWordChunking and LLMExtractionStrategy
        result = self.crawler.run(
            url=url,
            word_count_threshold=5,
            chunking_strategy=FixedLengthWordChunking(chunk_size=100),
            extraction_strategy=LLMExtractionStrategy(provider="ollama/llama3", api_token='no-token-needed'), bypass_cache=True
        )
        self.assertTrue(result.success, "Failed to crawl and extract with FixedLengthWordChunking and LLMExtractionStrategy")
        
    # def test_invalid_url(self):
    #     with self.assertRaises(Exception) as context:
    #         self.crawler.run(url='invalid_url', bypass_cache=True)
    #     self.assertIn("Invalid URL", str(context.exception))
    
if __name__ == '__main__':
    unittest.main()
