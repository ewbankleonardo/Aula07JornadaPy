def somando (a:float = 10, b:float = 10) -> float:
    return a+b

valor3=(somando(a=20))

print(valor3)

#Calcular Média de Valores em uma Lista

from typing import List

def media_lista(valores:List) -> float:
    return sum(valores)/len(valores)

lista = [2,2,2,3,5]

print(media_lista(lista))


#Filtrar Dados Acima de um Limite
def filtro (valores: List, limite:float)->List[float]:
    res =[valor for valor in valores if valor>limite]
    #for valor in valores:
    #    if valor<limite:
    #        res.append(valor)
    
    return res
print (filtro(lista,2))
    
#Contar Valores Únicos em uma Lista

def unicos(valores:List[float])->int:
    return len(set(valores))
#A set in Python is an unordered collection of unique elements. 
# Sets are mutable, meaning you can add 
# or remove elements after their creation, but the individual elements must be immutable.
print(unicos(lista))

#Converter Celsius para Fahrenheit em uma Lista

def convert(fahrenheit:List[float])-> List[float]:
    convertido:list[float] = [(lambda f: ((f-32)*5/9))(temp)for temp in fahrenheit]
    return convertido

#(lambda f: ((f - 32) * 5 / 9))(temp)
#This is an inline anonymous function (lambda) that:
#Takes one argument f (a Fahrenheit temperature).
#Applies the formula to convert Fahrenheit to Celsius: [ C = (F - 32) \times \frac{5}{9} ]
#Immediately after defining the lambda, it is called with (temp)

fah=[10,20,30]
celsius = convert(fah)
print(celsius)

#Calcular Desvio Padrão de uma Lista
def calcular_desvio_padrao(valores: List[float]) -> float:
    media = sum(valores)/len(valores)
    variancia = sum((x-media)**2 for x in valores)/len(valores)
    return variancia ** 0.5

#Encontrar Valores Ausentes em uma Sequência
def encontrar_valores_ausentes(sequencia: List[int]) -> List[int]:
    completo = set(range(min(sequencia), max(sequencia) + 1))
    return list(completo - set(sequencia))

listinha=[1,4,5,6]
print("ausentes")
print(min(listinha))
print(max(listinha)+1)
completo = set(range(min(listinha), max(listinha) + 1))
print(completo)
aus = encontrar_valores_ausentes(listinha)
print()
print(aus)


