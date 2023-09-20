# # Steps:
# 1. Build a list of n-grams from the corpus.
# 2. Build a dict with the keys being those n-grams and the values being all the words after that.
# 3. Check the last and last - n words from the given sentence in the parameter.
# 4. Try to match it with the n-grams in our n-gram dict
# 5. Return the most frequent occuring word
# 6. For random, create a dict with the word in corpus and the associated probability. Then use the weighted prob to keep appending until the while loop runs

################ Instructions for deterministic vs the randomized?#############################
# If the input flag randomize is false, choose at each step the single most probable next token. When two
# tokens are equally probable, choose the one that occurs first in the corpus. This is called a deterministic
# process. If randomize is true, draw the next word randomly from the appropriate distribution.

import nltk
import random
from collections import Counter

print("text being generated")  # To show in the output that the program has started


# just using to create the large corpus from nltk for training the model and testing (took it from Prof Wang's code.)
def test_generator():
    """Test Markov text generator."""
    corpus = nltk.word_tokenize(nltk.corpus.gutenberg.raw("austen-sense.txt").lower())
    return corpus


############### HELPER FUNCTIONS #################
# for the n-gram (selects the last n words of a sentence to be used as the n-gram)
def get_last_n_words(sentence, n):
    # words = sentence.lower().split(" ")
    return sentence[-n:]


# generates the n-grams (using tuples instead of lists because it's better than lists for the fact that they need less memory allocation because of being immutable)
def generate_n_grams(vocab, n):
    n_grams = [tuple(vocab[i : i + n]) for i in range(len(vocab) - n + 1)]
    return n_grams
    # pass


# creates a dictionary with the keys being the n-grams and the values being the next words after those n-grams in the corpus
def make_model(vocab, n_grams, n):
    model = {}
    for i in range(0, len(n_grams) - 1):
        if n_grams[i] not in model:
            model[n_grams[i]] = []
        # if n < 1:
        #     # model[n_grams[i]].append(n_grams[i + 1])
        #     return get_most_common_word(vocab)
        # else:
        model[n_grams[i]].append(n_grams[i + 1][n - 1])
    return model
    # pass


# takes a list and returns the most common word, or
def get_most_common_word(words):
    word_counts = {}
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    most_common_word = max(word_counts, key=word_counts.get)
    word_counts.pop(most_common_word)
    return most_common_word


# takes all the words in a dict and creates a dictionary with the word in the corpus and the associated probability of that word which will be used for weighted randomness.
def weights(corpus):
    freq = Counter(corpus)

    total = len(corpus)

    probabilities = {item: count / total for item, count in freq.items()}

    return probabilities


# Selects a token based on the weight. Tokens with higher frequency will be selected more often.
def random_weight(word_weights):
    words, weights = list(word_weights.keys()), list(word_weights.values())
    selected_word = random.choices(words, weights=weights, k=1)[0]
    return selected_word


# final function :) ### MAIN ONE REQUIRED FOR ASSIGNMENT (CALLS ALL OTHER FUNCTIONS) ####
def finish_sentence(sentence, n, corpus, randomize):
    ogn = n  # storing the OG value of n
    while (
        len(sentence) < 10
        and sentence[-1] != "?"
        and sentence[-1] != "."
        and sentence[-1] != "!"
    ):
        # print(ogn) just checking smth u can ignore
        if n > len(sentence) + 1:
            n = len(sentence) + 1
        # for stochastic
        if randomize == True:
            if n == 1:  # if n =1, i.e unigram -> you just append the most common word
                sentence.append(random_weight(weights(corpus)))
                n = ogn
            else:
                words = get_last_n_words(sentence, n - 1)
                words = tuple(words)
                n_grams = generate_n_grams(corpus, n - 1)
                model = make_model(corpus, n_grams, n - 1)
                if words in model:
                    # next_word = get_most_common_word(model[words])
                    sentence.append(random_weight(weights(model[words])))
                    # sentence.append(next_word)
                    n = ogn  # returning to the old n for next
                else:
                    n = n - 1
        # deterministic - but first have to check for unigram
        else:
            if n == 1:  # if n =1, i.e unigram -> you just append the most common word
                sentence.append(get_most_common_word(corpus))
                n = ogn
            else:
                words = get_last_n_words(sentence, n - 1)
                words = tuple(words)
                n_grams = generate_n_grams(corpus, n - 1)
                model = make_model(corpus, n_grams, n - 1)
                if words in model:
                    next_word = get_most_common_word(model[words])
                    sentence.append(next_word)
                    # print("deter")
                    n = ogn
                else:
                    ##### stupid backoff
                    n = n - 1
                    # finish_sentence(sentence, n, corpus, randomize)
    return sentence


############ MAIN (only using it for testing it for myself) ################
sentence = ["robot"]
corpus = test_generator()
n = 3
x = finish_sentence(sentence, n, corpus, True)
print(x)

# print("text generation finished")
# # check for bug for n = 1
