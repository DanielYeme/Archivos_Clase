import pandas as pd
import pulp
from pulp import LpMaximize, LpProblem, LpVariable, lpSum

# Cargar el archivo CSV en un DataFrame
df = pd.read_csv("mochila_almno_.csv")

# Función para convertir listas en formato de cadena a listas de enteros
def parse_list(string):
    return list(map(int, string.strip("[]").replace(',', '').split()))

# Procesar cada fila del archivo
solutions = []
for _, row in df.iterrows():
    problem_id = row['Id problem']
    weights = parse_list(row['Weights'])
    prices = parse_list(row['Prices'])
    capacity = int(row['Capacity'])  # Asegurar que la capacidad es un entero
    num_items = len(weights)
    
    # Definir el problema de optimización
    model = LpProblem(name=f"knapsack_{problem_id}", sense=LpMaximize)
    
    # Definir variables binarias para seleccionar ítems
    x = [LpVariable(name=f"x{i}", cat='Binary') for i in range(num_items)]
    
    # Función objetivo: maximizar el valor total de los ítems seleccionados
    model += lpSum(prices[i] * x[i] for i in range(num_items)), "Objective"
    
    # Restricción de capacidad de la mochila
    model += lpSum(weights[i] * x[i] for i in range(num_items)) <= capacity, "Capacity_Constraint"
    
    # Resolver el problema
    model.solve()
    
    # Obtener la solución óptima
    best_picks = [int(pulp.value(x[i])) for i in range(num_items)]
    best_price = sum(prices[i] * best_picks[i] for i in range(num_items))
    avg_weight = sum(weights) / num_items if num_items > 0 else 0
    avg_price = sum(prices) / num_items if num_items > 0 else 0
    cost_function = f"maximize {' + '.join(f'{prices[i]}x{i}' for i in range(num_items))}"
    constraint = f"{' + '.join(f'{weights[i]}x{i}' for i in range(num_items))} <= {capacity}"
    
    # Guardar los resultados en una lista
    solutions.append([best_picks, best_price, avg_weight, avg_price, cost_function, constraint])

# Convertir soluciones en un DataFrame y asignarlas a df
df_results = pd.DataFrame(solutions, columns=['Best picks', 'Best price', 'Average Weights', 'Average Prices', 'Cost function', 'Constraint'])
df = pd.concat([df, df_results], axis=1)

# Guardar el archivo de salida
df.to_csv("mochila_resultado.csv", index=False)

print("Optimización completada. Archivo guardado como mochila_resultado.csv")
