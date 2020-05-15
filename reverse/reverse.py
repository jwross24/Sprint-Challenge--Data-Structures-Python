class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev):
        # If the list is empty, do nothing
        if not self.head:
            return
        # If we're at the last node, set it to the head
        if not node.get_next():
            self.head = node

            # Set the next node to the previous node
            node.set_next(prev)
            return

        # Save the current node's next
        new_next = node.get_next()

        # Set the next node to the previous node
        node.set_next(prev)
        self.reverse_list(new_next, node)
