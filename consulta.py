from banco import listar_veiculos, listar_veiculo_unico

escolha = int(input("Se deseja consultar um veículo especifico, digite 1. Caso contrário, digite 0.\n"))
if escolha == 1:
    identificacao_veiculo = int(input('Digite o número de identificação do veículo:\n'))
    listar_veiculo_unico(identificacao_veiculo)
else: 
    listar_veiculos()