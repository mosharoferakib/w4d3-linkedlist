from Node import Node

class Add_list_elements:
    def __init__(self):
        self.head = None

    def add_node(self, value):
        node = Node(value)
        if not self.head:
            self.head = node
        else:
            current_node = self.head
            while current_node.right:
                current_node = current_node.right
            current_node.right = node

    def add_list_elements(self, lst):
        for element in lst:
            self.add_node(element)

linked_list = Add_list_elements()
linked_list.add_list_elements(["Friday", "Saturday", "Sunday"])

current_node = linked_list.head
while current_node:
    print(current_node.value)
    current_node = current_node.right