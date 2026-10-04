class Node:
    def __init__(self, val = None):
        self.val = val
        self.child = []
        self.is_finish = False

class PrefixTree:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        current = self.root
        start = len(word)
        for i, c in enumerate(word):
            vals = [node.val for node in current.child]
            if c not in vals:
                start = i
                break
            current = current.child[vals.index(c)]
        
        for i in range(start, len(word)):
            next_node = Node(word[i])
            current.child.append(next_node)
            current = next_node
        
        current.is_finish = True
        

    def search(self, word: str) -> bool:
        current = self.root
        for c in word:
            vals = [node.val for node in current.child]
            if c not in vals:
                return False
            current = current.child[vals.index(c)]
        
        return current.is_finish

    def startsWith(self, prefix: str) -> bool:
        current = self.root
        for c in prefix:
            vals = [node.val for node in current.child]
            if c not in vals:
                return False
            current = current.child[vals.index(c)]
        
        return True
        