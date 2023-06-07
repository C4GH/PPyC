import random
import time
import concurrent.futures
import math
from itertools import combinations

def generate_deck():
    values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    suits = ['♠', '♥', '♦', '♣']  # Picas, Corazones, Diamantes, Tréboles
    deck = [f'{value}{suit}' for value in values for suit in suits]
    return deck

def calcular_factorial_secuencial(n): #Calcula el factorial
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

def factorial_paralelo(n, threshold=500):
    if n <= threshold:
        resultado = math.factorial(n)
    else:
        with concurrent.futures.ProcessPoolExecutor() as executor:  # aquí se define la cantidad de procesos
            futuro1 = executor.submit(factorial_paralelo, n // 2) #definimos futuros
            futuro2 = executor.submit(factorial_paralelo, n - n // 2)
            resultado = futuro1.result() * futuro2.result() #el resultado se obtiene de multiplicar los futuros
    return resultado

def calcular_combinaciones(n, r, parallel=False):
    if parallel:
        return factorial_paralelo(n) / (factorial_paralelo(r) * factorial_paralelo(n - r))
    else:
        return calcular_factorial_secuencial(n) / (calcular_factorial_secuencial(r) * calcular_factorial_secuencial(n - r))

def generate_combinations(cards, r):
    return list(combinations(cards, r))

def main():
    deck = generate_deck()

    total_cards = int(input("Ingrese el total de cartas para seleccionar (menor o igual a 52): "))
    combinatoria = int(input("Ingrese el número de cartas para combinar (menor o igual al total de cartas seleccionadas): "))

    selected_cards = random.sample(deck, total_cards)
    
    print(f"\nCartas seleccionadas: {selected_cards}")
    
    # Sequential calculation of combinations
    seq_start_time = time.time()
    seq_combinations = calcular_combinaciones(len(selected_cards), combinatoria)
    seq_end_time = time.time()
    print(f"\nTiempo de cálculo secuencial: {seq_end_time - seq_start_time} segundos.")
    print(f"Número de combinaciones (Secuencial): {seq_combinations}")
    
    # Parallel calculation of combinations
    par_start_time = time.time()
    par_combinations = calcular_combinaciones(len(selected_cards), combinatoria, parallel=True)
    par_end_time = time.time()
    print(f"\nTiempo de cálculo paralelo: {par_end_time - par_start_time} segundos.")
    print(f"Número de combinaciones (Paralelo): {par_combinations}")

    # Generate all possible combinations of the selected cards
    possible_combinations = generate_combinations(selected_cards, combinatoria)
    print(f"\nCombinaciones posibles: {possible_combinations}")

if __name__ == "__main__":
    main()