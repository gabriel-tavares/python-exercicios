#Faça um programa que calcule o aumento de um salário. Ele deve solicitar o valor do salário e a porcentagem do aumento. Exiba o valor do aumento e do novo salário.

print 'Exercício-04'
print
salario = float(raw_input('Digite seu salário: '))
aumento = float(raw_input('Digite de quanto foi o aumento: '))
resultado = aumento / 100 * salario
salario = salario + resultado
print
print 'Seu aumento foi de %s' %resultado
print 'Totalizando %s' %salario
                        
