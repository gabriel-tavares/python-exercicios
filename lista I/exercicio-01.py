#Fa�a um programa que pe�a dois n�meros inteiros e imprima a soma desses dois n�meros

print 'Exerc�cio-01'
print ''
cont = 1
valor1 = 0
soma = 0
while (cont < 3):
    v1 = raw_input('Digite um n�mero inteiro (Valor %s): ' %cont)
    if not v1:
        print 'Campo em branco, por favor digite um n�mero inteiro'
    elif type(v1) == float:
        print 'Voc� digitou %s. Apenas n�mero inteiro' %v1
    else:
        try:
            valor1 = int(v1)
            soma += valor1
            cont += 1

        # Caso ele tente converter um string q n�o seja n�mero, ele vai cair no except e rodar d novo.
        except: 
            print 'Voc� digitou %s. Apenas n�mero inteiro' %v1

print 'O resultado da soma �: %s' %soma

    
         
