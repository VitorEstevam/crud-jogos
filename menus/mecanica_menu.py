from consolemenu import *
from consolemenu.items import *
from connections.mecanicaDAO import MecanicaDAO


# region methods
def insert():
    desc = input("insira a descricao da mecanica\n")
    c = MecanicaDAO()
    r = c.insert_on_db(desc)
    input(f"mecanica de id: {r}")
    print("aperte qualquer tecla para sair\n")


def select():
    id = input("insira a id da mecanica que você deseja visualizar\n")
    c = MecanicaDAO()
    r = c.select_from_db(id)
    input(f"{r}")
    print("aperte qualquer tecla para sair\n")


def select_all():
    # id = input("insira a id da mecanica que você deseja\n")
    c = MecanicaDAO()
    r = c.select_all_from_db()
    input(f"{r}")
    print("aperte qualquer tecla para sair\n")


def update():
    id = input("insira a id da mecanica que você deseja modificar\n")
    desc = input("insira a descricao da mecanica\n")
    c = MecanicaDAO()
    r = c.update_on_db(id, desc)
    input(f"mecanica de id{r} atualizada")
    print("aperte qualquer tecla para sair\n")


def delete():
    id = input("insira a id da mecanica que você deseja deletar\n")
    c = MecanicaDAO()
    r = c.remove_from_db(id)
    input(f"{r}")
    print("aperte qualquer tecla para sair\n")
# endregion


mecanica_menu = ConsoleMenu("MECANICAS", "Mecanicas dos jogos")
mecanica_menu.append_item(FunctionItem("Inserir Mecanica", insert))
mecanica_menu.append_item(FunctionItem("Ver Mecanica", select, ""))
mecanica_menu.append_item(FunctionItem(
    "Ver todas as mecanicas", select_all, ""))
mecanica_menu.append_item(FunctionItem("Editar uma mecanica", update, ""))
mecanica_menu.append_item(FunctionItem("Deletar uma mecanica", delete, ""))
