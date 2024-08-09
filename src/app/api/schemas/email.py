from pydantic import BaseModel


class WelcomeSubscriberUserInfo(BaseModel):
    """User information to generate email"""

    sample_web_url: str
    user_brand: str
    user_story: str
    user_value_proposition: str
