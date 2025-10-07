class RBNode:
    def __init__(self, value, point):
        self.val = value
        self.parent = None
        self.left = None
        self.right = None
        self.red = True          
        self.color = "RED"
        self.point = point


class RBTree:
    def __init__(self):
        self.nil = RBNode(None, None)
        self.nil.red = False
        self.root = self.nil

    def getRoot(self):
        return self.root

    # ----- Insertion -----
    def insert(self, value, point):
        new_node = RBNode(value, point)
        new_node.left = self.nil
        new_node.right = self.nil

        parent = None
        current = self.root
        while current != self.nil:
            parent = current
            if value < current.val:
                current = current.left
            elif value > current.val:
                current = current.right
            else:
                # Duplicate, ignore
                return

        new_node.parent = parent
        if parent is None:
            self.root = new_node
        elif value < parent.val:
            parent.left = new_node
        else:
            parent.right = new_node

        self.fix_insert(new_node)

    # ----- Fix Insert -----
    def fix_insert(self, node):
        while node != self.root and node.parent.red:
            parent = node.parent
            grandparent = parent.parent
            if grandparent is None:
                break  # Reached root's child

            if parent == grandparent.left:
                uncle = grandparent.right
                if uncle.red:
                    parent.red = False
                    uncle.red = False
                    grandparent.red = True
                    node = grandparent
                else:
                    if node == parent.right:
                        node = parent
                        self.rotate_left(node)
                        parent = node.parent
                    parent.red = False
                    grandparent.red = True
                    self.rotate_right(grandparent)
            else:
                uncle = grandparent.left
                if uncle.red:
                    parent.red = False
                    uncle.red = False
                    grandparent.red = True
                    node = grandparent
                else:
                    if node == parent.left:
                        node = parent
                        self.rotate_right(node)
                        parent = node.parent
                    parent.red = False
                    grandparent.red = True
                    self.rotate_left(grandparent)
        self.root.red = False

    # ----- Left Rotation -----
    def rotate_left(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.nil:
            y.left.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    # ----- Right Rotation -----
    def rotate_right(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.nil:
            y.right.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    # ----- Search -----
    def search(self, value):
        current = self.root
        while current != self.nil:
            if value < current.val:
                current = current.left
            elif value > current.val:
                current = current.right
            else:
                return True
        return False

    # ----- Inorder Traversal -----
    def inorder(self, node=None):
        if node is None:
            node = self.root
        if node != self.nil:
            self.inorder(node.left)
            color = "R" if node.red else "B"
            print(f"{node.val}({color})", end=" ")
            self.inorder(node.right)

# ----- Deletion -----
    # Transplant one subtree for another
    def transplant(self, u, v):
        if u.parent is None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    # Find the minimum node in a subtree
    def minimum(self, node):
        while node.left != self.nil:
            node = node.left
        return node

    # Delete a node with a given value
    def delete(self, value):
        z = self.root
        while z != self.nil and z.val != value:
            if value < z.val:
                z = z.left
            else:
                z = z.right
        if z == self.nil:
            return  # Node not found

        y = z
        y_original_red = y.red
        if z.left == self.nil:
            x = z.right
            self.transplant(z, z.right)
        elif z.right == self.nil:
            x = z.left
            self.transplant(z, z.left)
        else:
            y = self.minimum(z.right)
            y_original_red = y.red
            x = y.right
            if y.parent == z:
                x.parent = y
            else:
                self.transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
            self.transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.red = z.red

        if not y_original_red:
            self.fix_delete(x)

    # ----- Fix Delete -----
    def fix_delete(self, x):
        while x != self.root and not x.red:
            if x == x.parent.left:
                w = x.parent.right
                if w.red:
                    w.red = False
                    x.parent.red = True
                    self.rotate_left(x.parent)
                    w = x.parent.right
                if not w.left.red and not w.right.red:
                    w.red = True
                    x = x.parent
                else:
                    if not w.right.red:
                        w.left.red = False
                        w.red = True
                        self.rotate_right(w)
                        w = x.parent.right
                    w.red = x.parent.red
                    x.parent.red = False
                    w.right.red = False
                    self.rotate_left(x.parent)
                    x = self.root
            else:
                w = x.parent.left
                if w.red:
                    w.red = False
                    x.parent.red = True
                    self.rotate_right(x.parent)
                    w = x.parent.left
                if not w.left.red and not w.right.red:
                    w.red = True
                    x = x.parent
                else:
                    if not w.left.red:
                        w.right.red = False
                        w.red = True
                        self.rotate_left(w)
                        w = x.parent.left
                    w.red = x.parent.red
                    x.parent.red = False
                    w.left.red = False
                    self.rotate_right(x.parent)
                    x = self.root
        x.red = False
    
    # ----- Search -----
    def search(self, value):
        current = self.root
        while current != self.nil:
            if value < current.val:
                current = current.left
            elif value > current.val:
                current = current.right
            else:
                return True  # Found the value
        return False  # Not found
    
    def range_query(self, low, high):
        result = []
        def inorder_range(node):
            if node is self.nil:
                return

            if node.val > low:
                inorder_range(node.left)
            
            if low <= node.val <= high:
                result.append((node.val, node.point))
                print(node.val)

            if node.val < high:
                inorder_range(node.right)
        
        inorder_range(self.root)
        return result
        