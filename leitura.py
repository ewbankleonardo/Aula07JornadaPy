from typing import List
import csv

arq= 'vendas.csv'

def ler_csv(nome_do_arquivo:str) -> List[dict]:
    """
    le arquivo CSV e transforma em lista de dicionario  
    """
    lista = []
    try:
        with open(nome_do_arquivo,mode='r',encoding="UTF-8") as arquivo:
            vendas = csv.DictReader(arquivo)
            
            for linha in vendas:
                lista.append(linha)


    except FileNotFoundError as e:
        print(e)


    return lista


def filtrar_entregues(lista:list[dict]) -> list[dict]:

    """"
    Funcao que filtra entregas = True
    """
    lista_filtrados: list = []
    for produto in lista:
        if produto.get("entregue") == "True":

            lista_filtrados.append(produto)
    return lista_filtrados

def somar_valores_entregues(lista_filtrados:list[dict]) -> int:

    """"
    Funcao que soma o total da entrega
    """
    valor = 0
    for produto in lista_filtrados:
        valor += int(produto.get("preco"))

    return valor

lista_de_produtos = ler_csv(arq)
entregues = filtrar_entregues(lista_de_produtos)
print(entregues)
total = somar_valores_entregues(entregues)
print(f"Total {total}")