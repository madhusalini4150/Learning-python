#Join Sets-
#>>Union()-The union() and update() methods joins all items from both sets.The union() method returns a new set with all items from both sets.
set1={"a","b","c"}
set2={1,2,3}
sets=set1.union(set2)
print(sets)
#You can use the | operator instead of the union() method, and you will get the same result.
sets=set1|set2
print(sets)
#Join Multiple sets
set3={True,False}
set4={"Jhon","Elena"}
sets=set1.union(set2,set3,set4)
print(sets)
#When using the | operator, separate the sets with more | operators
sets=set1|set2|set3|set4
print(sets)
#Join a set and a tuple-
x={1,2,3,4}
y=(3,4,5,6,7,7,8)
z=x.union(y)
print(z)
#The  | operator only allows you to join sets with sets, and not with other data types like you can with the  union() method.
#The update() method inserts all items from one set into another.
#--The update() changes the original set, and does not return a new set.
#>>Update-The update() method inserts all items from one set into another.The update() changes the original set, and does not return a new set.
set1.update(set2)
print(set1)
#>>Intersection-Keep ONLY the duplicates,The intersection() method will return a new set, that only contains the items that are present in both sets.
a={1,2,3,4,5,6}
b={4,3,6,72,8,9}
c=a.intersection(b)
print(c)
#You can use the & operator instead of the intersection() method, and you will get the same result.
c=a&b
print(c)
#The & operator only allows you to join sets with sets, and not with other data types like you can with the intersection() method.
#The intersection_update() method will also keep ONLY the duplicates, but it will change the original set instead of returning a new set
a.intersection_update(b)
print(a)
#The values True and 1 are considered the same value. The same goes for False and 0.
set1={"apple",1,"banana","cherry",0}
set2={False,True,1,"blue"}
set1.intersection(set2)
print(set1)
#>>Difference-The difference() method will return a new set that will contain only the items from the first set that are not present in the other set.
set4=set1.difference(set2)
print(set4)
#You can use the - operator instead of the difference() method, and you will get the same result
set5=set1-set2
print(set5)
#>>Symmetric Differences-The symmetric_difference() method will keep only the elements that are NOT present in both sets.
set6=set1.symmetric_difference(set2)
print(set6)
#You can use the ^ operator instead of the symmetric_difference() method, and you will get the same result.
set0=set1^set2
print(set0)
#---------------------------------------------------------------------------------------------------------------------------------------------------------------
#FROZENSET-frozenset is an immutable version of a set.
#Use the frozenset() constructor to create a frozenset from any iterable.
x=frozenset({"blue","pink","yellow"})
print(x)
print(type(x))
#METHODS-
#Copy()-Returns a shallow copy
fs=frozenset({1,2,3,4})
x=fs.copy()
print(fs)
print(x)
#Difference()-Returns a new frozenset with the difference
fs1=frozenset({1,2,3,4})
fs2=frozenset({4,5,6,7,2})
fs3=frozenset({8,9,10})
diff=fs1.difference(fs2)
print(diff)
print(fs1-fs2)
#Intersection()-Returns a new frozenset with the intersection
insec=fs1.intersection(fs2)
print(insec)
print(fs1&fs2)
#isdisjoint()-Returns whether two frozensets have an intersection
print(fs1.isdisjoint(fs2))
print(fs1.isdisjoint(fs3))
#issubset()-Returns True if this frozenset is a (proper) subset of another
print(fs1.issubset(fs2))
#superset()-Returns True if this frozenset is a (proper) superset of another
print(fs1.issuperset(fs2))
#Symmetric_difference()-Returns a new frozenset with the symmetric differences
sydif=fs1.symmetric_difference(fs2)
print(sydif)
#Union()-Returns a new frozenset containing the union
un=fs1.union(fs2)
print(un)
