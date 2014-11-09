#Escreva um programa que leia a quantidade de dias, horas,  minutos e segundos do usuário. Calcule o total em segundos.

print 'Exercício-03'
print

dias = int(raw_input('Digite a quantidade de dias: '))
horas = int(raw_input('Digite a quantidade de horas: '))
minutos = int(raw_input('Digite a quantidade de minutos: '))
segundos = int(raw_input('Digite a quantidade de segundos: '))

print '%s Dias, %s:%s:%s ' % (dias, horas, minutos, segundos)

total = segundos +(60 *(minutos +(60 *(horas + (dias * 24)))))

print total

