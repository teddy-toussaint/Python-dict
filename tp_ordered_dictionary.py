'''
Created on December 12th 2016
dictionary 
@author: ttoussaint
'''

class OrderedDictionary():

    # Constructor
    def __init__(self, *args, **kwargs):
        # Attributes
        self.keys = []
        self.vals = []
        
        # 1 argument => it's a dictionary
        if len(args) == 1:
            for k, v in dict(args[0]).items():
                self.add(k, v)
        # several named arguments forming a dictionnary
        elif len(kwargs) > 0:
            for k, v in dict(kwargs).items():
                self.add(k, v)
    
    # Representation
    def __repr__(self):
        res = str()
        if len(self.keys) == 0:
            res = "Empty dictionary\n"
        else:
            my_len = len(self.keys)
            res = "{"
            res = res + "{}: {}, ".format(self.keys[0], self.vals[0])
            for i in range(1, my_len-1):
                res = res +"{}: {}, ".format(self.keys[i], self.vals[i])
            res = res + "{}: {}".format(self.keys[my_len-1], self.vals[my_len-1])
            res = res + "}.\n"
        return res
    
    # Item getter
    def __getitem__(self, key):
        return self.vals[self.i_finder(key)]
    
    # Delete item
    def __delitem__(self, key):
        i = self.i_finder(key)
        del self.keys[i]
        del self.vals[i]
    
    # Item setter
    def __setitem__(self, key, val):
        i = self.i_finder(key)
        if i == -1:
            self.add(key, val)
        else:
            self.vals[i] = val
    # Tuple adder
    def add(self, key, val):
        self.keys.append(key)
        self.vals.append(val)
        
    # Check content
    def __contains__(self, key):
        i = self.i_finder(key)
        if i == -1:
            return False
        else:
            return True
    
    # Length
    def __len__(self):
        return len(self.keys)
    
    ## Sorting
    def sort(self):
        resK = []
        resV = []
        my_len = len(self.keys)
        mini = self.keys[0]
        for j in range(my_len):
            for i in range(my_len):
                if (self.keys[i] < mini) and (self.keys[i] not in resK):
                    mini = self.keys[i]
            resK.append(mini)
            resV.append(self.vals[(self.i_finder(mini))])
            #change value of 'mini'
            for i in range(my_len):
                if self.keys[i] != mini:
                    mini = self.keys[i]
                    print(mini)
                    break
        self.keys = resK
        self.vals = resV
        
    ## Reversing
    def reverse(self):
        resK = []
        resV = []
        my_len = len(self.keys)
        for i in range(my_len):
            resK.append(self.keys[my_len-1-i])
            resV.append(self.vals[my_len-1-i])
        self.keys = resK
        self.vals = resV
    
    # Index finder
    def i_finder(self, key):
        if key in self.keys:
            for t in enumerate(self.keys):
                if t[1] == key:
                    return t[0]
        else:
            return -1
    
x = OrderedDictionary()
y = OrderedDictionary({0:"lol", 5:"mdr", 3:"XD", 4:"haha"})
z = OrderedDictionary(a = 18, b = 23, d = 38, g = 27, z = 42, f = 98, v = 37)
print(x, y, z)

# TEST
z.sort()
print(x, y, z)