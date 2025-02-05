class Node(object):
    def __init__(self, data, next_pointer = None):
        self.data = data
        self.next_pointer = next_pointer
    
    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data

    def get_next_pointer(self):
        return self.next_pointer

    def set_next_pointer(self, next_pointer):
        self.next_pointer = next_pointer

class LinkedList(object): 
    def __init__(self):                                # initialize the linked list,
        self.head_pointer = None                       # when initialized, the head pointer will point to nothing since linked list will be empty 
    
    def add_to_start(self, data): 
        if self.head_pointer == None:                  # if list is empty
            new_node = Node(data)                      # make a new node by passing data to it, its next_pointer will point to None by default(see above)
            self.head_pointer = new_node               # make the head pointer point to the new node      

        else:                                          # if list is not empty
            new_node = Node(data, self.head_pointer)   # make new node by passing the data and making its next pointer point to what the head_pointer was pointing to
            self.head_pointer = new_node               # make the head pointer point to the new node

    def add_to_end(self, data):                        # add to end without a tail pointer
        new_node = Node(data)

        if self.head_pointer is None:  # If the list is empty
            self.head_pointer = new_node
            return
        
        current_node = self.head_pointer                       # start from the node at the beginning
        while current_node.next_pointer:               # traverse the list until the node's next pointer points to None (meaning last node has reached)
            current_node = current_node.next_pointer              # get to the last_node and save it 
        
        current_node.next_pointer = new_node              # make the pointer of the last node point to the new node

    def add_to_middle(self, data, position):  
        if position == 0:  # If inserting at the start
            self.add_to_start(data)
            return  

        new_node = Node(data)  
        current_node = self.head_pointer  
        count = 0  

        while current_node is not None and count < position - 1:  
            current_node = current_node.next_pointer  
            count += 1  

        if current_node is None:  # If position is out of bounds
            print("Position out of bounds")
            return  

        new_node.next_pointer = current_node.next_pointer  
        current_node.next_pointer = new_node 
        

    def delete(self, key):
        if self.head_pointer is None:  # If the list is empty
            print("List is empty")
            return 
        
        if self.head_pointer.data == key:  # If the key is in the first node
            self.head_pointer = self.head_pointer.next_pointer  
            return  

        current_node = self.head_pointer
        while current_node.next_pointer is not None and current_node.next_pointer.data != key:  
            current_node = current_node.next_pointer  

        if current_node.next_pointer is None:  # If key is not found
            print("Key not found")
            return
        
        current_node.next_pointer = current_node.next_pointer.next_pointer  # Bypass the node with the key

    