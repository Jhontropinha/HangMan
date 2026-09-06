import random
import os
import unicodedata

def remover_acentos(texto):
    """Remove acentos de uma string (ex: 'É' vira 'E', 'Ã' vira 'A')."""
    return ''.join(
        c for c in unicodedata.normalize('NFD', texto)
        if unicodedata.category(c) != 'Mn'
    )

def carregar_palavras(caminho_arquivo="palavras.txt"):
    """Lê o arquivo de palavras e retorna uma lista de tuplas (palavra, dica)."""
    if not os.path.exists(caminho_arquivo):
        return [
            ("PYTHON", "Linguagem de programação versátil"),
            ("ABACAXI", "Fruta tropical com coroa"),
            ("COMPUTADOR", "Máquina para processamento de dados")
        ]
    
    palavras = []
    with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            linha = linha.strip()
            if ":" in linha:
                palavra, dica = linha.split(":", 1)
                palavras.append((palavra.strip().upper(), dica.strip()))
    return palavras

def desenhar_forca(erros):
    """Exibe o estágio atual do boneco na forca."""
    estagios = [
        """
           +---+
           |   |
               |
               |
               |
               |
        =========""",
        """
           +---+
           |   |
           O   |
               |
               |
               |
        =========""",
        """
           +---+
           |   |
           O   |
           |   |
               |
               |
        =========""",
        """
           +---+
           |   |
           O   |
          /|   |
               |
               |
        =========""",
        """
           +---+
           |   |
           O   |
          /|\\  |
               |
               |
        =========""",
        """
           +---+
           |   |
           O   |
          /|\\  |
          /    |
               |
        =========""",
        """
           +---+
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        ========="""
    ]
    return estagios[erros]

def jogar():
    palavras = carregar_palavras()
    palavra_secreta, dica = random.choice(palavras)
    palavra_sem_acento = remover_acentos(palavra_secreta)
    
    letras_descobertas = ["_" if letra.isalpha() else letra for letra in palavra_secreta]
    letras_tentadas = set()
    erros = 0
    max_erros = 6

    print("=" * 40)
    print("      JOGO DA FORCA EM PYTHON      ")
    print("=" * 40)
    print(f"DICA: {dica}\n")

    while erros < max_erros and "_" in letras_descobertas:
        print(desenhar_forca(erros))
        print("\nPalavra: " + " ".join(letras_descobertas))
        print(f"Letras tentadas: {', '.join(sorted(letras_tentadas)) if letras_tentadas else 'Nenhuma'}")
        
        chute = input("\nDigite uma letra: ").strip().upper()
        chute_sem_acento = remover_acentos(chute)

        if len(chute) != 1 or not chute.isalpha():
            print("\n[!] Por favor, digite apenas uma letra válida.")
            continue
        
        if chute_sem_acento in letras_tentadas:
            print(f"\n[!] Você já tentou a letra '{chute}'. Tente outra!")
            continue

        letras_tentadas.add(chute_sem_acento)

        if chute_sem_acento in palavra_sem_acento:
            print(f"\n[✓] Boa! A letra '{chute}' está na palavra.")
            for i, letra in enumerate(palavra_sem_acento):
                if letra == chute_sem_acento:
                    letras_descobertas[i] = palavra_secreta[i]
        else:
            erros += 1
            print(f"\n[X] Que pena! A letra '{chute}' não está na palavra. Tentativas restantes: {max_erros - erros}")

    print(desenhar_forca(erros))
    if "_" not in letras_descobertas:
        print("\n" + "=" * 40)
        print(f"PARABÉNS! Você venceu. A palavra era: {palavra_secreta}")
        print("=" * 40)
    else:
        print("\n" + "=" * 40)
        print(f"GAME OVER! Você perdeu. A palavra era: {palavra_secreta}")
        print("=" * 40)

if __name__ == "__main__":
    jogar()