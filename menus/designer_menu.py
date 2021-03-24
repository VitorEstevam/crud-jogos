from consolemenu import *
from consolemenu.items import *
from connections.designerDAO import DesignerDAO


# region methods
def insert():
    desc = input("insira a descricao da designer\n")
    c = DesignerDAO()
    r = c.insert_on_db(desc)
    input(f"designer de id: {r}")
    print("aperte qualquer tecla para sair\n")


def select():
    id = input("insira a id do designer que você deseja visualizar\n")
    c = DesignerDAO()
    r = c.select_from_db(id)
    input(f"{r}")
    print("aperte qualquer tecla para sair\n")


def select_all():
    # id = input("insira a id da designer que você deseja\n")
    c = DesignerDAO()
    r = c.select_all_from_db()
    input(f"{r}")
    print("aperte qualquer tecla para sair\n")


def update():
    id = input("insira a id do designer que você deseja modificar\n")
    desc = input("insira a descricao da designer\n")
    c = DesignerDAO()
    r = c.update_on_db(id, desc)
    input(f"designer de id:{r} atualizado")
    print("aperte qualquer tecla para sair\n")


def delete():
    id = input("insira a id do designer que você deseja deletar\n")
    c = DesignerDAO()
    r = c.remove_from_db(id)
    input(f"{r}")
    print("aperte qualquer tecla para sair\n")
# endregion


designer_menu = ConsoleMenu("DESIGNERS", "Designers dos jogos")
designer_menu.append_item(FunctionItem("Inserir Designer", insert))
designer_menu.append_item(FunctionItem("Ver Designer", select, ""))
designer_menu.append_item(FunctionItem(
    "Ver todos os designers", select_all, ""))
designer_menu.append_item(FunctionItem("Editar um designer", update, ""))
designer_menu.append_item(FunctionItem("Deletar um designer", delete, ""))
