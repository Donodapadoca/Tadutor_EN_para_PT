import requests
import json

def traduzir(palavra):
    url= "hhtps://tanslate.googleapis.com/translate_a/single?client=gtx&sl=en&tl=pt&dt=t&q="
    response = requests.get(url)
    traducao = json.loads(response.text)[0][0][0]
    return traducao

def main():
    print("Bem-vindo ao tradutor de EN -> PT")
    print("Digite 'sair' para encerrar o programa")

    while True:
        palavra = input("Digite uma palavra em inglês")
        if palavra.lower() == 'sair':
            break
        traducao = traduzir(palavra)
        print(f"Tradução: {traducao}")

if __name__ == "_main_":
    main()