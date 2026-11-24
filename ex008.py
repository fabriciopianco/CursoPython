# Crie um programa que leia um valor em metro e exiba convertido em centimetros e milimitros.

m = float(input('Digite um valor em metros: '))
c = m * 100
mm = m * 1000

print('Metros: {}\nCentimetros: {}\nMilimetros: {}'.format(m, c, mm))