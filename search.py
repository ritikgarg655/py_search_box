from index_intersection import *

def lowerstring(d):
    return d.lower()

def split_string(sentence):
    return sentence.split()

def similar_words(s):
    import nltk
    from nltk.corpus import wordnet
    synonyms = []
    for syn in wordnet.synsets(s):
        for lemma in syn.lemmas():
            synonyms.append(lemma.name())
    return synonyms

def stop_filter(temp):
    import nltk
    from nltk.corpus import stopwords 
    from nltk.tokenize import word_tokenize 
    
    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(temp) 
    
    filtered_sentence=[]
    for w in word_tokens: 
        if w not in stop_words: 
            filtered_sentence.append(w) 
    return filtered_sentence

def return_index( w):
    l = [',','.','/','~','!','#','\'','$','%','&','(',')','…',':','-',' ']
    if(w<='9' and w>='0'):
        return ord(w)-ord('0')+1
    elif w in l:
        return 10+l.index(w)
    elif (w<='z' and w>='a'):
        return ord(w)-ord('a')+20+2+1+1+1+1+1
    elif (w<='Z' and w>='A'):
        return ord(w)-ord('A')+20+2+1+1+1+26+1+1
    else:
        # if undefine char has arrived send to  0 position
        return 0

class TrieNode(object):
    def __init__(self, char: str):
        self.char = char
        self.children = [0]*(51+26+1+1)
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

def insert(root,word,index,filters):
    print(type(filters))
    for key in filters:
        if(key == 'lower' and filters[key]):
            lowerstring(word)
        elif key == 'synonyms' and filters[key]:
            li = similar_words(word)
        elif key == 'stopword' and filters[key]:
            li2 = stop_words(word)

    word = word.lower()
    for i in range(0,len(word)):
        for j in range(i+1,len(word)):
            add(root,word[i:j+1],index)

def add_dic(list_sentence,filters):
    for index in range(0,len(list_sentence)):
        if(filters[split]):
            for word in list_sentence[index].split():
                insert(root,word,index,filters)
        else:
            insert(root,list_sentence[index],index,filters)

def query(que):
    combine_list = []
    for word in que.split():
        combine_list.append(find(root,word))
    return index_intersection(combine_list)

root = TrieNode('*')
