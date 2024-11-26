from textnode import TextNode, TextType

def main():
    node =  TextNode(
        text = "Hello", 
        text_type = TextType.ITALIC
    )
    print(node)

if __name__ == "__main__":
    main()