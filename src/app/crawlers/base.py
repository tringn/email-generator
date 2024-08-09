from abc import ABC, abstractmethod


class BaseCrawler(ABC):
    @abstractmethod
    def crawl(self, *args, **kwargs):
        raise NotImplementedError("Subclasses must implement this method.")
