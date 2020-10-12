from index_intersection import *


def return_index( w):
    l = [',','.','/','~','!','#','\'','$','%','&','(',')','…',':','-']
    if(w<='9' and w>='0'):
        return ord(w)-ord('0')
    elif w in l:
        return 10+l.index(w)
    elif (w<='z' and w>='a'):
        return ord(w)-ord('a')+20+2+1+1+1
    else:
        return 0

class TrieNode(object):
    def __init__(self, char: str):
        self.char = char
        self.children = [0]*51
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

def find(root, prefix: str):
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

def insert(root,word,index):
    word = word.lower()
    for i in range(0,len(word)):
        for j in range(i+1,len(word)):
            add(root,word[i:j+1],index)

def add_dic(list_sentence):
    
    for index in range(0,len(list_sentence)):
        for word in list_sentence[index].split():
            insert(root,word,index)

def query(que):
    combine_list = []
    for word in que.split():
        combine_list.append(find(root,word))
    return index_intersection(combine_list)

root = TrieNode('*')