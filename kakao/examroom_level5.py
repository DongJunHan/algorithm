#아직 못품
def make_binary_tree(num, links, binary_tree, root, index):
    if root == -1 or index > len(binary_tree):
        return binary_tree
    binary_tree[index] = num[root]
    binary_tree = make_binary_tree(num, links, binary_tree, links[root][0], index * 2)
    binary_tree = make_binary_tree(num, links, binary_tree, links[root][1], index * 2 + 1)

    return binary_tree
def solution(k, num, links):
    answer = 0
    root = None
    binary_tree = [0 for _ in range(2*len(num)+1)]
    #find root
    tmp_root = root
    while True:
        for k ,v in enumerate(links):
            if v[0] == -1 or v[1] == -1:
                continue
            if tmp_root == None:
                tmp_root = k
            else:
                if tmp_root in v:
                    tmp_root = k
        if root != tmp_root:
            root = tmp_root
        else:
            break
    #make binary tree
    binary_tree = make_binary_tree(num, links, binary_tree, root, 1)
    enough = sum(num) // k



    print(binary_tree)
    return answer


if __name__ == "__main__":
    k = 3
    num = [12, 30, 1, 8, 8, 6, 20, 7, 5, 10, 4, 1]
    links = [[-1, -1], [-1, -1], [-1, -1], [-1, -1], [8, 5], [2, 10], [3, 0], [6, 1], [11, -1], [7, 4], [-1, -1], [-1, -1]]
    # links = [[-1, -1], [-1, -1], [-1, 0], [2, 1]]
    print(solution(k, num, links))