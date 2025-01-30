class HTMLNode:
    """
    A class representing an HTML node.

    Attributes:
        tag (str): The tag of the HTML node.
        value (str): The value of the HTML node.
        children (list): The children of the HTML node.
        props (dict): The properties of the HTML node.
    """

    def __init__(self, tag: str = None, value: str = None, children: list = None, props=None):
        """
        Initializes an HTMLNode instance.

        Args:
            tag (str): The tag of the HTML node.
            value (str): The value of the HTML node.
            children (list): The children of the HTML node.
            props (dict): The properties of the HTML node.
        """
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        """
        Converts the HTML node to an HTML string.

        Raises:
            NotImplementedError: This method should be implemented by subclasses.
        """
        raise NotImplementedError()

    def props_to_html(self):
        """
        Converts the properties of the HTML node to an HTML string.

        Returns:
            str: The HTML string representation of the properties.
        """
        result = ""  # Always start with an empty string
        if self.props:  # Check if props is not None and not empty
            for key, value in self.props.items():
                result += f' {key}="{value}"'
        return result  # Return the result whether props is None or not

    def __repr__(self):
        """
        Returns a string representation of the HTMLNode instance.

        Returns:
            str: The string representation of the HTMLNode instance.
        """
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"


class ParentNode(HTMLNode):

    def __init__(self, tag, children: list, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if not self.tag:
            raise ValueError("You must have a tag")
        if not self.children:
            raise ValueError("You must have children this is a ParentNode")
        children_html = ""
        for child in self.children:
            children_html += child.to_html()
        return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"

    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("Invalid HTML: no value")
        if self.tag is None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"
