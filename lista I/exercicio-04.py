#Fa�a um programa que calcule o aumento de um sal�rio. Ele deve solicitar o valor do sal�rio e a porcentagem do aumento. Exiba o valor do aumento e do novo sal�rio.

print 'Exerc�cio-04'
print
salario = float(raw_input('Digite seu sal�rio: '))
aumento = float(raw_input('Digite de quanto foi o aumento: '))
resultado = aumento / 100 * salario
salario = salario + resultado
print
print 'Seu aumento foi de %s' %resultado
print 'Totalizando %s' %salario
                        
