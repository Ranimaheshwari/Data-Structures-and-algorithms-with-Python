class Node:
    def  __init__(self, prev=None, data=None, next=None):
        self.prev = prev
        self.data = data
        self.next = next

class DoublyLL:
    def __init__(self):
        self.head = None

    def print_ll(self):
        if self.head == None:
            print("LL is empty")
        
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + " ---> "
            itr =  itr.next

        print(llstr[:-5])

    def insert_at_beg(self, data):
        if self.head is None:
            self.head = Node(None, data, None)
            return
        self.head = Node(None, data, self.head)

    def remove_at_beg(self):
        if self.head is None:
            print("ll is empty")
            return
        self.head = self.head.next
    
    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(None, data, None)
            return
        
        itr = self.head
        while itr.next:
            itr =  itr.next
        
        itr.next = Node(itr, data, None)

    def remove_at_end(self):
        if self.head is None:
            print("ll is empty")
            return
        
        itr = self.head
        while itr.next:
            itr = itr.next

        itr.prev.next = None

    def insert_values(self, values_list):
        for data in values_list:
            self.inert_at_end(data)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count+=1
            itr = itr.next
        return count

    def insert_at_index(self, index, data):
        if index<0 or index > self.get_length():
            print("Invalid index")
            return
        
        elif index == 0:
            self.insert_at_beg(data )
        
        itr, count = self.head, 0
        while itr:
            if count == index - 1:
                itr.next = Node(itr, data, itr.next)
                itr.next.prev = itr
                break
            itr = itr.next
            count+=1

    def remove_at_index

    
        

dl = DoublyLL()

dl.print_ll()
dl.insert_at_beg(1)
dl.print_ll()
dl.insert_at_beg(2)
dl.print_ll()
dl.insert_at_beg(3)
dl.print_ll()

dl.insert_at_end(4)
dl.print_ll()

dl.insert_at_index(2, 5)
dl.print_ll()

dl.remove_at_beg()
dl.print_ll()

dl.remove_at_end()
dl.print_ll()

