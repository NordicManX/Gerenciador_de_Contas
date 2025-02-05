from flask import Flask, request, jsonify, render_template

app = Flask(__name__, template_folder="templates")

# Armazena o salário e as contas
dados = {
    "salario": 0,
    "contas": []
}

@app.route("/")
def index():
    return render_template("index.html")  # Certifique-se de que o HTML está na pasta "templates"

@app.route("/definir-salario", methods=["POST"])
def definir_salario():
    salario = request.json.get("salario", 0)

    if salario <= 0:
        return jsonify({"status": "error", "message": "Salário inválido, deve ser maior que zero!"})
    
    dados["salario"] = salario
    return jsonify({"status": "success", "saldo": dados["salario"]})

@app.route("/adicionar", methods=["POST"])
def adicionar_conta():
    descricao = request.json.get("descricao")
    valor = request.json.get("valor")

    if not descricao:
        return jsonify({"status": "error", "message": "Descrição da conta não pode estar vazia!"})

    if not isinstance(valor, (int, float)) or valor <= 0:
        return jsonify({"status": "error", "message": "Valor inválido! O valor deve ser maior que zero."})

    dados["contas"].append({"descricao": descricao, "valor": valor})
    return jsonify({"status": "success"})

@app.route("/listar", methods=["GET"])
def listar_contas():
    total_contas = sum(conta["valor"] for conta in dados["contas"])
    saldo_atual = dados["salario"] - total_contas  # Ajusta o saldo corretamente

    return jsonify({"contas": dados["contas"], "saldo": saldo_atual, "total": total_contas})

@app.route("/editar", methods=["POST"])
def editar_conta():
    index = request.json.get("index")
    nova_descricao = request.json.get("descricao")
    novo_valor = request.json.get("valor")

    if index is None or not (0 <= index < len(dados["contas"])):
        return jsonify({"status": "error", "message": "Índice inválido!"})

    if not nova_descricao:
        return jsonify({"status": "error", "message": "Descrição da conta não pode estar vazia!"})

    if not isinstance(novo_valor, (int, float)) or novo_valor <= 0:
        return jsonify({"status": "error", "message": "Valor inválido! O valor deve ser maior que zero."})

    dados["contas"][index] = {"descricao": nova_descricao, "valor": novo_valor}
    return jsonify({"status": "success"})

@app.route("/remover", methods=["POST"])
def remover_conta():
    index = request.json.get("index")

    if index is None or not (0 <= index < len(dados["contas"])):
        return jsonify({"status": "error", "message": "Índice inválido!"})

    dados["contas"].pop(index)
    return jsonify({"status": "success"})

if __name__ == "__main__":
    app.run(debug=False)
