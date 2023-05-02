palavra_secreta = ["m","o","r","a","n","g","o"]
letras_descobertas = []

print("\n*** jogo da forca ***\n")

for i in range(0, len(palavra_secreta)):
    letras_descobertas.append("-")

acertou = False

while acertou == False :
    letra = str(input("digite a letra: "))

    for i in range(0, len(palavra_secreta)):
        if letra == palavra_secreta[i] :
            letras_descobertas[i] = letra