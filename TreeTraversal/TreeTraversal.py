import json

class Node: 
    def __init__(self, key): 
        self.val = key
        self.children = []

def build_tree(datalist, node=None):
    child = ""

    for i, row in enumerate(datalist):
        for key in row:
            if row[key] == node:
                #Root = Node(row[key])
                #Root.children.append(child)
                #print(Root.val, Root.children)

                if row[key] not in tree:
                    tree.update({row[key]: [child]})
                else:
                    tree[row[key]].append(child)

                datalist[i] = []
                build_tree(datalist, child)
            child = row[key]

def Walk(mydict):
    for key in tree:
        print(key, tree[key])


tree = {}
get_file = json.load(open("json_file"))
build_tree(get_file)
Walk(tree)
