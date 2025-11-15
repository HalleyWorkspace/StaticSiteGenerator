

class HTMLNode:

    def __init__(self,tag=None,value=None,children=None,props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        prop_html = ""
        if self.props:
            for prop,attribute in self.props.items():
                prop_html += f' {prop}="{attribute}"'
        return prop_html
    
    def __repr__(self):
        return f"HTMLNode({self.tag},{self.value},{self.children},{self.props})"
    
    
class LeafNode(HTMLNode):

    def __init__(self, tag, value, children = None, props = None):
        if children:
            raise Exception("LeafNodes can't have children")
        super().__init__(tag, value, children, props)

    def to_html(self):
        if not self.value:
            raise ValueError()
        if not self.tag:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    
class ParentNode(HTMLNode):

    def __init__(self, tag, children, value=None, props = None):
        if not children:
            raise Exception("Parent needs Children")
        super().__init__(tag,value,children,props)

    def to_html(self):
        if not self.tag:
            raise ValueError("No Tag")
        if not self.children:
            raise ValueError("No Children")
        html = f"<{self.tag}{self.props_to_html()}>"
        for child in self.children:
            html += child.to_html()
        html += f"</{self.tag}>"
        return html