print('{:=^40}'.format('DAMIÃOELTRO'))
prec = float(input('Digite o preço do produto: R$'))
print('''FORMAS DE PAGAMENTOS
[1] à vista dinheiro/cheque
[2] à visra no cartão
[3] 2x no cartão
[4] 3x ou mais no cartão''')
condit = int(input('Qual é a opção: '))
if condit == 1:
  nprec = prec-(prec* 10 / 100)
  print(nprec)
elif condit == 2:
    cprec = prec-(prec*10/100) #preço a vista no cartão
    print(cprec)
elif condit == 3:
    cprec2 = prec/2 #preço em 2 vezes no cartão
    print(f'Sua compra de {prec } parcelada em 2 vezes é {cprec2} SEM JUROS.')
elif condit == 4:
    cprec3 = prec+(prec*20/100)
    totparc = int(input('Quantas parcelas?'))
    parcelas = cprec3 / totparc
    print(f'Sua compra de R${prec} parcelada em {totparc} vezes é {parcelas} COM JUROS.')
else:
    print('Forma de pagamento invalida')
print('{:=^20}'.format('FIM'))
