import string
import random
import requests
import os
import numpy as np
import re


def get_mapping():
    char_set = list(string.ascii_lowercase)
    shuffled_char_set = char_set.copy()
    random.shuffle(shuffled_char_set)

    true_mapping = {}
    for key, value in zip(char_set, shuffled_char_set):
        true_mapping[key] = value


# initialize Markov matrix
M = np.ones((26, 26))

# initial state distribution
pi = np.zeros(26)


def get_ch_indx(ch):
    """ Returns the index of character """
    return ord(ch) - 97


def update_pi(ch):
    """ Update initial state distribution """
    i = get_ch_indx(ch)
    pi[i] += 1


def update_transisition(ch0, ch1):
    """ Update Markov matrix """
    i = get_ch_indx(ch0)
    j = get_ch_indx(ch1)
    M[i, j] += 1


def get_word_probability(word):
    """ Returns the probability of a word """
    i = get_ch_indx(word[0])
    logp = np.log(pi(i))

    for ch in word[1:]:
        logp += np.log(M(i, j))
        i = j

    return logp


def get_sequence_probability(words):
    logp = list(map(lambda word: get_word_probability(word), words)).sum()
    return logp


def download_file():
    # create a markov model based on an English dataset
    # is an edit of https://www.gutenberg.org/ebooks/2701
    # (I removed the front and back matter)

    # download the file
    if not os.path.exists('moby_dick.txt'):
        print("Downloading moby dick...")
        r = requests.get(
            'https://lazyprogrammer.me/course_files/moby_dick.txt')
        with open('moby_dick.txt', 'w', encoding="utf-8") as f:
            f.write(r.content.decode())


def main():
    download_file()

    # for replacing non-alpha characters
    regex = re.compile('[^a-zA-Z]')

    # load in words
    for i, line in enumerate(open('moby_dick.txt', encoding="utf-8")):
        line = line.strip()  # Strip spaces around
        if line:
            # replace all non-alpha characters with space
            line = regex.sub(' ', line)

            for token in line.lower().split():
                # First letter, add to pi
                ch0 = token[0]
                update_pi(ch0)
                # Update Transision probabilites
                for ch1 in token[1:]:
                    update_transisition(ch0, ch1)
                    ch0 = ch1


if __name__ == "__main__":
    main()
    # normalize the probabilities
    pi /= pi.sum()
    M /= M.sum(axis=1, keepdims=True)
    print(pi)
    print(M)
