import re
from collections import Counter

def ler_arquivo(nome_arquivo):
    with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
        texto = arquivo.read()
    return texto

def contar_palavras(texto):
    palavras = re.findall(r'\b\w+\b', texto.lower())  # Considera palavras e ignora case
    return len(palavras), Counter(palavras)

def substituir_palavra(texto, palavra_antiga, palavra_nova):
    return texto.replace(palavra_antiga, palavra_nova)

def main():
    nome_arquivo = input("Digite o nome do arquivo de texto: ")

    try:
        # Ler o arquivo
        texto = ler_arquivo(nome_arquivo)

        # Contar palavras e frequências
        total_palavras, frequencias = contar_palavras(texto)
        print(f"Número total de palavras: {total_palavras}")
        print("Frequência de cada palavra:")
        for palavra, freq in frequencias.items():
            print(f"{palavra}: {freq}")

        # Substituir palavras
        palavra_antiga = input("Digite a palavra a ser substituída: ")
        palavra_nova = input("Digite a nova palavra: ")
        texto_substituido = substituir_palavra(texto, palavra_antiga, palavra_nova)

        # Escrever o novo texto em um novo arquivo
        novo_nome_arquivo = "texto_substituido.txt"
        with open(novo_nome_arquivo, 'w', encoding='utf-8') as arquivo:
            arquivo.write(texto_substituido)

        print(f"A palavra '{palavra_antiga}' foi substituída por '{palavra_nova}' e o novo texto foi salvo em '{novo_nome_arquivo}'.")

    except FileNotFoundError:
        print("Arquivo não encontrado. Verifique o nome e tente novamente.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

# Executar o programa
if __name__ == "__main__":
    main()
