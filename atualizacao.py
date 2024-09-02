from estruturas import Veiculo
from banco import verificar_cadastro_veiculo, atualizar_veiculo

placa_veiculo = int(input('Digite a placa do veículo:\n'))

veiculo_existe = verificar_cadastro_veiculo(placa_veiculo)

if not veiculo_existe:
    print("Veículo {} não está cadastrado".format(placa_veiculo))
else:
    marca = input('Digite a marca do veículo:\n')
    modelo = input('Digite o modelo do veículo:\n')
    ano = int(input('Digite o ano do veículo:\n'))
    cor = input('Digite a cor do veículo:\n')
    tipo_veiculo = input('Digite o tipo do veículo:\n')
    
    automovel = Veiculo(marca, modelo, ano, cor, tipo_veiculo)
    automovel.placa = placa_veiculo
    
    atualizar_veiculo(automovel)

    print("Atualização do veículo ID {} realizado com sucesso!" .format(placa_veiculo))
