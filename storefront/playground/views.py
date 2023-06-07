# Create your views here.
from django.shortcuts import render
from .utils import calcular_combinaciones, factorial_paralelo, calcular_factorial_secuencial, generate_deck, generate_combinations
import random
import timeit

def card_combinations_view(request):
    if request.method == "POST":
        total_cards = int(request.POST.get('total_cards'))
        combinatoria = int(request.POST.get('combinatoria'))

        deck = generate_deck()
        selected_cards = random.sample(deck, total_cards)

        seq_start_time = timeit.default_timer()
        seq_combinations = calcular_combinaciones(len(selected_cards), combinatoria)
        seq_end_time = timeit.default_timer()
        seq_time = seq_end_time - seq_start_time

        par_start_time = timeit.default_timer()
        par_combinations = calcular_combinaciones(len(selected_cards), combinatoria, parallel=True)
        par_end_time = timeit.default_timer()
        par_time = par_end_time - par_start_time

        possible_combinations = generate_combinations(selected_cards, combinatoria)

        context = {
            'selected_cards': selected_cards,
            'seq_combinations': seq_combinations,
            'seq_time': seq_time,
            'par_combinations': par_combinations,
            'par_time': par_time,
            'possible_combinations': possible_combinations,
        }

        return render(request, 'combinations/result.html', context)

    return render(request, 'combinations/input.html')
