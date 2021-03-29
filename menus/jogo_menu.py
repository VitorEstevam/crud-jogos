from consolemenu import *
from consolemenu.items import *

from connections.jogoDAO import JogoDAO
from menus.jogo_update_menu import show_menu
# region methods


def update():
    id = input("insira a id do jogo que deseja modificar\n")
    nome = input("insira o nome do jogo\n")
    idade = input("insira a idade recomendada\n")
    tempo = input("insira o tempo do jogo\n")
    jogadoresmin = input("insira a quantidade minima de players\n")
    jogadoresmax = input("insira a quantidade maxima de players\n")
    tipo = input("insira a id do tipo de jogo\n")
    j = JogoDAO()
    jogo = j.update_on_db(id, idade, nome, tempo,
                          jogadoresmin, jogadoresmax, tipo)
    print(f"jogo de id: {jogo} atualizado")
    input("aperte qualquer tecla para sair\n")


def insert():
    nome = input("insira o nome do jogo\n")
    idade = input("insira a idade recomendada\n")
    tempo = input("insira o tempo do jogo\n")
    jogadoresmin = input("insira a quantidade minima de players\n")
    jogadoresmax = input("insira a quantidade maxima de players\n")
    tipo = input("insira a id do tipo de jogo\n")
    j = JogoDAO()
    jogo = j.insert_on_db(idade, nome, tempo, jogadoresmin, jogadoresmax, tipo)
    print(f"jogo de id: {jogo}")
    input("aperte qualquer tecla para sair\n")


def select():
    id = input("insira a id do jogo\n")
    j = JogoDAO()
    resp = j.select_from_db(id)
    print(resp)
    input("aperte qualquer tecla para sair\n")


def select_all():
    j = JogoDAO()
    resp = j.select_all_from_db()
    print(resp)
    input("aperte qualquer tecla para sair\n")


def delete():
    id = input("insira a id do jogo\n")
    j = JogoDAO()
    resp = j.remove_from_db(id)
    print(f"{resp}")
    input("aperte qualquer tecla para sair\n")
# endregion


jogo_menu = ConsoleMenu("JOGOS", "")
jogo_menu.append_item(FunctionItem("Inserir jogo", insert))
jogo_menu.append_item(FunctionItem("Ver jogo", select))
jogo_menu.append_item(FunctionItem("Ver todos os jogos", select_all))
jogo_menu.append_item(FunctionItem("Atualizar um jogo", update, ""))
jogo_menu.append_item(FunctionItem("Deletar um jogo", delete, ""))
jogo_menu.append_item(FunctionItem(
    "add ou remover categorias/designers/mecanicas", show_menu))
