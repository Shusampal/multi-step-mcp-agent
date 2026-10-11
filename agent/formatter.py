import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()


GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_MODEL_NAME = os.getenv("GROQ_MODEL_NAME")


groq_client = Groq(api_key=GROQ_API_KEY)


def format_answer(state):

    prompt = f"""

    Your task is to provide user answer in naturally humanly way

    The user asked:
    {state["user_request"]}

    Actions performed:
    {state["actions"]}

    Observations:
    {state["observations"]}

    Answer the user naturally.

    Do not mention internal planning.
    Do not mention state.
    Do not mention tools.
"""

    response = groq_client.chat.completions.create(
        model=GROQ_MODEL_NAME,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content.strip()
