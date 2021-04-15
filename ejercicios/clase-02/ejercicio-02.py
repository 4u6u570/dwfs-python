# 2. Escribe un programa Python que acepte un número entero (n) y calcule el valor de n + nn + nnn

n = input('Escriba el valor de n: ')

nn = int('{}{}'.format(n, n))
nnn = int('%s%s%s'% (n, n, n))
n = int(n)

suma = n + nn + nnn
print(suma)
