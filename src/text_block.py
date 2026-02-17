from enum import Enum
import re


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def block_to_block_type(block:str):
    
    if re.match(r"#{1,6} \w+",block):
        return BlockType.HEADING
    if block.startswith("```\n") and block.endswith("```"):
        return BlockType.CODE
    if re.match(r"^> *.+",block,flags=re.MULTILINE):
        return BlockType.QUOTE
    if re.match(r"^- .+",block,flags=re.MULTILINE):
        return BlockType.UNORDERED_LIST
    if re.match(r"^\d\. .+",block,flags=re.MULTILINE):
        numbering = re.findall(r"^\d\.",block,flags=re.MULTILINE)
        numbers = [int(number[:-1]) for number in numbering]
        if numbers[0] == 1 and numbers == list(range(1,max(numbers)+1)):
            return BlockType.ORDERED_LIST


    return BlockType.PARAGRAPH

    

def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    blocks = [block.strip() for block in blocks]
    blocks = [block for block in blocks if block]
    return blocks