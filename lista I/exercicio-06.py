#Calcule o tempo de uma viagem de carro. Pergunte a dist�ncia a percorrer e a velocidade m�dia esperada para a viagem.

print 'Exerc�cio-06'
print
distancia = float(raw_input('Digite a dist�ncia a percorrer (km): '))
velocidade = float(raw_input('Digite a velocidade m�dia (km): '))
tempo = 60
velocidade = velocidade * 1000 # converter em metro
distancia = distancia * 1000 # converter em metro
valor = (tempo * distancia)
resultado = valor / velocidade

print 'Resultado � %s' %resultado


