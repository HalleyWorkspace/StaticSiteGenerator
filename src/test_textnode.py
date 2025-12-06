import unittest

from textnode import TextNode, TextType, split_nodes_delimiter, extract_markdown_images,extract_markdown_links


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

    def test_4(self):
        node = TextNode("This has a `code block` in it", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node],'`',TextType.CODE)
        expected_nodes = [
            TextNode("This has a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" in it", TextType.TEXT)
        ]
        self.assertEqual(new_nodes,expected_nodes)

    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_link(self):
        matches = extract_markdown_links(
            "This is text with a link [to boot dev](https://www.boot.dev)"
        )
        self.assertListEqual([("to boot dev", "https://www.boot.dev")], matches)
    
    if __name__ == "__main__":
        unittest.main()