import requests
import json
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("OPENROUTER_API_KEY")


def explicar_legal(texto):
    url = "https://openrouter.ai/api/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
        "X-Title": "CerebroLegal",  # opcional
    }

    payload = {
        "model": "deepseek/deepseek-r1:free",
        "messages": [
            {
                "role": "user",
                "content": f"Explicá el siguiente texto legal como si tuvieras 15 años:\n\n{texto}"
            }
        ],
        "temperature": 0.5,
        "max_tokens": 700
    }

    try:
        response = requests.post(url, headers=headers, data=json.dumps(payload))
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"]
    except Exception as e:
        return f" Error al conectarse a OpenRouter: {e}"

def main():
    print(" CerebroLegal - Versión Consola")
    print("=" * 50)
    texto = input("Pegá el texto legal que querés entender:\n\n")
    print("\n Explicación simplificada:\n")
    resultado = explicar_legal(texto)
    print(resultado)

if __name__ == "__main__":
    main()
 