import unittest
from htmlnode import HTMLNode, LeafNode


class TestHTMLNode(unittest.TestCase):

    def test_init(self):
        node = HTMLNode(tag="div", value="Hello", children=[],
                        props={"class": "container"})
        self.assertEqual(node.tag, "div")
        self.assertEqual(node.value, "Hello")
        self.assertEqual(node.children, [])
        self.assertEqual(node.props, {"class": "container"})

    def test_props_to_html(self):
        node = HTMLNode(props={"class": "container", "id": "main"})
        self.assertEqual(node.props_to_html(), ' class="container" id="main"')

        node_empty_props = HTMLNode()
        self.assertEqual(node_empty_props.props_to_html(), '')

    def test_repr(self):
        node = HTMLNode(tag="div", value="Hello", children=[],
                        props={"class": "container"})
        self.assertEqual(
            repr(node), "HTMLNode(div, Hello, [], {'class': 'container'})")
        leafnode = LeafNode("a", "Hello", {"href": "youtube.com"})
        self.assertEqual(
            repr(leafnode), "LeafNode(a, Hello, {'href': 'youtube.com'})")

    def test_to_html_no_children(self):
        node = LeafNode("p", "Hello")
        self.assertEqual(node.to_html(), "<p>Hello</p>")

    def test_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")


if __name__ == '__main__':
    unittest.main()
