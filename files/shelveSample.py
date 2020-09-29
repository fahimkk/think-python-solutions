import shelve
db = shelve.open('selvesample.db')
db['cat'] = 'cat name is puppy'
db['dog'] = 'dog name is caaat'

print(db['cat'])
for key in db:
    print(key)
print(list(db.values()))
print(list(db.keys()))
print(list(db.items()))
