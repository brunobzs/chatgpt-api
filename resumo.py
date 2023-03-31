import openai
from dotenv import load_dotenv
import os

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")


def ler_arquivo(arquivo):
    with open(arquivo, 'r', encoding='utf-8') as f:
        return f.read()


def criar_resumo(texto):
    resposta = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Resuma o texto: {texto}",
        temperature=0.8,
        max_tokens=2048,
        n=1,
        stop=None
    )
    return resposta['choices'][0]['text']


arquivo = 'texto.txt'
texto = ler_arquivo(arquivo)
print(criar_resumo(texto))
