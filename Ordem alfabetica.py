lista = []
frase = str(input('Digite uma frase: ').title())
frase2 = str(input('Digite outra frase: ').title())
frase3 = str(input('Digite outra frase: ').title())
lista.extend([frase, frase2, frase3])
lista.sort()
print(", ".join(lista))