#anil

class Node():
    '''A container for nodes'''

    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList():
    '''ADT for LinkedList'''

    def __init__(self,data=None):
        self.head = Node(data)

    def insertBeg(self,data):
        if self.head.data is None:
            self.head.data = data
        else:
            newNode = Node(data)
            newNode.next = self.head
            self.head = newNode

    def insertEnd(self,data):
        if self.head.data is None:
            self.head.data = data
        else:
            newNode = Node(data)
            ptrNode = self.head
            while ptrNode.next is not None:
                ptrNode = ptrNode.next
            ptrNode.next = newNode

    def delete(self,data):
        if self.head.data is None:
            print("LinkedList is already empty")
        elif self.head.data == data:
            tempNode = self.head
            self.head = self.head.next
            del(tempNode)
        else:
            ptrNode = self.head.next
            preptrNode = self.head
            while ptrNode.data != data:
                preptrNode = ptrNode
                ptrNode = ptrNode.next
            preptrNode.next = ptrNode.next
            del(ptrNode)


    def __str__(self):
        ptrNode = self.head
        tmp = []
        while ptrNode is not None:
            tmp.append(ptrNode.data)
            ptrNode = ptrNode.next
        return str(tmp)

print("Linked List")
l = LinkedList()
ch = 0
while ch != 5:
    ch = int(input("\n1. Insert at Begining\n2. Insert at End\n3. Print the linked list\n4. Delete a node\n5. Exit\nEnter your choice: "))
    if ch == 1:
        l.insertBeg(int(input("Enter data: ")))
    elif ch == 2:
        l.insertEnd(int(input("Enter data: ")))
    elif ch == 3:
        print(l)
    elif ch == 4:
        l.delete(int(input("Enter data: ")))
