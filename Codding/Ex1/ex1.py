def get_dists():
    with open('english_dist.txt', 'r') as file:
        english_dist = [s.lower().strip('\n').split('\t') for s in file.readlines()]
    with open('french_dist.txt', 'r') as file:
        french_dist = [s.lower().strip('\n').split('\t') for s in file.readlines()]
    return english_dist, french_dist
