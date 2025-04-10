import time
import os
from typing import Callable

from openai import OpenAI
import anthropic



def retry_with_exponential_backoff(
    func,
    max_retries: int = 20,
    initial_sleep_time: float = 1.0,
    backoff_factor: float = 1.5,
) -> Callable:
    """
    Retry a function with exponential backoff.

    This decorator retries the wrapped function in case of rate limit errors, using an exponential backoff strategy to
    increase the wait time between retries.

    Args:
        func (callable): The function to be retried.
        max_retries (int): Maximum number of retry attempts. Defaults to 20.
        initial_sleep_time (float): Initial sleep time in seconds. Defaults to 1.
        backoff_factor (float): Factor by which the sleep time increases after each retry. Defaults to 1.5.

    Returns:
        callable: A wrapped version of the input function with retry logic.

    Raises:
        Exception: If the maximum number of retries is exceeded.
        Any other exception raised by the function that is not a rate limit error.

    Note:
        This function specifically handles rate limit errors. All other exceptions
        are re-raised immediately.
    """

    def wrapper(*args, **kwargs):
        sleep_time = initial_sleep_time

        for _ in range(max_retries):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                if "rate limit" in str(e).lower().replace("_", " "):
                    sleep_time *= backoff_factor
                    time.sleep(sleep_time)
                else:
                    raise e

        raise Exception(f"Maximum retries {max_retries} exceeded")

    return wrapper

#getting all the models from openai and anthropic


def get_openai_model_list():
    openai_client = OpenAI(
        api_key = os.getenv('OPENAI_API_KEY')
    )
    openai_model_details = openai_client.models.list()
    openai_models = []
    for model_details in openai_model_details:
        openai_models.append(model_details.id)
    return openai_models

def get_anthropic_model_list():
    anthropic_client = anthropic.Anthropic()
    anthropic_models = []
    for model_details in anthropic_client.models.list():
        anthropic_models.append(model_details.id)
    return anthropic_models
