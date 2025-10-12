import unittest

from htmlnode import HTMLNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("a","This is text",None,{"href":"https://www.google.com","target": "_blank"})
        node2  = HTMLNode("a","This is text",None,{"href":"https://www.google.com","target": "_blank"})
        self.assertEqual(node.props_to_html(), node2.props_to_html())

    


if __name__ == "__main__":
    unittest.main()