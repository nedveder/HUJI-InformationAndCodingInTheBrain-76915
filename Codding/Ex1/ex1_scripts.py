# Set up the data
conditional = {'Interesting': [.8, .5, .1], 'Boring': [.2, .5, .9]}
cost = {'Attending': [0, 7, 10], 'Not Attending': [20, 5, 0]}
states = {'Good': 0, 'Mediocre': 1, 'Bad': 2}
actions = ['Attending', 'Not Attending']
possible_observations = ['Interesting', 'Boring']

# Define all possible strategies
strategies = [{'Interesting': 'Attending', 'Boring': 'Attending'},
              {'Interesting': 'Attending', 'Boring': 'Not Attending'},
              {'Interesting': 'Not Attending', 'Boring': 'Attending'},
              {'Interesting': 'Not Attending', 'Boring': 'Not Attending'}]


def calculate_state_conditional_risk(strategy):
    risk = [0] * len(states)
    for w in states.values():
        for x in possible_observations:
            risk[w] += conditional[x][w] * cost[strategy[x]][w]
    return max(risk)


if __name__ == '__main__':
    for s in strategies:
        print(s, calculate_state_conditional_risk(s))
    print(f"The minmax strategy is: {min(strategies, key=calculate_state_conditional_risk)}")

"""
########################### Output ###########################
{'Interesting': 'Attending', 'Boring': 'Not Attending'}
"""
