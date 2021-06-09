# yield function
def firstYield():
    i =1
    yield i+1
    yield i+2
    yield i+3
    

firstYield()
for i in firstYield():
    print(i)
#next function
lst = iter(["hi","hello","hey"])
print(next(lst))
print(next(lst))
print(next(lst))

def simpleGeneratorFun():
    yield 1
    yield 2
    yield 3
   
# x is a generator object
x = simpleGeneratorFun()
  
# Iterating over the generator object using next
print(x.next()) # In Python 3, __next__()
print(x.next())
print(x.next())