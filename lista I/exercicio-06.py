#Calcule o tempo de uma viagem de carro. Pergunte a distância a percorrer e a velocidade média esperada para a viagem.

print 'Exercício-06'
print
distancia = float(raw_input('Digite a distância a percorrer (km): '))
velocidade = float(raw_input('Digite a velocidade média (km): '))
tempo = 60
velocidade = velocidade * 1000 # converter em metro
distancia = distancia * 1000 # converter em metro
valor = (tempo * distancia)
resultado = valor / velocidade

print 'Resultado é %s' %resultado


