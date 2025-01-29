import unittest
from htmlnode import HTMLNode


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


if __name__ == '__main__':
    unittest.main()
