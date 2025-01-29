from enum import Enum


class TextType(Enum):
    """
    An enumeration representing different types of text.
    """
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"


class TextNode:
    """
    A class representing a text node.

    Attributes:
        text (str): The text content of the node.
        text_type (TextType): The type of the text.
        url (str): The URL associated with the text node (optional).
    """

    def __init__(self, text, text_type, url=None):
        """
        Initializes a TextNode instance.

        Args:
            text (str): The text content of the node.
            text_type (TextType): The type of the text.
            url (str): The URL associated with the text node (optional).
        """
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        """
        Checks if two TextNode instances are equal.

        Args:
            other (TextNode): The other TextNode instance to compare.

        Returns:
            bool: True if the instances are equal, False otherwise.
        """
        return (
            self.text_type == other.text_type
            and self.text == other.text
            and self.url == other.url
        )

    def __repr__(self):
        """
        Returns a string representation of the TextNode instance.

        Returns:
            str: The string representation of the TextNode instance.
        """
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
