# Daniel Yeme Morfin, David Lara Medina,Santiago Vazquez Ortega

import pandas as pd
from pulp import LpMaximize, LpProblem, LpVariable, lpSum

# --------------------------------------------------------------------------------------------------
file_path = "C:\SIM-MAT_2025\Archivos_Clase\Actividad 2.4\mochila_almno_.csv"       # Seccion encargada de leer el archivo csv
df = pd.read_csv(file_path)

#---------------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------------
def parse_list(string):                                   # Seccion que convierte listas de textos en enteros.
    return list(map(int, string.strip('[]').split()))
#----------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------
solutions = []
for _, row in df.iterrows():
    problem_id = row['Id problem']
    weights = parse_list(row['Weights'])                  # Seccion de iteraciones, analiza el archivo CSV y comienza el bucle
    prices = parse_list(row['Prices'])
    capacity = row['Capacity']
    n_item = len(weights)
#--------------------------------------------------------------------------------------------------------------------
    #---- Definir el problema de optimización------------------------------------------------------------------------
    problema = LpProblem(name=f"knapsack_{problem_id}", sense=LpMaximize)
    
    # Definir variables binarias --------------------------------------------------------------------------------------
    x = [LpVariable(name=f"x{i}", cat='Binary') for i in range(n_item)]   # 1 Significa que fue seleccionado, 0 que no
    #-----------------------------------------------------------------------------------------------------------------
    # Función objetivo: maximizar el valor total de los ítems seleccionados
    problema += lpSum(prices[i] * x[i] for i in range(n_item)), "Objective"
    
    # Restricciones
    problema += lpSum(weights[i] * x[i] for i in range(n_item)) <= capacity, "Capacity_Constraint"
    
    # Resolucion
    problema.solve()
    
    # Obtener la solución óptima--------------------------------------------------------------------------------------------
    best_picks = [int(x[i].value()) for i in range(n_item)]
    best_price = sum(prices[i] * best_picks[i] for i in range(n_item))
    avg_weight = sum(weights) / n_item
    avg_price = sum(prices) / n_item
    cost_function = f"maximize {' + '.join(f'{prices[i]}x{i}' for i in range(n_item))}"
    constraint = f"{' + '.join(f'{weights[i]}x{i}' for i in range(n_item))} <= {capacity}"
    
    # resultados------------------------------------------------------------------------------------------------------
    solutions.append([
    str(best_picks),                         # Se utilizo este formato para evitar problemas de forma
    best_price,
    avg_weight,
    avg_price,
    cost_function,
    constraint
])
#------------------------------------------------------------------------------------------------------------------------
# Agregar los resultados al DataFrame
df[['Best picks', 'Best price', 'Average Weights', 'Average Prices', 'Cost function', 'Constraint']] = solutions

# Guardar el archivo de salida
df.to_csv("mochila_resultado.csv", index=False)

print("Finalizado. Archivo guardado como mochila_resultado.csv")
