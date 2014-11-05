"""
Trie data structure
"""

class Node:

    def __init__(self):
        self.word = None
        self.children = {}

    def insert(self, kmer):
        node = self
        for letter in word:
            if letter not in node.children:
                node.children[letter] = TrieNode()
            node = node.children[letter]
        node.word = word


def get_matches(word, trie, d=0):
    curr_row = range(len(word) + 1)
    results = []
    for letter in trie.children:
        _search(trie.children[letter], letter, word, curr_row, results, d)
    return results


def _search(node, letter, word, prev_row, results, d):
    cols = len(word) + 1
    curr_row = [prev_row[0] + 1]
    for col in range(1, cols):
        ins_diff = curr_row[col-1] + 1
        del_diff = prev_row[col] + 1
        if word[col-1] != letter:
             rep_diff = prev_row[col-1] + 1
        else:
             rep_diff = prev_row[col-1]
        curr_row.append(min(ins_diff, del_diff, rep_diff))
    if curr_row[-1] <= d and node.word != None:
        results.append(node.word)
    if min(curr_row) <= d:
        for letter in node.children:
            _search(node.children[letter], letter, word, curr_row,
                    results, d)
