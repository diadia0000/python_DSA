class node:
    def __init__(self):
        self.value = None
        self.next = None
        self.prev = None
def insert_node(t,x):
    t.next = x.next
    t.prev = x
    x.next = t
    x.next.prev = t
def delete_node(t,x):
    if t.value == x:
        x.prev.next = x.next
        x.next.prev = x.prev
