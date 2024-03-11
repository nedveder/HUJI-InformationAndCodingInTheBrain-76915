import numpy as np
import matplotlib.pyplot as plt


def get_letter_distributions():
    with open('english_dist.txt', 'r') as f:
        english_dist = [s.lower().strip('\n').split('\t') for s in f.readlines()]
        english_dist = {i[0]: float(i[1]) for i in english_dist}
        english_dist[' '] = english_dist.pop('space ')
    with open('french_dist.txt', 'r') as f:
        french_dist = [s.lower().strip('\n').split('\t') for s in f.readlines()]
        french_dist = {i[0]: float(i[1]) for i in french_dist}
        french_dist[' '] = french_dist.pop('space ')
    return english_dist, french_dist


def sample_n_words(n, selected_text):
    """
    Sample N letters randomly from the text
    """
    # sample N letters from the text
    english_dist, french_dist = get_letter_distributions()
    english_posterior_prob, french_posterior_prob = P_ENGLISH_WORLD, P_FRENCH_WORLD
    english_posterior, french_posterior = [P_ENGLISH_WORLD], [P_FRENCH_WORLD]
    llh = [0]

    for i in range(n):
        letter = "-"
        while letter not in "abcdefghijklmnopqrstuvwxyz ":
            letter = selected_text[np.random.randint(0, len(selected_text))]


        # Update the posterior probability
        english_posterior_prob *= english_dist[letter]
        french_posterior_prob *= french_dist[letter]

        # Normalize the posterior probability
        total = english_posterior_prob + french_posterior_prob
        english_posterior_prob /= total
        french_posterior_prob /= total

        english_posterior.append(english_posterior_prob)
        french_posterior.append(french_posterior_prob)

        # Update the log-likelihood
        llh.append(llh[-1] + np.log(english_dist[letter] / french_dist[letter]))

    return english_posterior, french_posterior, llh


# DEFINE THE CONSTANTS
N = 100
P_ENGLISH_WORLD = 0.7
P_FRENCH_WORLD = 0.3


def plot_posteriors(ax, english_ps, french_ps, text_type='English'):
    ax.plot(english_ps, label='English')
    ax.plot(french_ps, label='French')
    ax.set_title(f'{text_type} Text')
    ax.set_xlabel('Number of letters')
    ax.set_ylabel('Posterior Probability')
    ax.legend()


if __name__ == '__main__':
    np.random.seed(0)
    texts = ['English text', 'French text']
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 5))
    log_likelihoods = []
    with open("english_text.txt", 'r') as file:
        text = file.read().replace('\n', '').lower()
        english_posteriors, french_posteriors, log_likelihood = sample_n_words(N, text)
        log_likelihoods.append(log_likelihood)

    plot_posteriors(ax1, english_posteriors, french_posteriors, text_type='English')

    with open("french_text.txt", 'r', encoding='ISO-8859-1') as file:
        text = file.read().replace('\n', '').lower()
        english_posteriors, french_posteriors, log_likelihood = sample_n_words(N, text)
        log_likelihoods.append(log_likelihood)

    plot_posteriors(ax2, english_posteriors, french_posteriors, text_type='French')
    # Plot the log-likelihood for each text
    plt.figure()
    # Plot the log-likelihood for each text in Log scale
    plt.plot(log_likelihoods[0], label='English')
    plt.plot(log_likelihoods[1], label='French')
    plt.title(r'Log-Likelihood of the two texts')
    plt.xlabel('Number of letters (N)')
    plt.ylabel(r'Log-Likelihood $\log\left(\frac{P(English)}{P(French)}\right)$')
    plt.legend()
    plt.show()
