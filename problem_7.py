# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self, handler = "not found handler"):
        # Initialize the node with children as before, plus a handler
        self.children = {}
        self.handler = handler

    def insert(self, subpath, handler):
        # Insert the node as before
        self.children[subpath] = RouteTrieNode(handler)

# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, root_handler = "root handler", not_found_handler = "not found handler"):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode(root_handler)
        self.not_found_handler = not_found_handler
        self.root.children[''] = RouteTrieNode(root_handler)

    def insert(self, path, handler):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        current = self.root
        for subpath in path:
            if subpath not in current.children:
                current.insert(subpath, self.not_found_handler)
            current = current.children[subpath]
        current.handler = handler
        if path[-1] != '':
            current.children[''] = RouteTrieNode(handler)

    def find(self, path):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        current = self.root
        for subpath in path:
            if subpath not in current.children:
                return self.not_found_handler
            current = current.children[subpath]
        return current.handler

# The Router class will wrap the Trie and handle 
class Router:
    def __init__(self, root_handler = "root handler", not_found_handler = "not found handler"):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.trie = RouteTrie(root_handler, not_found_handler)

    def add_handler(self, path, handler):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        path = self.split_path(path)
        self.trie.insert(path, handler)

    def lookup(self, path):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        path = self.split_path(path)
        return self.trie.find(path)


    def split_path(self, path):
        # you need to split the path into parts for 
        # both the add_handler and loopup functions,
        # so it should be placed in a function here
        return path.split('/')[1:]

# Here are some test cases and expected outputs you can use to test your implementation

# create the router and add a route
router = Router("root handler", "not found handler") 
# add a route
router.add_handler("/home/about", "about handler")  

print("Problem 7")
print("-"*40)
print("Input Handler: " + "/home/about - about handler")

# some lookups with the expected output
print("-"*40)
print("Lookup Input: " + "/")
print("Output: ")
print(router.lookup("/")) # should print 'root handler'
print("Expect:")
print('root handler')
print("-"*40)
print("Lookup Input: " + "/home")
print("Output: ")
print(router.lookup("/home")) # should print 'not found handler'
print("Expect: ")
print('not found handler')
print("-"*40)
print("Lookup Input: " + "/home/about")
print("Output: ")
print(router.lookup("/home/about")) # should print 'about handler'
print("Expect: ")
print('about handler')
print("-"*40)
print("Lookup Input: " + "/home/about/")
print("Output: ")
print(router.lookup("/home/about/")) # should print 'about handler'
print("Expect: ")
print('about handler')
print("-"*40)
print("Lookup Input: " + "/home/about/me")
print("Output: ")
print(router.lookup("/home/about/me")) # should print 'not found handler'
print("Expect: ")
print('not found handler')