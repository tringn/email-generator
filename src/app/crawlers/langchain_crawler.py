from langchain_community.document_loaders import WebBaseLoader

from .base import BaseCrawler

__all__ = ["LangchainCrawler"]


class LangchainCrawler(BaseCrawler):
    def __init__(self) -> None:
        super().__init__()

    @staticmethod
    def crawl(url) -> str:
        loader = WebBaseLoader(url)
        documents = loader.load()
        return documents[0].page_content
