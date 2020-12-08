# -*- coding: utf-8 -*-

import flask
from flask import request, json
import re

app = flask.Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return "<h1>Validação de senha</h1><p>Esta api é destinada para o desafio do Itau.</p>"

@app.route('/password/validate', methods=['GET'])
def api_id():
    if 'id' in request.args:
        id = str(request.args['id'])
    else:
        return "Error: O id não foi informado. Por favor informe um id válido."

    return test_password(id)

def test_password(password):
    message = "Senha validada"
    status = True
    # Nove ou mais caracteres
    # Ao menos 1 dígito
    # Ao menos 1 letra minúscula
    # Ao menos 1 letra maiúscula
    # Ao menos 1 caractere especial
    # Considere como especial os seguintes caracteres: !@#$%^&*()-+
    # Não possuir caracteres repetidos dentro do conjunto

    minimal_number = 1
    minimal_upper_char = 1
    minimal_lower_char = 1
    minimal_special_char = 1
    minimal_len_char = 9

    if len(password or ()) < minimal_len_char:
        message = str('Senha tem que ter no minimo '+str(minimal_len_char)+' caracteres')
        status = False
    if len(re.findall(r"[A-Z]", password)) < minimal_upper_char:
        message = str('Senha tem que ter no minimo '+str(minimal_upper_char)+' letras maiusculas')
        status = False
    if len(re.findall(r"[a-z]", password)) < minimal_lower_char:
        message = str('Senha tem que ter no minimo '+str(minimal_lower_char)+' letras minusculas')
        status = False
    if len(re.findall(r"[0-9]", password)) < minimal_number:
        message = str('Senha tem que ter no minimo '+str(minimal_number)+' numeros')
        status = False
    if len(re.findall(r"[!@#$%^&*()-+]", password)) < minimal_special_char:
        message = str('Senha tem que ter no minimo '+str(minimal_special_char)+' caracter especial')
        status = False
    if len(re.findall(r"(\w)*.*\1", password)) > 0:
        message = str('Senha nao pode ter caracteres repetidos. O caracter ' + str(re.findall(r"(\w)*.*\1", password))+ ' está repetido')
        status = False
    if len(re.findall(r"\s+", password)) > 0:
        message = str('Senha nao pode ter espacos')
        status = False

    return json.dumps({"status": status, "message": message})

app.run(host="0.0.0.0", port=80)
