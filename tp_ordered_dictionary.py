'''
Created on December 12th 2016
Ordered Dictionary 
@author: ttous
'''

# Ordered dictionary
class OrderedDictionary:

    # Constructor
    def __init__(self, *args, **kwargs):
        # Attributes
        self.ks = []
        self.vs = []
        
        # 1 argument => it's a dictionary
        if len(args) == 1:
            for k, v in dict(args[0]).items():
                self.add(k, v)
        # several named arguments forming a dictionnary
        elif len(kwargs) > 0:
            for k, v in dict(kwargs).items():
                self.add(k, v)
    
    # Representation : displays as "{key1: val1, key2: val2, ...}"
    def __repr__(self):
        res = str()
        if len(self.ks) == 0:
            res = "{}"
        else:
            my_len = len(self.ks)
            res = "{"
            res += "{}: {}, ".format(self.ks[0], self.vs[0])
            for i in range(1, my_len-1):
                res += "{}: {}, ".format(self.ks[i], self.vs[i])
            res += "{}: {}".format(self.ks[my_len-1],
                                   self.vs[my_len-1])
            res += "}"
        return res
    
    # Item getter
    def __getitem__(self, key):
        return self.vs[self.i_finder(key)]
    
    # Delete item
    def __delitem__(self, key):
        i = self.i_finder(key)
        del self.ks[i]
        del self.vs[i]
    
    # Item setter
    def __setitem__(self, key, val):
        i = self.i_finder(key)
        if i == -1:
            self.add(key, val)
        else:
            self.vs[i] = val
    # Tuple adder
    def add(self, key, val):
        self.ks.append(key)
        self.vs.append(val)
        
    # Check content
    def __contains__(self, key):
        return key in self.ks
    
    # Length
    def __len__(self):
        return len(self.ks)
    
    # Iteration
    def __iter__(self):
        return iter(self.ks)
    
    # Adds 2 ordered dictionary together
    def __add__(self, dico):
        res = OrderedDictionary()
        # Adds the 1st one to the result
        for t1 in self.items():
            res.add(t1[0], t1[1])
        # Adds the 2nd one to the result
        for t2 in dico.items():
            res.add(t2[0], t2[1])
        return res
    
    # Sorts according to the keys
    def sort(self):
        resK = []
        resV = []
        my_len = len(self.ks)
        mini = self.ks[0]
        for j in range(my_len):
            for i in range(my_len):
                if (self.ks[i] < mini) and (self.ks[i] not in resK):
                    mini = self.ks[i]
            resK.append(mini)
            resV.append(self.vs[(self.i_finder(mini))])
            for i in range(my_len):
                if (self.ks[i] != mini) and (self.ks[i] not in resK):
                    mini = self.ks[i]
                    break
        self.ks = resK
        self.vs = resV
        
    # Reverses the order of the keys
    def reverse(self):
        resK = []
        resV = []
        my_len = len(self.ks)
        for i in range(my_len):
            resK.append(self.ks[my_len-1-i])
            resV.append(self.vs[my_len-1-i])
        self.ks = resK
        self.vs = resV
        
    # Returns the keys
    def keys(self):
        return self.ks
        
    # Returns the values
    def values(self):
        return self.vs
        
    # Returns both the keys and the values as tuples
    def items(self):
        res = []
        for i in range(len(self.ks)):
            # Creates the i'th tuple and adds it to the list
            t = self.ks[i], self.vs[i]
            res.append(t)
        return res
    
    # Index finder
    def i_finder(self, key):
        if key in self.ks:
            for t in enumerate(self.ks):
                if t[1] == key:
                    return t[0]
        else:
            return -1
