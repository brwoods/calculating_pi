# purpose: learn python, use GIT, use Wingware
# date: 28-JUN-2020
# author: David Kopec - "Classic Computer Science Problems in Python" - Manning
def calculate_pi(n_terms: int) ->  float:
    numerator: float = 4.0  
    denominator: float = 1.0
    operation: float = 1.0
    pi: float = 0.0
    for _ in range(n_terms):
        pi += operation * (numerator / denominator)
        denominator += 2.0
        operation *= -1.0
    return pi

    