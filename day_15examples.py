#sets==
it_companies={"Facebook","Google","Microsoft","Apple","IBM","Oracle","Amazon"}
A={19,22,24,20,24,25,26}
B={19,22,20,25,26,24,28,27}
ages=[22,19,24,25,26,24,25,24]
#>Find the length of the set it_companies
print(len(it_companies))
#>Add 'Twitter' to it_companies
it_companies.add("Twitter")
print(it_companies)
#>Insert multiple IT companies at once to the set it_companies
it_companies.update({"Infosys","TCS","Wipro"})
print(it_companies)
#>Remove one of the companies from the set it_companies
it_companies.remove("TCS")
#or it_companies.discard("TCS")
#>Join A and B
C=A.union(B)
print(C)
#C=A|B
#print(C)
#>Find A intersection B
C=A.intersection(B)
print(C)
#or
#C=A&B
#print(C)
#>Is A subset of B
print(A.issubset(B))
#>Are A and B disjoint sets
print(A.isdisjoint(B))
#>Join A with B and B with A
C=A.union(B)
print(A)
D=B.union(A)
print(D)
#>What is the symmetric difference between A and B
sys_diff=A.symmetric_difference(B)
print(sys_diff)
#Delete the sets completely
del A
del B
del it_companies
#Convert the ages to a set and compare the length of the list and the set, which one is bigger?
ages=[22,19,24,25,26,24,25,24]
print(ages)
myset=set(ages)
print(myset)
print("Length of List:",len(ages))
print("Length of set:",len(myset))
if len(ages)>len(myset):
    print("List is bigger")
elif len(ages)<len(myset):
    print("Set is Bigger")
else:
    print("Both are equal")
