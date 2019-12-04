from queue import Queue


class BinaryTree:

    def __init__(self, data: object):
        self.__data = data
        self.__left = None
        self.__right = None

    def insert_left(self, new_node: object):
        """
        insert a node in the left branch
        :param new_node: object of the node
        :return:
        """
        if self.__left is None:
            self.__left = BinaryTree(new_node)
        else:
            t = BinaryTree(new_node)
            t.__left = self.__left
            self.__left = t

    def insert_right(self, new_node: object):
        """
        insert a node in the right branch
        :param new_node: object of the node
        :return:
        """
        if self.__right is None:
            self.__right = BinaryTree(new_node)
        else:
            t = BinaryTree(new_node)
            t.__right = self.__right
            self.__right = t

    def insert(self, new_node: object):
        """
        insert a node in the next branch available (from left to right)
        :param new_node: object of the node
        :return:
        """
        q = Queue()
        q.put(self)  # add the tree to a queue
        # do level order traversal until we find an empty place
        while not q.empty():
            _temp = q.get()
            if _temp.left() is None:
                _temp.insert_left(new_node)
                break
            else:
                q.put(_temp.left())
            if _temp.right() is None:
                _temp.insert_right(new_node)
                break
            else:
                q.put(_temp.right())

    def right(self):
        """
        return right branch
        :return:
        """
        return self.__right

    def left(self):
        """
        return left branch
        :return:
        """
        return self.__left

    def root(self) -> object:
        """
        return node data
        :return:
        """
        return self.__data

    def is_empty(self) -> bool:
        """
        is node empty
        :return:
        """
        return self.__data is None

    def preorder(self):
        """
        DFS in pre-order (node then left then right)
        :return:
        """
        print(self.__data)
        if self.__left is not None:
            self.__left.preorder()
        if self.__right is not None:
            self.__right.preorder()

    def inorder(self):
        """
        DFS in in-order (left then node then right)
        :return:
        """
        if self.__left is not None:
            self.__left.inorder()
        print(self.__data)
        if self.__right is not None:
            self.__right.inorder()

    def postorder(self):
        """
        DFS in post-oder (left then right then node
        :return:
        """
        if self.__left is not None:
            self.__left.postorder()
        if self.__right is not None:
            self.__right.postorder()
        print(self.__data)

    def dfs(self):
        """
        DFS depth first search
        :return:
        """
        s: list = []
        s.append(self)  # add tree to a stack
        # do a preorder traversal
        while len(s) != 0:
            _temp: BinaryTree = s.pop()
            if _temp is not None and not _temp.is_empty():
                print(_temp.root())
                s.append(_temp.right())
                s.append(_temp.left())

    def bfs(self):
        """
        BFS breadth first search
        :return:
        """
        q: Queue = Queue()
        q.put(self)         # enqueue

        while not q.empty():
            st = q.get()    # dequeue

            if st is not None:
                print(st.root())
                q.put(st.left())
                q.put(st.right())


    def height(self) -> int:
        """
        calcule la hauteur de l'arbre
        :param node:
        :return: la hauteur de l'arbre
        """











    def depth(self, key: object) -> int:
        """
        calcule la profondeur du nœude key
        :param key: la clé du node
        :return: la profondeur du node
        """

















def pep(tree: BinaryTree):
    print()
    print("preorder")
    tree.preorder()

    print()
    print("inorder")
    tree.inorder()

    print()
    print("postorder")
    tree.postorder()

    print()
    print("dfs iterative")
    tree.dfs()


if __name__ == "__main__":
    """
                   root
                /        \  
               a          d 
             /   \      /   \
             b   c      e    f
    """

    r = BinaryTree('root')
    r.insert('a')
    r.insert('d')
    r.insert('b')
    r.insert('c')
    r.insert('e')
    r.insert('f')

    # print()
    # print("bfs")
    # r.bfs()

    # print()
    # print("hauter:", r.height())
    #
    print("profondeur de a:", r.depth("a"))
    print("profondeur de e:", r.depth("e"))
    print("profondeur de g:", r.depth("g"))
