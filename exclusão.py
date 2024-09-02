from banco import verificar_cadastro_veiculo, excluir_veiculo, listar_veiculo_unico

placa_veiculo = int(input('Digite a placa do veículo:\n'))

veiculo_existe = verificar_cadastro_veiculo(placa_veiculo)

if not veiculo_existe:
    print("Veículo {} não cadastrado" .format(placa_veiculo))
else: 
    listar_veiculo_unico(placa_veiculo)
    confirmacao = ""

    while True:
        confirmacao = input('Digite "EXCLUIR" para excluir o veículo e "CANCELAR" para desistir da ação.\n') 
    
        if confirmacao == "EXCLUIR":
            excluir_veiculo(placa_veiculo)
            print("Veículo excluído com sucesso.")
            break
        elif confirmacao == "CANCELAR":
            print("Operação cancelada.")
            break
        else:
            print("Entrada inválida. Tente novamente.")