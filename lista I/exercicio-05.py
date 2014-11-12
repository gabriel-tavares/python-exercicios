#Solicite  o  preço  de  uma  mercadoria  e  o  percentual  de  desconto.  Exiba  o  valor  do  desconto  e  o preço a pagar.

print 'Selecione o produto'
print 'a - produto 1'
print 'b - produto 2'
print 'c - produto 3'
selecao = raw_input('Letra do produto: ')

a = 15.50
b = 9.80
c = 7.40
desconto = 7.5


if selecao == 'a':
    print 'Produto 1 custa %s e tem %s desconto' %(a, desconto)
    resultado = desconto / 100 * a
    print 'Desconto de %.2f, novo preço %.2f' % (resultado, a - resultado)

elif selecao == 'b':
    print 'Produto 2 custa %s e tem %s desconto' %(b, desconto)
    resultado = desconto / 100 * b
    print 'Desconto de %.2f, novo preço %.2f' % (resultado, b - resultado)
else:
    print 'Produto 3 custa %s e tem %s desconto' %(c, desconto)
    resultado = desconto / 100 * c
    print 'Desconto de %.2f, novo preço %.2f' % (resultado, c - resultado)

                    

