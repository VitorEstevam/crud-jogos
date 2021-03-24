from consolemenu import *
from consolemenu.items import *

from menus.categoria_menu import *
from menus.tipo_menu import *
from menus.designer_menu import *
from menus.mecanica_menu import *

# from categorias_menu import categorias_menu

main_menu = ConsoleMenu("CRUD JOGOS", "boardgames bom demais")
main_menu.append_item(FunctionItem("Jogos", print, ""))
main_menu.append_item(FunctionItem("Categorias", categoria_menu.show))
main_menu.append_item(FunctionItem("Designers", designer_menu.show))
main_menu.append_item(FunctionItem("Tipo de jogo", tipo_menu.show))
main_menu.append_item(FunctionItem("Mecanicas", mecanica_menu.show))
