# Crie um progama que leia um numero e mostre seu dobro, triplo e sua raiz quadrada.

n = int(input('Digite um numero: '))
d = n * 2
t = n * 3
rq = n ** (1/2)
print('O dobro é: {} \nO triple é: {} \nA raiz quadrada é: {:.2f}'.format(d, t, rq))