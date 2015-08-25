import random

def choose_from_histogram(a_hist):
    choice_list = []
    for k in a_hist:
        for num in range(a_hist[k]):
            choice_list += k

    random_choice = random.choice(choice_list)
    return random_choice
