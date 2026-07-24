from openai_client import client
from openai import (
    AuthenticationError,
    APIConnectionError,
    APITimeoutError,
    RateLimitError,
    BadRequestError,
)
from config import MODEL
from prompts import SYSTEM_PROMPT
from logger import logger
logger.info("Application started")

messages = [
    {
        "role": "system",
        "content": SYSTEM_PROMPT
    }
]


def start_chat():

    print("=" * 60)
    print("🤖 AI Chat Application")
    print("Type 'exit' to quit.")
    print("=" * 60)

    while True:

        user_prompt = input("\nYou: ")

        if user_prompt.lower() == "exit":
            print("Goodbye! 👋")
            break

        messages.append(
            {
                "role": "user",
                "content": user_prompt
            }
        )

        try:
            logger.info("calling OpenAI API")
            response = client.chat.completions.create(
                model=MODEL,
                messages=messages,
                stream=True             


            )
            
            assistant_reply = ""
            for chunk in response:
                if chunk.choices[0].delta.content:
                    content = chunk.choices[0].delta.content
                    print(content, end="", flush=True)
                    assistant_reply += content
            print() 
            logger.info("response received from OpenAI API")
            messages.append(
                {
                    "role": "assistant",
                    "content": assistant_reply
                }
            )

        except AuthenticationError:
            logger.error("Authentication failed. Check your OpenAI API key.")

        except RateLimitError:
            logger.error("Rate limit exceeded. Please try again later.")

        except APITimeoutError:
            logger.error("The request timed out.")

        except APIConnectionError:
            logger.error("Unable to connect to the OpenAI API.")

        except BadRequestError as e:
            logger.error(f"Bad request: {e}")
