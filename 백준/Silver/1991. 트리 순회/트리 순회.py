import sys
def preOrder(root:str):
    if root != ".":
        print(root,end="")
        preOrder(dict_tree[root][0]) #left
        preOrder(dict_tree[root][1]) #right
def inOrder(root:str):
    if root != ".":
        inOrder(dict_tree[root][0]) #left
        print(root, end="")
        inOrder(dict_tree[root][1]) #right

def postOrder(root:str):
    if root != ".":
        postOrder(dict_tree[root][0])
        postOrder(dict_tree[root][1])
        print(root, end="")

if __name__ == "__main__":
    dict_tree = {}
    T = int(input())
    for test_case in range(T):
        root, left, right= sys.stdin.readline().strip().split()
        dict_tree[root] = [left, right]
    preOrder("A")
    print()
    inOrder("A")
    print()
    postOrder("A")