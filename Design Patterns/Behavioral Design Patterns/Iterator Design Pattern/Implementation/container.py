class Iterator:
    def has_next(self):
        pass
    
    def next(self):
        pass

class Container:
    def get_iterator(self):
        pass 

class CollectionOfNamesIterator(Iterator):
        def __init__(self, names):
            self.__i = 0
            self.__names = names
        
        def has_next(self):
            return self.__i < len(self.__names)
        
        def next(self):
            curr = None
            if self.has_next():
                curr = self.__names[self.__i]
                self.__i = self.__i + 1

            return curr

class CollectionOfNames(Container):
    def __init__(self):
        self.__names = []
       
    
    def get_iterator(self):
        return CollectionOfNamesIterator(self.__names)

    def add(self, element):
        self.__names.append(element)


arr = CollectionOfNames()

arr.add('Bimbisara')
arr.add('AjatuSetru')
arr.add('Dhanananda')
arr.add('Chandra Gupta Maurya')
arr.add('BinduSara')
arr.add('Ashoka')
arr.add('Brihadratha')
arr.add('Pushya Mitra Sunga')
arr.add('Kujula Kadphisis')
arr.add('Kanishka')
arr.add('Vimala Kudphesis')
arr.add('Chandra Gupta II')
arr.add('Samudra Gupta')
arr.add('Kumar Gupta')

iterator = arr.get_iterator()

while(iterator.has_next()):
    print(iterator.next())