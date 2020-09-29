import dbm, pickle
# The pickle module can help. It translates almost any type of object into a string 
# suitable for storage in a database, and then translates strings back into objects 

db = dbm.open('pickData.db','c')
t = [1,2,3]
db['L1']= pickle.dumps(t)
# pickle.dumps takes an object as a parameter and returns a string representation
# (dumps is short for “dump string”):
print(db['L1'])

# The format isn’t obvious to human readers; it is meant to be easy for pickle to interpret. 
#pickle.loads (“load string”) reconstitutes the object#
print(pickle.loads(db['L1']))
db.close()

print('----')

example_dict = {1:'6',2:'2',3:'f'}
pickle_out = open("dict.pickle",'wb')
pickle.dump(example_dict,pickle_out)
pickle_out.close()

pickle_in = open('dict.pickle','rb')
ex_dict = pickle.load(pickle_in)
print(ex_dict)
