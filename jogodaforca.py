import random

def escolher_palavra():
    palavras = ["python", "javascript", "java", "html", "css", "ruby", "php"]
    return random.choice(palavras)

def exibir_palavra(palavra, letras_adivinhadas):
    exibicao = ""
    for letra in palavra:
        if letra in letras_adivinhadas:
            exibicao += letra
        else:
            exibicao += "_"
    return exibicao

def jogar_forca():
    palavra_secreta = escolher_palavra()
    letras_adivinhadas = set()
    tentativas_restantes = 6

    print("Bem-vindo ao Jogo da Forca!")
    print(exibir_palavra(palavra_secreta, letras_adivinhadas))

    while tentativas_restantes > 0:
        palpite = input("Digite uma letra: ")

        if palpite in letras_adivinhadas:
            print("Você já tentou essa letra. Tente outra.")
            continue

        letras_adivinhadas.add(palpite)

        if palpite not in palavra_secreta:
            tentativas_restantes -= 1
            print(f"Incorreto! Você tem {tentativas_restantes} tentativas restantes.")
        else:
            print("Correto!")

        exibicao_atual = exibir_palavra(palavra_secreta, letras_adivinhadas)
        print(exibicao_atual)

        if "_" not in exibicao_atual:
            print("Parabéns! Você venceu!")
            break

    if tentativas_restantes == 0:
        print(f"Fim de jogo! A palavra correta era: {palavra_secreta}")

if __name__ == "__main__":
    jogar_forca()
