import os
from dotenv import load_dotenv
from openai import OpenAI
import argparse

def main():
    load_dotenv()

    api_key = os.environ.get("OPENROUTER_API_KEY")
    if not api_key:
        raise RuntimeError("Could not find Openrouter API key in .env file")

    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key,
    )

    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    args = parser.parse_args()

    model = 'openrouter/free'
    messages=[
        {
            "role": "user",
            "content": args.user_prompt,
        }
    ]

    response = client.chat.completions.create(model=model, messages=messages)

    if not response.usage.prompt_tokens or not response.usage.completion_tokens:
        raise RuntimeError("Returned tokens are None, they may be an issue with the model")

    print(f"Prompt tokens: {response.usage.prompt_tokens}")
    print(f"Response tokens: {response.usage.completion_tokens}")
    
    print(response.choices[0].message.content)

if __name__ == "__main__":
    main()
