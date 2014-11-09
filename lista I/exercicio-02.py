#Escreva um programa que leia um valor em metros e o exiba convertido em milímetros

print 'Exercício-02'
print ''
print 'Conversão de Metros em Milímetros'

metros = raw_input('Metro(s): ')

if not metros:
    print 'Campo em branco, por favo digite de novo'
elif ',' in metros:
    print 'Use o . (ponto) como separador decimal.'
else:
    try:
        metros = float(metros)
        mm = metros * 1000
        print 'O valor da conversão em milímetro é:%s mm' %mm
    except:
        print 'Valor incorreto'
    
