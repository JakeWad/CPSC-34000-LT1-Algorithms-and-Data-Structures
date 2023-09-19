#Node class with data and link part of a node in the linked list
class Node :
    def __init__(self, data) :
        self.data = data
        self.link = None
      
      
#linked list class containing a head of the linked list
class LinkedList :
    def __init__(self) :
        self.head = None  #stating node
    
    #display method for the linked list
    def display(self) :
        if self.head is None:
            print("List is empty")
            return
        else:
            print("\n[",end="")
            cur = self.head    #cur - current node
            while cur is not None:
                print(cur.data , end=" ")
                cur = cur.link
                
            print("]\n",end="")
         
    #add_head : add element at the head or staring of the linked list        
    def add_head(self,e) :
        new_node = Node(e)  #creating a new node
        new_node.link = self.head  #setting new_node link to head
        self.head = new_node  #changing head to new node
    
    #add_tail : add element at the end of the linked list
    def add_tail(self,e) :
        new_node = Node(e)  #new node
        #if head is None i.e. list is empty then change head to new node and return
        if self.head is None:
            self.head = new_node
            return
        #otherwise traverse the list upto the last element
        cur = self.head
        while(cur.link is not None) :
            cur = cur.link
        
        #then add the new node in the link of the last element in the linked list
        cur.link = new_node
      
      
    #find_3rd_to_last  : finds the 3rd element from the last of the linked list   
    def find_3rd_to_last(self) :
        #if list size is less than 3 then return None
        if self.head is None or self.head.link is None or self.head.link.link is None :
            return None
        
        #otherwise point to the first and the 3rd element in the list
        pointerA = self.head; #first element
        pointerB = self.head.link.link #third element from the starting
        
        #traverse till pointerB reaches the end of the list 
        #then pointerA  will be pointing to the 3rd last element in the list
        while(pointerB.link is not None) :
            pointerA = pointerA.link
            pointerB = pointerB.link
        
        return pointerA
    
    #reverse : actual reverse of the liked list
    def reverse(self) :
        #if array size is <= 1 then return the head
        if self.head is None or self.head.link is None :
            return self.head
        
        #otherwise take three nodes prvious, current, next
        prev_node = self.head
        cur_node = prev_node.link
        next_node = cur_node.link
        self.head.link = None  #make the head point to None at starting
        
        while(cur_node is not None ) :
            cur_node.link = prev_node   #current.link = previous
            prev_node = cur_node        #previous = current
            cur_node = next_node        #current = next
            if next_node is not None :  #next = next.link
                next_node = next_node.link
        
        #  head->1->2->3->4->5->None
        #  None<-1<-2<-3<-4<-5<-head
        self.head = prev_node  #previous will be having the last node at the end so head will be replaced by the previous
        
        
#main program    
#using this linked list in the program
linked_list = LinkedList()
linked_list.add_head(2)
linked_list.add_tail(3)
linked_list.add_tail(10)
linked_list.add_head(1)
linked_list.add_tail(20)
linked_list.add_tail(30)

print("Dispalying the created list")
linked_list.display()

#taking the 3rd element from the last in node
node = linked_list.find_3rd_to_last()
print("3rd to last element : ",node.data)  #print third element from the last
    
#applying the reverse method on the list
linked_list.reverse()
#displaying the list after reversing iter
print("After reverse  : ")
linked_list.display()
