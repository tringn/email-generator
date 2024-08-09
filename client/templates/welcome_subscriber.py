import requests  # type: ignore
import streamlit as st
from logger import get_logger
from settings import Settings

logger = get_logger(__name__)

_settings = Settings()


def generate_welcome_subscriber_email(
    sample_web_url: str,
    user_brand: str,
    user_story: str,
    user_value_proposition: str,
) -> str:
    resp = requests.post(
        url=_settings.WELCOME_SUBSCRIBER_EMAIL_URL,
        json={
            "sample_web_url": sample_web_url,
            "user_brand": user_brand,
            "user_story": user_story,
            "user_value_proposition": user_value_proposition,
        },
        timeout=30,
    )

    if resp.status_code == 200:
        return resp.json()
    else:
        logger.error(resp.json()["detail"])
        raise ValueError(resp.json()["detail"])


st.markdown("# Welcome Subscriber Email")


sample_web_url = st.text_input("Which web pages best demonstrate your writing style")
user_brand = st.text_input("Enter your brand name here")
user_story = st.text_area("Tell us about your story here")
user_value_proposition = st.text_area("Tell us about your value proposition")

generate_but = st.button("Generate welcome subscriber email")

if generate_but:

    try:
        email = generate_welcome_subscriber_email(
            sample_web_url=sample_web_url,
            user_brand=user_brand,
            user_story=user_story,
            user_value_proposition=user_value_proposition,
        )

    except Exception as exc:
        st.subheader("Oppppssss. Error happened.")
        st.error(exc)
    else:
        st.subheader(email)
