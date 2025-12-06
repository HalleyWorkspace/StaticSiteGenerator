from enum import Enum
from htmlnode import LeafNode
import re

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"


class TextNode:

    def __init__(self,text,text_type,url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, textNode):
        if self.text == textNode.text and self.text_type == textNode.text_type:
            if self.url:
                if self.url == textNode.url:
                    return True
            else:
                return True
        return False

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"

def text_node_to_html_node(text_node):
    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(tag=None, value=text_node.text)
        case TextType.BOLD:
            return LeafNode(tag="b",value=text_node.text)
        case TextType.ITALIC:
            return LeafNode(tag="i",value=text_node.text)
        case TextType.CODE:
            return LeafNode(tag="code",value=text_node.text)
        case TextType.LINK:
            return LeafNode(tag="a",value=text_node.text,href=text_node.url)
        case TextType.IMAGE:
            return LeafNode(tag="img",value="",src=text_node.url,alt=text_node.text)
        
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        sections = old_node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("invalid markdown, formatted section not closed")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], TextType.TEXT))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes

def extract_markdown_images(text):
    regex= r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(regex,text)
    return matches

def extract_markdown_links(text):
    regex= r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(regex,text)
    return matches