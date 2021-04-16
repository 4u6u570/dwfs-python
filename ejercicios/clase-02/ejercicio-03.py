## 3. Escribe un programa en Python que acepte una cadena de caracteres y cuente el tamaño de la cadena y cuantas veces aparece la letra A (mayuscula y minúscula)

def contar_digitos_letras(cadena):
    digitos = 0
    letras = 0

    for c in cadena:
        if c.isdigit():
            digitos += 1
        elif c == 'a'or c == 'A':
            letras += 1
        else:
            pass

    return digitos, letras


texto = input('Digite un texto: ')
resultado = contar_digitos_letras(texto)

print('Cantidad de dígitos: %i' % resultado[0])
print('Cantidad de letras A: %i' % resultado[1])