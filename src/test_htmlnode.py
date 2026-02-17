import unittest

from htmlnode import HTMLNode,LeafNode,ParentNode
from textnode import TextNode, text_node_to_html_node, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("a","This is text",None,{"href":"https://www.google.com","target": "_blank"})
        node2  = HTMLNode("a","This is text",None,{"href":"https://www.google.com","target": "_blank"})
        self.assertEqual(node.props_to_html(), node2.props_to_html())

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a","This is text",{"href":"https://www.google.com","target": "_blank"})
        self.assertEqual(node.to_html(),'<a href="https://www.google.com" target="_blank">This is text</a>')
    

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")


if __name__ == "__main__":
    unittest.main()