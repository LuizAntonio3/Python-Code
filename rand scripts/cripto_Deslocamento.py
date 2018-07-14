deslocamento = int(input("Qual o deslocamento? (int)\n"))
arquivo = input("Texto a ser realocado (nome do arquivo txt)\n")

with open(arquivo, 'r') as arqTexto:
    texto = arqTexto.read()

textoRealocado = ""

for i in range(0, len(texto) - 1):
    it = texto[i]
    if it == ' ':
        textoRealocado = textoRealocado + it
        continue
    elif it == '.':
        textoRealocado = textoRealocado + it
        continue
    elif it == "'":
        textoRealocado = textoRealocado + it
        continue
    elif it == '(':
        textoRealocado = textoRealocado + it
        continue
    elif it == ')':
        textoRealocado = textoRealocado + it
        continue
    elif ord(it) + deslocamento > 122:
        textoRealocado = textoRealocado + chr(ord(it) - 26 + deslocamento)
    else:
        textoRealocado = textoRealocado + chr(ord(it) + deslocamento)

with open('resp.txt', 'w') as f:
    f.write(textoRealocado)
