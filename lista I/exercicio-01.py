#Faça um programa que peça dois números inteiros e imprima a soma desses dois números

print 'Exercício-01'
print ''
cont = 1
valor1 = 0
soma = 0
while (cont < 3):
    v1 = raw_input('Digite um número inteiro (Valor %s): ' %cont)
    if not v1:
        print 'Campo em branco, por favor digite um número inteiro'
    elif type(v1) == float:
        print 'Você digitou %s. Apenas número inteiro' %v1
    else:
        try:
            valor1 = int(v1)
            soma += valor1
            cont += 1

        # Caso ele tente converter um string q não seja número, ele vai cair no except e rodar d novo.
        except: 
            print 'Você digitou %s. Apenas número inteiro' %v1

print 'O resultado da soma é: %s' %soma

    
         
