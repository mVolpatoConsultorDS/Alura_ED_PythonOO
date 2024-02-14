def contar_letra(palavra):
    letras = []
    for i in palavra:
        letras.append(i[0])
        if i[0] == 'm':
            print(i[0])
        else:
            print('not m')
        #print(i[0])
    return len(letras)

def for_inverso(palavra):
    letras = []
    for i in palavra[::-1]:
        letras.append(i[0])
        print(i[0])
    return

def invertir(palabra):
    return palabra[::-1]

palavra = input('Digite Palavra: ')

print(f'A palavra {palavra} tem {contar_letra(palavra)} letras\n')

print(invertir(palavra))

for_inverso(palavra)