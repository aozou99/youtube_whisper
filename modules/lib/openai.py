import openai
import os
from dotenv import load_dotenv
load_dotenv()


def summarize_text(text):
    openai.api_key = os.environ.get("OPENAI_API_KEY")

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"Please summarize the following text:\n\n{text}\n",
        max_tokens=200,
        n=1,
        stop=None,
        temperature=0.5,
    )

    return response.choices[0].text.strip()
