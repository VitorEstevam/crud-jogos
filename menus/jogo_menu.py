from consolemenu import *
from consolemenu.items import *

from connections.jogoDAO import JogoDAO
# region methods


def insert():
    nome = input("insira o nome do jogo\n")
    idade = input("insira a idade recomendada\n")
    tempo = input("insira o tempo do jogo\n")
    jogadoresmin = input("insira a quantidade minima de players\n")
    jogadoresmax = input("insira a quantidade maxima de players\n")
    tipo = input("insira a id do tipo de jogo\n")
    j = JogoDAO()
    jogo = j.insert_on_db(idade, nome, tempo, jogadoresmin, jogadoresmax, tipo)
    input(f"jogo de id: {jogo}")
    print("aperte qualquer tecla para sair\n")


def delete():
    id = input("insira a id do jogo\n")
    j = JogoDAO()
    resp = j.remove_from_db(id)
    input(f"{resp}")
    print("aperte qualquer tecla para sair\n")
# endregion


jogo_menu = ConsoleMenu("JOGOS", "")
jogo_menu.append_item(FunctionItem("Inserir jogo", insert))
jogo_menu.append_item(FunctionItem("Ver jogo", print, ""))
jogo_menu.append_item(FunctionItem("Ver todos os jogos", print, ""))
jogo_menu.append_item(FunctionItem("Editar um jogo", print, ""))
jogo_menu.append_item(FunctionItem("Deletar um jogo", delete, ""))
