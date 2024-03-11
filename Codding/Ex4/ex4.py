import math
from collections import Counter
from matplotlib import pyplot as plt


def calculate_entropy(probabilities, normalization_factor=1):
    # Calculate the entropy
    estimated_entropy = -sum((p * math.log2(p) for p in probabilities.values() if p != 0))
    return estimated_entropy / normalization_factor


def estimate_entropy_single_symbol(text: str):
    # Estimate the probability of each character based on its occurrence in the text
    estimated_character_probabilities = {key: val / len(text) for key, val in Counter(text).items()}
    return calculate_entropy(estimated_character_probabilities)


def estimate_entropy_pairs(text: str):
    # Notice we can ignore pairs that are not in the text since they will have probability of 0 which cancels out
    frequencies = Counter([text[i:i + 2] for i in range(len(text) - 1)])
    # Estimate the probability of each pair of characters based on their occurrence in the text
    estimated_pair_probabilities = {key: val / len(text) for key, val in frequencies.items()}
    return calculate_entropy(estimated_pair_probabilities, 2)


def estimate_average_entropy_conditioned(text: str):
    frequencies = Counter([text[i:i + 2] for i in range(len(text) - 1)])
    estimated_character_probabilities = {key: val / len(text) for key, val in Counter(text).items()}
    entropy = 0
    for y, p_y in estimated_character_probabilities.items():
        for x, p_x in estimated_character_probabilities.items():
            p = frequencies.get(x + y, 0) / len(text)
            if p_y != 0 and p != 0:
                entropy -= p * math.log2(p / p_y)
    return entropy


if __name__ == '__main__':
    with open('MOBY DICK.txt', 'r') as f:
        data = f.readlines()
        data = "".join(data)
        print(f"There are {len(data)} symbols in text")
    print(f"Estimated entropy per character based on letter occurrence: {estimate_entropy_single_symbol(data)}")
    print(f"Estimated entropy per character based on letter-pair occurrence: {estimate_entropy_pairs(data)}")
    print(f"Estimated entropy per character based on conditioned letter occurrence: "
          f"{estimate_average_entropy_conditioned(data)}")
