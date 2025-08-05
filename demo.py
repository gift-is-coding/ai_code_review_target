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

    # Print a random integer between 1 and 100
    print("Random integer between 1 and 100:", random.randint(1, 100))

    # Print a random floating point number between 0 and 1
    print("Random float between 0 and 1:", random.random())

    # Print a random sample of 3 elements from a list
    sample_list = ['apple', 'banana', 'cherry', 'date', 'elderberry']
    print("Random sample of 3 fruits:", random.sample(sample_list, 3))

    # Shuffle the sample_list and print the result
    random.shuffle(sample_list)
    print("Shuffled list of fruits:", sample_list)