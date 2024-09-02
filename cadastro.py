from estruturas import Veiculo
from banco import verificar_cadastro_veiculo, inserir_veiculo

placa_veiculo = int(input('Digite a placa do veículo:\n'))

veiculo_existe = verificar_cadastro_veiculo(placa_veiculo)

if veiculo_existe:
    print("Veículo {} já cadastrado".format(placa_veiculo))
else:
    marca = input('Digite a marca do veículo:\n')
    modelo = input('Digite o modelo do veículo:\n')
    ano = int(input('Digite o ano do veículo:\n'))
    cor = input('Digite a cor do veículo:\n')
    tipo_veiculo = input('Digite tipo do veículo:\n')
    
    automovel = Veiculo(marca, modelo, ano, cor, tipo_veiculo)
    automovel.placa = placa_veiculo
    
    inserir_veiculo(automovel)
    
    print("Cadastro do veículo ID {} realizado com sucesso!" .format(placa_veiculo))