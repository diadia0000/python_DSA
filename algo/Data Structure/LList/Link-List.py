class Node:
    def __init__(self):
        self.val = None
        self.next = None


def insert(head, new_data, index):
    if index < 0 or index > length(head):
        print("Index out of range")
        return head
    new_node = Node()
    new_node.val = new_data
    if index == 0:
        new_node.next = head
        return new_node
    temp = head
    for _ in range(index - 1):
        temp = temp.next
    new_node.next = temp.next
    temp.next = new_node
    return head


def printList(head):
    while head:
        print(head.val, end=" ")
        head = head.next
    print()


def delete(head):
    print("delete node: %d" % head.val)
    if head is None:
        # 如果Link-List為空
        return None
    head = head.next
    return head


def deleteNode(head, node):
    print("delete node: %d" % node)
    # if the Link-List is Empty
    if head is None:
        return None
    # if the node is the Link-List's first node
    if head.val == node:
        head = head.next
        return head
    temp = head
    while temp.next is not None and temp.next.val != node:
        temp = temp.next
    if temp.next is None:
        print("Key Error: No such node")
        return head
    # if the node is in the middle or tail of the Link-List
    temp.next = temp.next.next
    return head


def append(head, new_data):
    if head.val is None:
        head.val = new_data
    else:
        new_node = Node()
        new_node.val = new_data
        while head.next is not None:
            head = head.next
        head.next = new_node
    return head


def length(head):
    count = 0
    while head is not None:
        count += 1
        head = head.next
    return count


def reverse_linked_list(head):
    prev = None
    current = head
    while current is not None:
        next_node = current.next  # 儲存下一個節點
        current.next = prev  # 反轉鏈接
        prev = current  # 將 prev 移動到當前節點
        current = next_node  # 移動到下一個節點
    return prev  # 返回新的鏈表頭


my_head = Node()
for i in range(0, 110, 10):
    append(my_head, i)
printList(my_head)
my_head = deleteNode(my_head, 30)
printList(my_head)

my_head = delete(my_head)
printList(my_head)
my_head = deleteNode(my_head, 90)
printList(my_head)
append(my_head, 101)
printList(my_head)
insert(my_head, -1, 3)
printList(my_head)
