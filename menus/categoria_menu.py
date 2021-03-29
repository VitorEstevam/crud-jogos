from consolemenu import *
from consolemenu.items import *
from connections.categoriaDAO import CategoriaDAO


# region methods
def insert():
    desc = input("insira a descricao da categoria\n")
    c = CategoriaDAO()
    r = c.insert_on_db(desc)
    input(f"categoria de id: {r}")
    print("aperte qualquer tecla para sair\n")


def select():
    id = input("insira a id da categoria que você deseja visualizar\n")
    c = CategoriaDAO()
    r = c.select_from_db(id)
    input(f"{r}")
    print("aperte qualquer tecla para sair\n")


def select_all():
    # id = input("insira a id da categoria que você deseja\n")
    c = CategoriaDAO()
    r = c.select_all_from_db()
    input(f"{r}")
    print("aperte qualquer tecla para sair\n")


def update():
    c = CategoriaDAO()
    print(c.select_all_from_db())
    id = input("insira a id da categoria que você deseja modificar\n")
    desc = input("insira a descricao da categoria\n")
    r = c.update_on_db(id, desc)
    input(f"categoria de id{r} atualizada")
    print("aperte qualquer tecla para sair\n")


def delete():
    c = CategoriaDAO()
    print(c.select_all_from_db())
    id = input("insira a id da categoria que você deseja deletar\n")
    r = c.remove_from_db(id)
    input(f"{r}")
    print("aperte qualquer tecla para sair\n")
# endregion


categoria_menu = ConsoleMenu("CATEGORIAS", "Categorias dos jogos")
categoria_menu.append_item(FunctionItem("Inserir Categoria", insert))
categoria_menu.append_item(FunctionItem("Ver Categoria", select, ""))
categoria_menu.append_item(FunctionItem(
    "Ver todas as categorias", select_all, ""))
categoria_menu.append_item(FunctionItem("Editar uma categoria", update, ""))
categoria_menu.append_item(FunctionItem("Deletar uma categoria", delete, ""))
