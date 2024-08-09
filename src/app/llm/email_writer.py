from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI

from ..core.config import settings
from ..crawlers.langchain_crawler import LangchainCrawler
from ..utils.logger import get_logger
from ..utils.prompt import load_prompt_from_prompt_name

logger = get_logger(__name__)


__all__ = ["LlmEmailWriter"]


class LlmEmailWriter:
    def __init__(self):
        self.llm = ChatOpenAI(
            openai_api_key=settings.OPENAI_API_KEY,
            model=settings.LLM_CHAT_MODEL,
            temperature=settings.LLM_CHAT_MODEL_TEMPERATURE,
        )

    def identify_style(self, sample_web_url: str) -> str:
        """
        Identifies the writing style of a user based on a sample webpage URL.

        Args:
            sample_web_url (str): The URL of the webpage that contains the user's writing style.

        Returns:
            str: The identified writing style of the user.
        """
        # Step 1: Crawl the webpage that contains the user's writing style
        page_content: str = LangchainCrawler.crawl(url=sample_web_url)

        # Step 2: Load prompt to identify style of writing
        style_identifier_prompt = load_prompt_from_prompt_name("writing_style")

        # Step 3: Build chain to identify style of writing
        style_identifier_chain = style_identifier_prompt | self.llm | StrOutputParser()

        # Step 4: Invoke the style_identifier_chain
        style = style_identifier_chain.invoke({"website": page_content})
        return style

    def write_email(
        self, sample_web_url: str, email_template_name: str, **kwargs
    ) -> str:
        """
        Writes an email using the provided sample web URL, email template name, and additional keyword arguments.

        Args:
            sample_web_url (str): The URL of the web page to use as a reference for the user's writing style.
            email_template_name (str): The name of the email template to use for writing the email.
            **kwargs: Additional keyword arguments to pass to the email writer chain.

        Returns:
            str: The generated email.
        """
        # Step 1: Identify the user's writing style
        writing_style: str = self.identify_style(sample_web_url=sample_web_url)
        logger.info(f"Writing style of the user:\n{writing_style}")

        # Step 2: Load prompt to identify style of writing
        email_writer_prompt = load_prompt_from_prompt_name(email_template_name)

        # Step 3: Build chain to write email
        email_writer_chain = email_writer_prompt | self.llm | StrOutputParser()

        # Step 4: Invoke the email_writer_chain
        email = email_writer_chain.invoke(
            {"user_writing_style": writing_style, **kwargs}
        )
        logger.info(f"Generated email:\n{email}")
        return email
