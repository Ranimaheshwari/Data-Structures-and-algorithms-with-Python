class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def isempty(self):
        return True if self.head==None else False
    
    def print_ll(self):
        if self.isempty():
            print("hey! LL is empty..")
            return
        print("Your LL is ->")
        itr = self.head
        llstr = ""
        while itr:
            llstr += itr.data+" ---> "
            itr = itr.next
        print(llstr[:-5])

    def insert_at_begining(self, data):
        '''
        [1, next] -> [2, none]
          {HEAD} 
        o/p : [3, next] -> [1, next] -> [2, none]
                {HEAD}
        '''
        print(f"inserting '{data}' at begining:")
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        '''
        [1, next] -> [2, none]
          {HEAD} 
        o/p : [1, next] -> [2, next] - > [3, none]
                {HEAD}
        '''
        print(f"inserting '{data}' at end:")
        node = Node(data, None)
        if self.isempty():
            self.head = node
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        
        itr.next = node

    def insert_values(self, data_list):
        ''' insert data from a list in LL'''
        for i in data_list:
            self.insert_at_end(i)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count+=1
            itr = itr.next
        return count
    
    def remove_at_index(self, index):
        '''
        [1, next] -> [2, next] -> [3, next] -> [4, none]
        after removing at index 2:
        - stop at prev index and then point to next-> next
        [1, next] -> [2, next]-\      /--> [4, none] which is actually [3, ((next))]
                                \ _ _/
        '''
        if index<0 or index>self.get_length():
            return "INVALID INDEX!!!"
        
        elif index == 0:
            self.head = self.head.next
            return
        
        count, itr = 0, self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break

            itr = itr.next
            count += 1

    def insert_at_index(self, index, data):
        '''
        [1, next] -> [2,next] -> [3, none]
        insert at 1 index
        [1, next]--\           /--> [2,next] -> [3, none]
                    \[4, next]/
        '''
        if index<0 or index>self.get_length():
            print("Invalid index")
            return "INVALID INDEX!!!"
        
        elif index == 0:
            self.insert_at_begining(data)
            return
        count, itr = 0, self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break
            count+=1
            itr=itr.next

    def insert_after_value(self, data_after, data):
        '''
        [1, next]-> [2,next] -> [3, none]
        insert after 2:
        [1, next] -> [2, next] --\           /--> [3, none] 
                                  \[4, next]/  
        '''
        if self.isempty():
            print("List is empty")
            return
        
        if self.head.data == data_after:
            self.head.next = Node(data, self.head.next)
            return
        
        itr = self.head
        count = 0
        print(self.get_length())
        while count <= self.get_length():
            print(count, itr.data)
            if itr.data == data_after:
                itr.next = Node(data, itr.next)
                break
            itr= itr.next
            count+=1

        print("Data is not present in LL to insert after")



ll_obj = LinkedList()
ll_obj.print_ll()

# ll_obj.insert_at_begining(1)
# ll_obj.insert_at_begining(2)
# ll_obj.print_ll()

# ll_obj.insert_at_end(3)
# ll_obj.insert_at_end(4)
# ll_obj.insert_at_end(5)
# ll_obj.print_ll()

ll_obj.insert_values(['rani', 'jyoti', 'sawai'])
ll_obj.print_ll()

ll_obj.insert_after_value("sawai", "savita")
ll_obj.print_ll()

# ll_obj.remove_at_index(2)
# ll_obj.print_ll()

# ll_obj.insert_at_index(1, "savita")
# ll_obj.insert_at_index(3, "sawai")
# ll_obj.print_ll()



# print(ll_obj.get_length())




        