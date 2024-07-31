## Problem3
#Replace Words (https://leetcode.com/problems/replace-words/)
#Define TrieNode class
class TrieNode:
    def __init__(self):
        self.children = [None] * 26  
        self.end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            i = ord(c) - ord("a")
            if curr.children[i] is None:
                curr.children[i] = TrieNode()
            curr = curr.children[i]
        curr.end = True

    def searchRoot(self, word: str) -> str:
        curr = self.root
        root = []
        for c in word:
            i = ord(c) - ord("a")
            if curr.children[i] is None or curr.end:
                break
            root.append(c)
            curr = curr.children[i]
        return ''.join(root) if curr.end else word

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = Trie()
        for word in dictionary:
            trie.insert(word)

        def replace(word: str) -> str:
            return trie.searchRoot(word)

        return ' '.join(map(replace, sentence.split()))
