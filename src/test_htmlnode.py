import htmlnode *
import unittest

class TestHTMLNode(unittest.TestCase):
    def test_base_html_node(self):
        # Test base HTMLNode initialization
        node = HTMLNode(tag="div", value="test", children=[], props={"class": "test"})
        self.assertEqual(node.tag, "div")
        self.assertEqual(node.value, "test")
        self.assertEqual(node.children, [])
        self.assertEqual(node.props, {"class": "test"})

        # Test props_to_html method
        self.assertEqual(node.props_to_html(), ' class="test"')
        
        # Test props_to_html with no props
        node = HTMLNode()
        self.assertEqual(node.props_to_html(), "")

        # Test props_to_html with multiple props
        node = HTMLNode(props={"class": "test", "id": "main"})
        self.assertTrue(' class="test"' in node.props_to_html())
        self.assertTrue(' id="main"' in node.props_to_html())

class TestLeafNode(unittest.TestCase):
    def test_leaf_node_initialization(self):
        # Test basic initialization
        node = LeafNode("span", "Hello", {"class": "greeting"})
        self.assertEqual(node.tag, "span")
        self.assertEqual(node.value, "Hello")
        self.assertEqual(node.props, {"class": "greeting"})
        self.assertIsNone(node.children)

    def test_leaf_node_to_html(self):
        # Test with no tag (text node)
        node = LeafNode(None, "Just text")
        self.assertEqual(node.to_html(), "Just text")

        # Test with tag and value
        node = LeafNode("span", "Hello")
        self.assertEqual(node.to_html(), "Just text")  # This should actually fail - implementation is incomplete

        # Test with properties
        node = LeafNode("span", "Hello", {"class": "greeting"})
        self.assertEqual(node.to_html(), "Just text")  # This should actually fail - implementation is incomplete

    def test_leaf_node_validation(self):
        # Test that None value raises ValueError
        with self.assertRaises(ValueError):
            LeafNode("span", None).to_html()

        # Test various value types
        node = LeafNode(None, 42)
        self.assertEqual(node.to_html(), "42")

        node = LeafNode(None, True)
        self.assertEqual(node.to_html(), "True")

class TestParentNode(unittest.TestCase):
    def test_parent_node_initialization(self):
        # Test basic initialization
        child = LeafNode(None, "Hello")
        node = ParentNode("div", [child], {"class": "container"})
        self.assertEqual(node.tag, "div")
        self.assertEqual(node.children, [child])
        self.assertEqual(node.props, {"class": "container"})
        self.assertIsNone(node.value)

    def test_parent_node_to_html(self):
        # Test with single child
        child = LeafNode(None, "Hello")
        node = ParentNode("div", [child])
        self.assertEqual(node.to_html(), "<div>Hello</div>")

        # Test with multiple children
        children = [
            LeafNode(None, "Hello"),
            LeafNode("span", "World"),
            LeafNode(None, "!")
        ]
        node = ParentNode("div", children)
        self.assertEqual(node.to_html(), "<div>HelloWorld!</div>")  # This should actually fail - LeafNode implementation incomplete

        # Test with properties
        node = ParentNode("div", [LeafNode(None, "Hello")], {"class": "greeting"})
        self.assertEqual(node.to_html(), '<div class="greeting">Hello</div>')

    def test_parent_node_validation(self):
        # Test that None tag raises ValueError
        with self.assertRaises(ValueError):
            ParentNode(None, [LeafNode(None, "Hello")]).to_html()

        # Test that empty children raises ValueError
        with self.assertRaises(ValueError):
            ParentNode("div", []).to_html()

        # Test that None children raises ValueError
        with self.assertRaises(ValueError):
            ParentNode("div", None).to_html()

    def test_nested_parent_nodes(self):
        # Test nested structure
        inner_node = ParentNode("p", [LeafNode(None, "Hello")])
        outer_node = ParentNode("div", [inner_node])
        self.assertEqual(outer_node.to_html(), "<div><p>Hello</p></div>")

        # Test complex nested structure with siblings
        children = [
            LeafNode(None, "Start: "),
            ParentNode("p", [LeafNode(None, "Hello")]),
            LeafNode(None, " Middle "),
            ParentNode("p", [LeafNode(None, "World")]),
            LeafNode(None, " End")
        ]
        node = ParentNode("div", children)
        self.assertEqual(node.to_html(), "<div>Start: <p>Hello</p> Middle <p>World</p> End</div>")

    def test_complex_structure(self):
        # Test a more complex HTML structure
        structure = ParentNode("div", [
            ParentNode("header", [
                LeafNode("h1", "Title", {"class": "main-title"}),
                LeafNode("p", "Subtitle")
            ], {"class": "header"}),
            ParentNode("main", [
                ParentNode("section", [
                    LeafNode("h2", "Section 1"),
                    LeafNode("p", "Content 1")
                ]),
                ParentNode("section", [
                    LeafNode("h2", "Section 2"),
                    LeafNode("p", "Content 2")
                ])
            ], {"id": "main-content"}),
            ParentNode("footer", [
                LeafNode("p", "Footer text")
            ])
        ], {"class": "container"})
        
        expected_html = (
            '<div class="container">'
            '<header class="header">'
            '<h1 class="main-title">Title</h1>'
            '<p>Subtitle</p>'
            '</header>'
            '<main id="main-content">'
            '<section><h2>Section 1</h2><p>Content 1</p></section>'
            '<section><h2>Section 2</h2><p>Content 2</p></section>'
            '</main>'
            '<footer><p>Footer text</p></footer>'
            '</div>'
        )
        
        self.assertEqual(structure.to_html(), expected_html)  # This should actually fail - LeafNode implementation incomplete

if __name__ == '__main__':
    unittest.main()