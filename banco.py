import sqlite3
from flask import Flask, request, jsonify

app = Flask(__name__)

def conectar_banco():
    conexao = sqlite3.connect('veiculos.db')
    cursor = conexao.cursor()  
    return conexao, cursor

def criar_tabela_veiculos():
    conexao, cursor = conectar_banco()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Veiculos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        placa TEXT NOT NULL,
        marca TEXT NOT NULL,
        modelo TEXT NOT NULL,
        ano INTEGER NOT NULL,
        cor TEXT NOT NULL,
        tipo_veiculo TEXT NOT NULL
        )
    ''')
    conexao.commit()
    conexao.close()

@app.route('/verificar_cadastro_veiculo', methods=['GET'])
def verificar_cadastro_veiculo():
    placa = request.args.get('placa')
    if not placa:
        return jsonify({"error": "Parâmetro placa é obrigatório"}), 400
    
    conexao, cursor = conectar_banco()
    if conexao is None or cursor is None:
        print("Não foi possível conectar ao banco de dados.")
        return
    criar_tabela_veiculos()
    cursor.execute('SELECT * FROM Veiculos WHERE placa = ?', (placa,))
    veiculos = cursor.fetchall()
    conexao.close()
    
    if veiculos:
        return jsonify({"result": True})
    else:
        return jsonify({"result": False})
    
@app.route('/listar_veiculo_unico', methods=['GET'])
def listar_veiculo_unico():
    placa = request.args.get('placa')
    if not placa:
        return jsonify({"error": "Parâmetro placa é obrigatório"}), 400
    
    conexao, cursor = conectar_banco()
    if conexao is None or cursor is None:
        return jsonify({"error": "Não foi possível conectar ao banco de dados."}), 500
    
    try:
        cursor.execute('SELECT * FROM Veiculos WHERE placa = ?', (placa,))
        veiculo = cursor.fetchone() 
        if veiculo:
            veiculo_dict = {
                "placa": veiculo[1],
                "marca": veiculo[2],
                "modelo": veiculo[3],
                "ano": veiculo[4],
                "cor": veiculo[5],
                "tipo_veiculo": veiculo[6]
            }
            return jsonify(veiculo_dict)
        else:
            return jsonify({"error": "Veículo não cadastrado."}), 404
    except sqlite3.Error as e:
        return jsonify({"error": f"Erro ao executar a consulta: {e}"}), 500
    finally:
        conexao.close()

@app.route('/listar_veiculos', methods=['GET'])
def listar_veiculos():
    placa = request.args.get('placa')
    if not placa:
        return jsonify({"error": "Parâmetro placa é obrigatório"}), 400
    
    conexao, cursor = conectar_banco()
    if conexao is None or cursor is None:
        print("Não foi possível conectar ao banco de dados.")
        return
    cursor.execute('SELECT * FROM Veiculos')
    veiculos = cursor.fetchall()
    for veiculo in veiculos:
        veiculo_dict = {
                "placa": veiculo[1],
                "marca": veiculo[2],
                "modelo": veiculo[3],
                "ano": veiculo[4],
                "cor": veiculo[5],
                "tipo_veiculo": veiculo[6]
            }
        return jsonify(veiculo_dict)
    conexao.close()
        
@app.route('/inserir_veiculo', methods=['POST'])
def inserir_veiculo():
    dados = request.get_json()
    placa = dados.get('placa')
    marca = dados.get('marca')
    modelo = dados.get('modelo')
    ano = dados.get('ano')
    cor = dados.get('cor')
    tipo_veiculo = dados.get('tipo_veiculo')
    
    if not all([placa, marca, modelo, ano, cor, tipo_veiculo]):
        return jsonify({"error": "Todos os campos são obrigatórios."}), 400

    conexao, cursor = conectar_banco()
    if conexao is None or cursor is None:
        return jsonify({"error": "Não foi possível conectar ao banco de dados."}), 500
    
    cursor.execute('''
    INSERT INTO Veiculos (placa, marca, modelo, ano, cor, tipo_veiculo)
    VALUES (?, ?, ?, ?, ?, ?)
    ''', (placa, marca, modelo, ano, cor, tipo_veiculo))
    conexao.commit()
    conexao.close()
    
    return jsonify({"message": "Veículo inserido com sucesso!"}), 201
    
@app.route('/atualizar_veiculo', methods=['PUT'])
def atualizar_veiculo(veiculo):
    conexao, cursor = conectar_banco()
    if conexao is None or cursor is None:
        print("Não foi possível conectar ao banco de dados.")
        return
    try:
        cursor.execute('''
        UPDATE Veiculos
        SET marca = ?, modelo = ?, ano = ?, cor = ?, tipo_veiculo = ?
        WHERE placa = ?
        ''', (veiculo.marca, veiculo.modelo, veiculo.ano, veiculo.cor, veiculo.tipo_veiculo, veiculo.placa))
        conexao.commit()
    except sqlite3.Error as e:
        print(f"Erro ao atualizar o veículo: {e}")
    finally:
        conexao.close()

@app.route('/excluir_veiculo', methods=['DELETE'])
def excluir_veiculo():
    placa = request.args.get('placa')
    if not placa:
        return jsonify({"error": "Parâmetro placa é obrigatório"}), 400
    
    conexao, cursor = conectar_banco()
    if conexao is None or cursor is None:
        print("Não foi possível conectar ao banco de dados.")
        return
    cursor.execute('DELETE FROM Veiculos WHERE placa = ?', (placa,))
    conexao.commit()
    conexao.close()
    
if __name__ == '__main__':
    app.run(debug=True)
