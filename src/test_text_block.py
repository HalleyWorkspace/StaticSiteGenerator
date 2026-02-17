import unittest
from text_block import markdown_to_blocks, block_to_block_type,BlockType

class TestMarkdownBlock(unittest.TestCase):
    
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
            blocks
            )

    def test_block_to_header(self):
        block = """### Hello World!"""
        test_type = block_to_block_type(block)
        self.assertEqual(
            BlockType.HEADING,
            test_type
        )

    def test_block_to_code(self):
        block="""```\nprint("Hello World!")\n```"""
        test_type = block_to_block_type(block)
        self.assertEqual(
            BlockType.CODE,
            test_type
        )
    
    def test_block_to_quote(self):
        block="""> Hello\n>World!"""
        test_type = block_to_block_type(block)
        self.assertEqual(
            BlockType.QUOTE,
            test_type
        )

    def test_block_to_unlist(self):
        block="""- Hello\n- World!"""
        test_type = block_to_block_type(block)
        self.assertEqual(
            BlockType.UNORDERED_LIST,
            test_type
        )

    def test_block_to_orderlist(self):
        block="""1. Hello\n2. World!"""
        test_type = block_to_block_type(block)
        self.assertEqual(
            BlockType.ORDERED_LIST,
            test_type
        )

    def test_block_to_paragraph(self):
        block="""Hello\nWorld!"""
        test_type = block_to_block_type(block)
        self.assertEqual(
            BlockType.PARAGRAPH,
            test_type
        )


if __name__ == "__main__":
    unittest.main()