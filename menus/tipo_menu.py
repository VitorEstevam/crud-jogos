from consolemenu import *
from consolemenu.items import *
from connections.tipoDAO import TipoDAO


# region methods
def insert():
    desc = input("insira a descricao da tipo\n")
    c = TipoDAO()
    r = c.insert_on_db(desc)
    input(f"tipo de id: {r}")
    print("aperte qualquer tecla para sair\n")


def select():
    id = input("insira a id do tipo que você deseja visualizar\n")
    c = TipoDAO()
    r = c.select_from_db(id)
    input(f"{r}")
    print("aperte qualquer tecla para sair\n")


def select_all():
    # id = input("insira a id da tipo que você deseja\n")
    c = TipoDAO()
    r = c.select_all_from_db()
    input(f"{r}")
    print("aperte qualquer tecla para sair\n")


def update():
    id = input("insira a id do tipo que você deseja modificar\n")
    desc = input("insira a descricao da tipo\n")
    c = TipoDAO()
    r = c.update_on_db(id, desc)
    input(f"tipo de id:{r} atualizado")
    print("aperte qualquer tecla para sair\n")


def delete():
    id = input("insira a id do tipo que você deseja deletar\n")
    c = TipoDAO()
    r = c.remove_from_db(id)
    input(f"{r}")
    print("aperte qualquer tecla para sair\n")
# endregion


tipo_menu = ConsoleMenu("TIPOS", "Tipos dos jogos")
tipo_menu.append_item(FunctionItem("Inserir Tipo", insert))
tipo_menu.append_item(FunctionItem("Ver Tipo", select, ""))
tipo_menu.append_item(FunctionItem(
    "Ver todos os tipos", select_all, ""))
tipo_menu.append_item(FunctionItem("Editar um tipo", update, ""))
tipo_menu.append_item(FunctionItem("Deletar um tipo", delete, ""))
