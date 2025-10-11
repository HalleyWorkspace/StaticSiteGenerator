import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_2(self):
        node = TextNode("This is a node", TextType.LINK, "www.google.com")
        node2 = TextNode("This is a node", TextType.IMAGE, "www.google.com")
        self.assertNotEqual(node,node2)

    def test_3(self):
        node = TextNode("This is a node", TextType.CODE, None)
        node2 = TextNode("This is a node", TextType.CODE, None)
        self.assertEqual(node,node2)


if __name__ == "__main__":
    unittest.main()