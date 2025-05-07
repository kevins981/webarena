"""Tools to generate from OpenAI prompts.
Adopted from https://github.com/zeno-ml/zeno-build/"""

import logging
import os
import random
import time
from typing import Any

import openai
#import openai.error


#def retry_with_exponential_backoff(  # type: ignore
#    func,
#    initial_delay: float = 1,
#    exponential_base: float = 2,
#    jitter: bool = True,
#    max_retries: int = 3,
#    errors: tuple[Any] = (openai.error.RateLimitError,),
#):
#    """Retry a function with exponential backoff."""
#
#    def wrapper(*args, **kwargs):  # type: ignore
#        # Initialize variables
#        num_retries = 0
#        delay = initial_delay
#
#        # Loop until a successful response or max_retries is hit or an exception is raised
#        while True:
#            try:
#                return func(*args, **kwargs)
#            # Retry on specified errors
#            except errors as e:
#                # Increment retries
#                num_retries += 1
#
#                # Check if max retries has been reached
#                if num_retries > max_retries:
#                    raise Exception(
#                        f"Maximum number of retries ({max_retries}) exceeded."
#                    )
#
#                # Increment the delay
#                delay *= exponential_base * (1 + jitter * random.random())
#                print(f"Retrying in {delay} seconds.")
#                # Sleep for the delay
#                time.sleep(delay)
#
#            # Raise exceptions for any errors not specified
#            except Exception as e:
#                raise e
#
#    return wrapper

def generate_from_centml_chat_completion(
    messages: list[dict[str, str]],
    model: str,
    temperature: float,
    max_tokens: int,
    top_p: float,
    context_length: int,
    client, 
    stop_token: str | None = None,
) -> str:
    if "CENTML_API_KEY" not in os.environ:
        raise ValueError(
            "CENTML_API_KEY environment variable must be set when using OpenAI API."
        )
    print("==== centml generate model ", model)
    print("==== centml generate input ", messages[:100])

    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature,
        max_tokens=max_tokens,
        top_p=top_p,
        stop=[stop_token] if stop_token else None,
    )
    print("==== centml generate response usage", response.usage)
    #print("==== centml generate response 3", response.choices[0])
    #print("==== centml generate response 4", response.choices[0]["message"])
    answer: str = response.choices[0].message.content
    print("==== centml generate answer ", answer)
    return answer


