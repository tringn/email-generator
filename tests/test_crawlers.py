import pytest

from src.app.crawlers.langchain_crawler import LangchainCrawler


@pytest.mark.parametrize(
    "url",
    [
        "https://www.etsy.com/news/etsy-unveils-top-back-to-school-trends-big-savings-and-more-to-start-the-school-year-in-style",
        "https://graceandthorn.com/",
    ],
)
def test_langchain_crawler(url):
    crawler = LangchainCrawler()
    document = crawler.crawl(url)
    assert isinstance(document, str)
