from pathlib import Path

from langchain_core.prompts import BasePromptTemplate, load_prompt


def load_prompt_from_prompt_name(prompt_name: str) -> BasePromptTemplate:
    """Load a template prompt from prompt's name

    Args:
        prompt_name (str): Name of prompt

    Returns:
        BasePromptTemplate: The langchain prompt template
    """
    prompt_file: str = str(
        Path(__file__).parent / ".." / "core" / "prompts" / f"{prompt_name}.yaml"
    )
    return load_prompt(prompt_file)
