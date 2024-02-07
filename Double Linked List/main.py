class Node():
    def __init__(self,data,next,prev):
        self.data = data
        self.next = next
        self.prev = prev

class Double_Linked_List():
    def __init__(self):
        self.head = None
    
    def get_last_element(self):
        itr = self.head
        while itr.next:
            itr = itr.next
        return itr

    def add_at_start(self,data):
        node = Node(data,self.head,None)
        self.head = node

    def add_at_index(self,index: int,data: any):
        le = self.length()
        if 0>le or le<index:
            raise Exception('Index out of range!')
        
        if index == 0:
            self.add_at_start(data)

        if index == (le-1):
            self.add_at_end(data)

        itr = self.head
        counter = 1
        while itr:
            if counter == index:
                break
            counter += 1
            itr = itr.next
        itr.next = Node(data,itr.next,itr)

    def add_at_end(self,data):
        if self.head is None:
            self.add_at_start(data)
            return
        itr = self.get_last_element()
        itr.next = Node(data,None,itr)

    def remove_at_start(self):
        self.head = self.head.next

    def remove_at_index(self,index: int):
        le = self.length()
        if 0>le or le<index:
            raise Exception('Index out of range!')
        
        if index:
            itr = self.head
            counter = 1
            while itr:
                if counter == index:
                    break
                counter += 1
                itr = itr.next
            itr.next = itr.next.next
            return
        self.remove_at_start()
        
    def length(self):
        itr = self.head
        counter = 0
        while itr:
            counter += 1
            itr = itr.next
        return counter
    
    def print_list_forwards(self):
        if self.head is None:
            print('Empty List')
            return
        
        itr = self.head
        print(itr.data,end=' ')
        itr = itr.next
        while itr:
            print('-->',itr.data,end='')
            itr = itr.next
        print('\n')

    def print_list_backwards(self):
        if self.head is None:
            print('Empty List')
            return
        itr = self.get_last_element()
        print(itr.data,end=' ')
        itr = itr.prev
        while itr:
            print('-->',itr.data,end='')
            itr = itr.prev
        print('\n')
        
        
    
    def add_values_at_end(self,data :list):
        for i in data:
            self.add_at_end(i)


if __name__ == "__main__":
    Dll = Double_Linked_List()
    #Dll.print_list_forwards()
    Dll.add_at_start('Apple')
    Dll.add_at_end('Big Apple')
    Dll.add_at_end('Small Apple')
    Dll.add_at_end('Both Apple')
    Dll.add_at_index(2,'New Apple')
    Dll.print_list_forwards()
    #Dll.remove_at_start()
    Dll.remove_at_index(2)
    Dll.print_list_forwards()
    Dll.print_list_backwards()
    #Dll.add_values_at_end([2,44,9,764,4])
    #Dll.print_list_forwards()
    leng = Dll.length()
    print(leng)
