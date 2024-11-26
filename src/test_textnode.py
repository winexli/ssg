import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_text_type(self):
        node = TextNode("Test", TextType.BOLD)
        self.assertEqual(node.text_type, TextType.BOLD)
        node2 = TextNode("Test", TextType.ITALIC) 
        self.assertEqual(node2.text_type, TextType.ITALIC)

    def test_text_value(self):
        node = TextNode("Hello World", TextType.BOLD)
        self.assertEqual(node.text, "Hello World")

    def test_not_equal(self):
        node = TextNode("Test", TextType.BOLD) 
        node2 = TextNode("Different", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_different_types(self):
        node = TextNode("Test", TextType.BOLD)
        node2 = TextNode("Test", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_url_none(self):
        node = TextNode("Test", TextType.LINK)
        node2 = TextNode("Test", TextType.LINK)
        self.assertEqual(node, node2)
        node.url = "https://www.test.com"
        self.assertNotEqual(node, node2)

    def test_url_different(self):
        node = TextNode("Test", TextType.LINK, "https://www.test1.com")
        node2 = TextNode("Test", TextType.LINK, "https://www.test2.com")
        self.assertNotEqual(node, node2)

    def test_none_properties(self):
        node = TextNode("Test", TextType.TEXT)
        node2 = TextNode("Test", TextType.TEXT, None) 
        self.assertEqual(node, node2)
        node.url = None
        node2.url = "https://test.com"
        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()