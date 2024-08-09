import pytest

from src.app.llm.email_writer import LlmEmailWriter


@pytest.mark.parametrize(
    "url",
    [
        # "https://www.etsy.com/news/etsy-unveils-top-back-to-school-trends-big-savings-and-more-to-start-the-school-year-in-style",
        "https://desiretableware.com/pages/about-us"
    ],
)
def test_identify_style(url):
    email_writer = LlmEmailWriter()
    style: str = email_writer.identify_style(url)
    assert isinstance(style, str)


def test_write_email_0():
    email_writer = LlmEmailWriter()
    email: str = email_writer.write_email(
        sample_web_url="https://desiretableware.com/pages/about-us",
        email_template_name="welcome_subscriber_email",
        user_brand="Desire Tableware",
        user_story="""We are a family run business in Auckland, New Zealand specialising in unique tableware that adds beauty, Charm and fun into everyday life. My story starts back in Iran where I was born. I remember sitting around the table with my Mum and Grandmother taking the time to enjoy the simple pleasures in life … a cup of tea or a traditional spirted family dinner. It was here my love of a beautiful table was born and a passion I have brought with me to my new home. I am so excited to be able to bring to you Zarin Porcelain, stunning tableware that is not only timeless and functional, but great quality at a great price.""",
        user_value_proposition="free delivery throughout the North and South Islands of New Zealand, sell great quality products suited to everyday living, world-class standards",
    )
    assert isinstance(email, str)


def test_write_email_1():
    email_writer = LlmEmailWriter()
    email: str = email_writer.write_email(
        sample_web_url="https://graceandthorn.com/blogs/the-cut/the-art-of-ikebana-beauty-in-simplicity",
        email_template_name="welcome_subscriber_email",
        user_brand="Grace & Thorn",
        user_story="""As a child growing up on an Council Estate in Islington, it was the Fiddle Leaf Fig tree in the front room of my Grandparents home that had me mesmerised. The fact that the tree existed within the walls of a house, not in a park, made this a specimen of awe and wonder for a city child.""",
        user_value_proposition="help people to see flowers and plants in a different way",
    )
    assert isinstance(email, str)
