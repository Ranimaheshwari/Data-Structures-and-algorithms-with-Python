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

    def print_detail(self):
        if self.head == None:
            print("LL is empty")
        
        itr = self.head
        llstr = ''
        while itr:
            llstr += f"[{itr.prev}, {itr.data}, {itr.next}] ---> "
            itr =  itr.next
        
        print(llstr[:-5])

    def print_backwords(self):
        if self.head == None:
            print("LL is empty")

        # get last node
        last_node = self.head
        while last_node.next:
            last_node = last_node.next

        itr = last_node
        llstr = ''
        while itr:
            print(itr.data)
            llstr += f"{itr.data} ---> "
            itr = itr.prev

        print(llstr[:-5])


    def insert_at_beg(self, data):
        if self.head is None:
            self.head = Node(None, data, None)
            return
        
        prev_head = self.head
        self.head = Node(None, data, self.head)
        prev_head.prev = self.head

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
            self.insert_at_beg(data)
            return
        
        itr, count = self.head, 0
        while itr:
            if count == index - 1:
                node = Node(itr, data, itr.next)
                if itr.next:
                    itr.next.prev = node
                itr.next = node
                break
            itr = itr.next
            count+=1

    def remove_at_index(self, index):
        if index<0 or index > self.get_length():
            print("Invalid index")
            return
        
        elif index == 0:
            self.remove_at_beg()
            return
        
        itr, count = self.head, 0
        while count < self.get_length():
            if count == index - 1:
                itr.next.prev = itr
                itr.next = itr.next.next
                break
            itr=itr.next
            count+=1

      

dl = DoublyLL()

dl.print_ll()
# dl.print_detail()
dl.insert_at_beg(1)
dl.print_ll()
dl.print_detail()
print()

dl.insert_at_beg(2)
dl.print_ll()
dl.print_detail()
print()

dl.insert_at_beg(3)
dl.print_ll()
dl.print_detail()
print()

dl.insert_at_end(4)
dl.print_ll()
dl.print_detail()
print()

dl.insert_at_index(2, 5)
dl.print_ll()
dl.print_detail()
print()

# dl.remove_at_beg()
# dl.print_ll()

# dl.remove_at_end()
# dl.print_ll()

# dl.remove_at_index(20)
# dl.print_ll()
# dl.print_detail()

dl.print_backwords()

