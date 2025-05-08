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


def red_flags(texto):
    url = "https://openrouter.ai/api/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
        "X-Title": "CerebroLegal",  # opcional
    }

    prompt = (
        "Revisá el siguiente texto legal y buscá posibles 'red flags' o cláusulas problemáticas. "
        "En particular, indicá si hay:\n"
        "- Permisos excesivos o vagos.\n"
        "- Obligaciones injustas para el usuario.\n"
        "- Límites poco claros sobre responsabilidad.\n"
        "- Lenguaje confuso o difícil de interpretar.\n\n"
        "Por cada red flag encontrada:\n"
        "- Copiá la cláusula sospechosa (o parte de ella).\n"
        "- Explicá en lenguaje simple por qué puede ser un problema.\n\n"
        "Texto legal a analizar:\n\n"
        f"{texto}"
    )

    payload = {
        "model": "deepseek/deepseek-r1:free",
        "messages": [
            {
                "role": "user",
                "content": prompt
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


def revision_de_permisos(texto):
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
                "content": f"Analizá el siguiente contrato y describí qué permisos o derechos está otorgando cada parte. Enfocate en identificar si una de las partes está otorgando más permisos o cediendo más derechos que la otra, y explicá esos puntos de forma clara y resumida:\n\n{texto}"
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
    
    opcion = input("Opcion que quieres que cerebro legal haga : Explicacion simplificada (A). Busqueda de Red Flags en Doc/Contrato(B). Revsion de permisos/derechos otorgados por cada parte(C)").lower() #Ususario decide la accion de cerebro

    print("=" * 50)

    if opcion == "a":
        texto = input("Pegá el texto legal que querés entender:\n\n")
        print("\n Explicación simplificada:\n")
        resultado = explicar_legal(texto)
        print(resultado)

    elif opcion == "b":
        texto = input("Ingresa el Doc/Contrato:\n\n")
        print("\n Posibles red flags:\n")
        resultado = red_flags(texto)
        print(resultado)

    elif opcion == "c":
        texto = input("Ingresa Doc/Contrato:\n\n")
        print("\n Analsis de forma clara:\n")
        resultado = revision_de_permisos(texto)
        print(resultado)




if __name__ == "__main__":
    main()
 