from google import genai
import os
import logging
import json
from datetime import datetime
import requests
from openai import OpenAI

# Configure logging
log_directory = os.getenv("LOG_DIR", "logs")
os.makedirs(log_directory, exist_ok=True)
log_file = os.path.join(log_directory, f"llm_calls_{datetime.now().strftime('%Y%m%d')}.log")

# Set up logger
logger = logging.getLogger("llm_logger")
logger.setLevel(logging.INFO)
logger.propagate = False  # Prevent propagation to root logger
file_handler = logging.FileHandler(log_file)
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(file_handler)

# Simple cache configuration
cache_file = "llm_cache.json"

# Основная реализация с DeepSeek (раскомментируйте для использования)
def call_llm(prompt: str, use_cache: bool = True) -> str:
    # Логирование промпта
    logger.info(f"PROMPT: {prompt}")

    # Конфигурация DeepSeek API
    api_key = os.getenv("DEEPSEEK_API_KEY")
    if not api_key:
        raise ValueError("DEEPSEEK_API_KEY environment variable not set")

#     headers = {
#         "Authorization": f"Bearer {api_key}",
#         "Content-Type": "application/json"
#     }
#
#     payload = {
#         "model": os.getenv("DEEPSEEK_MODEL", "deepseek-chat"),
#         "messages": [{"role": "user", "content": prompt}],
#         "temperature": 0.7,
#         "max_tokens": 4096
#     }
#
#     try:
#         response = requests.post(
#             "https://api.deepseek.com/v1/chat/completions",
#             headers=headers,
#             json=payload
#         )
#         response.raise_for_status()
#         response_text = response.json()['choices'][0]['message']['content']
#     except Exception as e:
#         logger.error(f"API Error: {str(e)}")
#         raise

    client = OpenAI(api_key=os.getenv("DEEPSEEK_API_KEY"), base_url="https://api.deepseek.com")

    response = client.chat.completions.create(
        model=os.getenv("DEEPSEEK_MODEL", "deepseek-reasoner"),
        messages=[
            {"role": "user", "content": prompt},
        ],
        stream=False
    )
    response_text = response.choices[0].message.content

    # Логирование ответа
    logger.info(f"RESPONSE: {response_text}")

    return response_text

if __name__ == "__main__":
    test_prompt = "Hello, how are you?"

    # First call - should hit the API
    print("Making call...")
    response1 = call_llm(test_prompt, use_cache=False)
    print(f"Response: {response1}")
