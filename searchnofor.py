def return_index( w):
    if(w<='9' and w>='0'):
        return ord(w)-ord('0')
    else:
        return ord(w)-ord('a')+10
class TrieNode(object):
    def __init__(self, char: str):
        self.char = char
        self.children = [0]*36
        self.word_finished = False
        self.end_word = False
        self.end_index = -1

def add(root, word: str,index):
    node = root
    for i in range(0,len(word)):
        char = word[i]
        found_in_child = False
        # Search for the character in the children of the present `node`
        if node.children[return_index(char)] != 0:
            node = node.children[return_index(char)]
            found_in_child = True
            if i == len(word)-1:
                # add end word here
                node.end_word = True
                node.index = index
        if not found_in_child:
            new_node = TrieNode(char)
            node.children[return_index(char)] = new_node
            node = new_node
            if i == len(word)-1:
                # add end word here
                node.end_word = True
                node.index = index

    node.word_finished = True

def traverse(root,list_index):
    if root == 0:
        return
    for i in range(0,36):
        traverse(root.children[i],list_index)
    if root.end_word:
        list_index.append(root.index)

def find_prefix(root, prefix: str):
    node = root
    for char in prefix:
        char_not_found = True
        if node.children[return_index(char)] != 0:
            node = node.children[return_index(char)]
            char_not_found = False
        if char_not_found:
            return []
    list_index = []
    traverse(node,list_index)
    return list_index

if __name__ == "__main__":
    root = TrieNode('*')
    sentance=input("Add something ")
    words=sentance.split()
    for w in words:
        add(root,w,2)
    
    sen=input("Search something ")
    wo=sen.split()
    for w in wo:
        print(find_prefix(root,w))
    add(root, "hackathon",1)
    add(root, 'hack',0)

    print(find_prefix(root, 'hac'))
    print(find_prefix(root, 'hack'))
    print(find_prefix(root, 'hackathon'))
    print(find_prefix(root, 'ha'))
    print(find_prefix(root, 'hammer'))
