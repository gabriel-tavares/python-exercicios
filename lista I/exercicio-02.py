#Escreva um programa que leia um valor em metros e o exiba convertido em mil�metros

print 'Exerc�cio-02'
print ''
print 'Convers�o de Metros em Mil�metros'

metros = raw_input('Metro(s): ')

if not metros:
    print 'Campo em branco, por favo digite de novo'
elif ',' in metros:
    print 'Use o . (ponto) como separador decimal.'
else:
    try:
        metros = float(metros)
        mm = metros * 1000
        print 'O valor da convers�o em mil�metro �:%s mm' %mm
    except:
        print 'Valor incorreto'
    
