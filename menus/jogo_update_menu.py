from consolemenu import *
from consolemenu.items import *

from connections.jogoDAO import JogoDAO

# region methods
id_jogo = 23


def add_mecanica():
    id_mecanica = input("insira a id do da mecanica que deseja inserir\n")
    j = JogoDAO()
    resp = j.add_mecanica(id_jogo, id_mecanica)
    print(resp)
    input("aperte qualquer tecla para sair\n")


def remove_mecanica():
    j = JogoDAO()
    print(j.sel_mecanica_with_id(id_jogo))
    id_mecanica = input("insira a id do da mecanica que deseja remover\n")
    resp = j.remove_mecanica(id_jogo, id_mecanica)
    print(resp)
    input("aperte qualquer tecla para sair\n")


def add_designer():
    id_designer = input("insira a id do designer que deseja inserir\n")
    j = JogoDAO()
    resp = j.add_designer(id_jogo, id_designer)
    print(resp)
    input("aperte qualquer tecla para sair\n")


def remove_designer():
    j = JogoDAO()
    print(j.sel_designer_with_id(id_jogo))
    id_designer = input("insira a id do designer que deseja remover\n")
    resp = j.remove_designer(id_jogo, id_designer)
    print(resp)
    input("aperte qualquer tecla para sair\n")


def add_categoria():
    id_categoria = input("insira a id do da categoria que deseja inserir")
    j = JogoDAO()
    resp = j.add_categoria(id_jogo, id_categoria)
    print(resp)
    input("aperte qualquer tecla para sair\n")


def remove_categoria():
    j = JogoDAO()
    print(j.sel_categoria_with_id(id_jogo))
    id_categoria = input("insira a id do da categoria que deseja remover")
    resp = j.remove_categoria(id_jogo, id_categoria)
    print(resp)
    input("aperte qualquer tecla para sair\n")
# endregion


jogo_update_menu = ConsoleMenu("Atualizar jogo", "")
jogo_update_menu.append_item(FunctionItem("Adicionar mecanica", add_mecanica))
jogo_update_menu.append_item(FunctionItem("Remover mecanica", remove_mecanica))
jogo_update_menu.append_item(FunctionItem("Adicionar designer", add_designer))
jogo_update_menu.append_item(FunctionItem("Remover designer", remove_designer))
jogo_update_menu.append_item(FunctionItem(
    "Adicionar categoria", add_categoria))
jogo_update_menu.append_item(FunctionItem(
    "Remover categoria", remove_categoria))


def show_menu():
    global id_jogo
    id_jogo = input("insira a id do jogo que deseja modificar\n")
    jogo_update_menu.show()
