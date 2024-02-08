class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_first(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_last(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def insert_at_position(self, data, position):
        if position < 0:
            print("Invalid position")
            return

        if position == 0:
            self.insert_at_first(data)
            return

        new_node = Node(data)
        current = self.head
        for _ in range(position - 1):
            if not current:
                print("Position out of bounds")
                return
            current = current.next

        new_node.next = current.next
        current.next = new_node

    def delete_at_first(self):
        if self.head:
            self.head = self.head.next

    def delete_at_last(self):
        if not self.head or not self.head.next:
            self.head = None
            return

        current = self.head
        while current.next.next:
            current = current.next
        current.next = None

    def delete_at_position(self, position):
        if position < 0:
            print("Invalid position")
            return

        if position == 0:
            self.delete_at_first()
            return

        current = self.head
        for _ in range(position - 1):
            if not current or not current.next:
                print("Position out of bounds")
                return
            current = current.next

        current.next = current.next.next

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def iterate(self):
        current = self.head
        while current:
            yield current.data
            current = current.next

    def recursive_display(self, node):
        if node:
            print(node.data, end=" -> ")
            self.recursive_display(node.next)
        else:
            print("None")


# Example Usage:
linked_list = LinkedList()

linked_list.insert_at_first(3)
linked_list.insert_at_first(2)
linked_list.insert_at_first(1)

linked_list.insert_at_last(4)
linked_list.insert_at_last(5)

linked_list.insert_at_position(10, 2)

print("Original Linked List:")
linked_list.display()

linked_list.delete_at_first()
linked_list.delete_at_last()
linked_list.delete_at_position(2)

print("\nLinked List after deletion:")
linked_list.display()

linked_list.reverse()

print("\nLinked List after reversal:")
linked_list.display()

print("\nLinked List Iteration:")
for item in linked_list.iterate():
    print(item, end=" ")

print("\n\nLinked List Recursive Display:")
linked_list.recursive_display(linked_list.head)
