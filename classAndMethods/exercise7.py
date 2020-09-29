
class Kangaroo(object):
    def __init__(self, pouch_contents=[]):
        self.pouch_contents = pouch_contents

    def __str__ (self):       
        return f'{self.__class__.__name__}  pouch_contents:{self.pouch_contents}'
    def put_in_pouch(self, obj):
        if isinstance(obj, Kangaroo):
            self.pouch_contents.extend(obj.pouch_contents)
        elif isinstance(obj,list):
            self.pouch_contents.extend(obj)
        else:
            self.pouch_contents.append(obj)
    
kanga = Kangaroo(['fahim','adil'])
roo = Kangaroo(['34','98'])

print(kanga)
print(roo)

kanga.put_in_pouch(['fida'])
print(kanga)

kanga.put_in_pouch(roo)
print(kanga)