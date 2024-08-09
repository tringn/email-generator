from fastapi import APIRouter, HTTPException

from app.api.schemas.email import WelcomeSubscriberUserInfo
from app.llm.email_writer import LlmEmailWriter

router = APIRouter()


@router.post("/generate/welcome_subscriber")
async def generate_welcome_subscriber_email(
    user_info_payload: WelcomeSubscriberUserInfo,
) -> str:
    """
    Generate a welcome email for a subscriber.

    Args:
        user_info_payload: A payload containing the user information.

    Returns:
        A string representing the generated email.

    Raises:
        HTTPException: If there is an error generating the email.
    """

    # Convert the user info payload to a dictionary
    user_info: dict = user_info_payload.model_dump()

    try:
        # Create an instance of the LLM email writer
        llm = LlmEmailWriter()

        # Generate the email using the LLM and the user information
        generated_email: str = llm.write_email(
            email_template_name="welcome_subscriber_email", **user_info
        )
    except Exception as exc:
        # If there is an error, raise an HTTPException with the error details
        raise HTTPException(status_code=500, detail=exc)
    else:
        # Return the generated email
        return generated_email
