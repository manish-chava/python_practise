# Lists - Ordered, changable, duplicates
names = ["manish",1,"chava","aditya","ravi teja"]
names.append("srinivas")
#print(f'names after `append`: {names}')

names.insert(2,"padma")
#print(f'names after using `insert`: {names}')

ages = [24,"NA",24,32,35]
names.extend(ages)
#print(names)

# Dictionaries - ordered, changable, no duplicates
# Does not allow duplicates
# Alows to change the keys and values.
# Dictionaries are ordered.
# Adding elements - update()
# Removing elements - pop, del, popitem

my_dict ={
    "manish": 24,
    "srinivas": 42,
    "padma": 44,
    "aditya": 33,
    "ravi teja": 35
}
#print(list(my_dict.items()))

# Tuples - ordered, unchangable, duplicates
my_tuple = ("manish",1,"chava")
first_name,age,last_name = my_tuple
#print(first_name)

# Set unchangable, no duplicates, no order
# In sets True and 1 are considered the same.

# Slicing
myname = "manishchava"
mynumvers=[1,2,3,4,5,6,7,8,9,10]
print(mynumvers[-6:])

