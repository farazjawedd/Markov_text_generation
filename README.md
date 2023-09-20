# Generating text using markov text generation to complete a sentence

A program for markov text generation using n-grams. 

The main function is called

```
finish_sentence(sentence, n, corpus, randomize=False)
```

and it is in the ``` mtg.py file ```. The ``` test_mtg.py ``` file is for testing.

It takes the following parameters:

1. sentence -> The (incomplete) sentence (already tokenized and in a list)
2. n -> what n to use for n-gram (2 or 3 or 4 etc)
3. corpus -> The word bank (for vocab) - already tokenized and in a list
4. randomize -> False by default. This is for rendering the output based on a deterministic or stochastic case.

The sentence generation stops when the sentence length reaches 10 words, or if there is one of the following characters: ``` "?", ".", "!" ```.

The corpus is obtained using the nltk library (this is optional, any corpus can be used). This function can be used after importing ```nltk```:

```
def test_generator():
    """Test Markov text generator."""
    corpus = nltk.word_tokenize(nltk.corpus.gutenberg.raw("austen-sense.txt").lower())
    return corpus

```



Some sample inputs and outputs using the corpus shown above:

## Deterministic Model 

Input # 1:
```
sentence = ['robot']
n = 3
corpus = corpus
randomize = False

```
Output # 1:
```
['robot', ',', 'and', 'the', 'two', 'miss', 'steeles', ',', 'as', 'she']
```

-----------
Input # 2:
```
sentence = ['she', 'was', 'not']
n = 1
corpus = corpus
randomize = False

```
Output # 2:
```
['she', 'was', 'not', ',', ',', ',', ',', ',', ',', ',']
```
----------
Input # 3:
```
sentence = ['robot']
n = 2
corpus = corpus
randomize = False

```
Output # 3:
```
['robot', ',', 'and', 'the', 'same', 'time', ',', 'and', 'the', 'same']
```
----------
Input # 4:
```
sentence = ['she', 'was', 'not']
n = 3
corpus = corpus
randomize = False

```
Output # 4:
```
['she', 'was', 'not', 'in', 'the', 'world', '.']
```

## Stochastic Model 

Input # 1:
```
sentence = ['robot']
n = 3
corpus = corpus
randomize = True

```
Output # 1:
```
['robot', 'she', 'had', 'started', '.']
```

-----------
Input # 2:
```
sentence = ['she', 'was', 'not']
n = 1
corpus = corpus
randomize = True

```
Output # 2:
```
['she', 'was', 'not', ',', 'when', 'so', 'with', 'time', 'yet', 'the']
```
----------
Input # 3:
```
sentence = ['robot']
n = 2
corpus = corpus
randomize = True

```
Output # 3:
```
['robot', 'assured', 'of', 'nature', 'of', 'colonel', "'s", 'affection', 'was', 'vexed']
```
----------
Input # 4:
```
sentence = ['she', 'was', 'not']
n = 3
corpus = corpus
randomize = True

```
Output # 4:
```
['she', 'was', 'not', 'in', 'my', 'banker', "'s", 'hands', ',', 'to']
```








