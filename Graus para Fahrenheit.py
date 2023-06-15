'''Faça um programa que recebe uma temperatura em graus Celsius e a converte para Fahrenheit. Se a temperatura em Fahrenheit for maior do que 100 graus, exiba uma mensagem de alerta.'''
graus = float(input('Quantos graus está em sua região? '))
fah = (graus * 1.8) + 32
cores = {'limpa' : '\033[m',
        'quente' : '\033[1;31m', 
          'medio' : '\033[1;33m',
           'fresco': '\033[1;32m' }
if fah >=100 :
    print(f'{cores["quente"]}Alerta, a temperatura está muito alta recomendamos que não se exponha ao sol e se mantenha em lugar fresco e arejado.{cores["limpa"]}')

elif fah >= 81 :
    print(f'{cores["medio"]}A temperatura está relativamente alta, lembre se de utilizar protetor solar.{cores["limpa"]}')

else:
    print(f'{cores["fresco"]}A temperatura não está tão alta mas lembre se de usar protetor solar em caso de exposição ao sol :){cores["limpa"]}')