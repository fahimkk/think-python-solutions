class LinearMap(object):
    def __init__(self):
        self.items =[]
    def add(self, k, v):
        self.items.append((k, v))
    def get(self, k):
        for key, val in self.items:
            if key == k: 
                return val
        raise KeyError


class BetterMap(object):
    def __init__(self, n=100): 
       self.maps = []
       for i in range(n):
           # all the elements of the list became LinearMap objects.
           self.maps.append(LinearMap())
    def find_map(self, k):
        # hash funtion used to convert the k to a specific number which is uniq 
        # and when takine mod by len we get the num from zero to len.
        index = hash(k) % len(self.maps)
        # self.maps is a list, in which elements are LinearMap objects.
        return self.maps[index]
    def add (self, k, v):
        m = self.find_map(k)
        # where m is a LinearMap object of index hask(k)
        m.add(k, v)
    def get (self, k):
        m = self.find_map(k)
        return m.get(k)

cllg_frnds = LinearMap()
cllg_frnds.add('shahad', 28)
shl_frnd = BetterMap()
hm_cozn = BetterMap()
hm_cozn.add('shameen',30)
shl_frnd.add('shameen',29)
cllg_frnds.add('shameen', 27)
print(shl_frnd.get('shameen'))
print(hm_cozn.get('shameen'))

class HashMap(object):
    def __init__(self):
        self.maps = BetterMap(2)
        self.num = 0
    def get(self, k):
        return self.maps.get(k)
    def add(self, k, v):
        if self.num == len(self.maps.maps):
            self.resize()
        self.maps.add(k,v) 
        self.num +=1

    def resize(self):
        new_maps = BetterMap(self.num * 2)
        for m in self.maps.maps:
            for k,v in m.items:
                new_maps.add(k,v)
        self.maps = new_maps
