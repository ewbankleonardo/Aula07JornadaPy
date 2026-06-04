from leitura import ler_csv,filtrar_entregues,somar_valores_entregues
arq = 'vendas.csv'
lista_de_produtos = ler_csv(arq)
entregues = filtrar_entregues(lista_de_produtos)
print(entregues)
total = somar_valores_entregues(entregues)
print(f"Total {total}")