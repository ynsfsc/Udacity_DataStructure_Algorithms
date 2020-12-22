## Represents a single node in the Trie
class TrieNode:
    def __init__(self):
        ## Initialize this node in the Trie
        self.is_word = False
        self.children = {}

    def insert(self, char):
        ## Add a child node in this Trie
        if char not in self.children:
            self.children[char] = TrieNode()
        
    def suffixes(self, suffix = ''):
        ## Recursive function that collects the suffix for 
        ## all complete words below this point
        output = []
        
        def _suffixes(current, suffix = ''):
            
            for char, node in current.children.items():
                if node.is_word:
                    output.append(suffix + char)
                
                _suffixes(node, suffix + char)
            
        _suffixes(self, '')
        return output

            
        
## The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        ## Initialize this Trie (add a root node)
        self.root = TrieNode()

    def insert(self, word):
        ## Add a word to the Trie
        current_node = self.root
        for char in word:
            if char not in current_node.children:
                current_node.insert(char)
            current_node = current_node.children[char]
            
        current_node.is_word = True
        

    def find(self, prefix):
        ## Find the Trie node that represents this prefix
        current = self.root
        for char in prefix:
            if char not in current.children:
                return None
            current = current.children[char]
            
        return current

MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym", 
    "fun", "function", "factory", 
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)
print("Word List: ")
print(wordList)

def f(prefix):
    if prefix != '':
        prefixNode = MyTrie.find(prefix)
        if prefixNode:
            print('\n'.join(prefixNode.suffixes()))
        else:
            print(prefix + " not found")
    else:
        print('')

# test1  
print("-"*40)
print("Test1 Input: " + "a")
f('a')
print("-"*40)
print('Expected:', 'nt', 'nthology', 'ntagonist', 'ntonym')

# test2
#should get:
#ie
#igger
#igonometry
#ipod
print("-"*40)
print("Test2 Input: " + "tripod")
f('tripod')
print("-"*40)
print('Expected:', '')

# test3
# should get "e not found"
print("-"*40)
print("Test3 Input: " + "e")
f('e')
print("-"*40)
print('Expected:', 'e not found')
