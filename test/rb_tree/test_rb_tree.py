import unittest
from RB_trees import RBTree

class TestCustomRBTree(unittest.TestCase):
    def setUp(self):
        self.tree = RBTree()

    def test_insertion_sequence(self):
        # Insert a sequence of numbers
        values = [10, 20, 30, 15, 25, 5]
        for v in values:
            self.tree.insert(v)

        # Check search
        self.assertTrue(self.tree.search(15))
        self.assertFalse(self.tree.search(100))

    def test_deletion_cases(self):
        values = [10, 20, 30, 40, 50]
        for v in values:
            self.tree.insert(v)

        self.tree.delete(20)  # Deleting a black node
        self.assertFalse(self.tree.search(20))

        self.tree.delete(30)  # Deleting a red node
        self.assertFalse(self.tree.search(30))

    def test_black_height(self):
        values = [7, 3, 18, 10, 22, 8, 11, 26]
        for v in values:
            self.tree.insert(v)

        # Check black height consistency
        def check_black_height(node):
            if node is None:
                return 1
            left = check_black_height(node.left)
            right = check_black_height(node.right)
            self.assertEqual(left, right)
            return left + (1 if node.color == "BLACK" else 0)

        check_black_height(self.tree.root)

if __name__ == '__main__':
    unittest.main()
