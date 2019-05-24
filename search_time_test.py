import time
import random
from binary_search_tree.linkedbst import LinkedBST
import copy
import sys

sys.setrecursionlimit(3000)


def file_processor(fname):
    with open(fname) as f:
        words = f.readlines()

    return words


def python_list_case(words):
    """
    function to test the time needed to find a particular value in the python list
    :return: float
    """
    x = random.sample(words, 10000)

    start = time.time()
    for i in x:
        words.index(i)
    end = time.time()
    return end - start


def binary_search_tree(words):
    t = LinkedBST()

    rearranged = copy.deepcopy(words)
    random.shuffle(rearranged)

    for i in rearranged:
        t.add(i)

    x = random.sample(list(t), 10000)
    start = time.time()
    for i in x:
        t.find(i)
    end = time.time()
    return end - start


def binary_search_tree_balanced(words):
    t = LinkedBST()

    rearranged = copy.deepcopy(words)
    random.shuffle(rearranged)
    middle = rearranged[len(rearranged) // 2]
    t.add(middle)
    for i in rearranged:
        if i != middle:
            t.add(i)

    x = random.sample(list(t), 10000)
    start = time.time()
    for i in x:
        t.find(i)
    end = time.time()
    return end - start


if __name__ == "__main__":
    words_dict = file_processor("words.txt")

    print(
        python_list_case(words_dict))  # Time for Python List - 12.254745244979858

    print(
        binary_search_tree(words_dict))  # Time for unbalanced Binary Search Tree - 0.09078550338745117

    print(
        binary_search_tree_balanced(words_dict))  # Time for balanced Binary Search Tree - 0.09012627601623535
