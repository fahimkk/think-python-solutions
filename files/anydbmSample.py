import dbm 

db = dbm.open('caption.dp','c')
# c means that databse should be created if doesnt exists

db['cleese.png']='photo of john cleese.'
print(db['cleese.png'])

db['cat']= 'cat name is puppy'
print(db['cat'])

print(db.keys())
print(type(db['cat']))


