class Node:
    def __init__(self):
        self.children = {}
        self.is_finish = False

class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        current = self.root
        for c in word:
            if c not in current.children:
                current.children[c] = Node()
            current = current.children[c]
        
        current.is_finish = True

    def search(self, word: str) -> bool:
        candidates = [self.root]
        for c in word:
            if len(candidates) == 0:
                return False
            next_candidates = []
            for candidate in candidates:
                if c == ".":
                    for child in candidate.children.values():
                        next_candidates.append(child)
                elif c in candidate.children:
                    next_candidates.append(candidate.children[c])
            
            candidates = next_candidates
        
        for candidate in candidates:
            if candidate.is_finish:
                return True
        
        return False