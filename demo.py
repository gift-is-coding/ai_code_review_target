import random

def print_random_fact():
    facts = [
        "Honey never spoils.",
        "Bananas are berries, but strawberries aren't.",
        "A group of flamingos is called a 'flamboyance'.",
        "Octopuses have three hearts.",
        "The Eiffel Tower can be 15 cm taller during hot days."
    ]
    print(random.choice(facts))

if __name__ == "__main__":
    print_random_fact()