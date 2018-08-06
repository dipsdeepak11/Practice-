#program to demostrate various common method in python list

list1=[1,2,3,4,5,6,7,44]
list2=[12,23,42,44,5,5555,7]
list3=["a","hello","world",1]


#append is use to add
list1.append(55)
print("new list1 is %s"%list1)

#insert a element at specified position
list2.insert(2,100)
print("new list2 is %s"%list2)

#extend adds the content of list3 in list1
list1.extend(list3)
print("new list1 is %s"%list1)

# calcluate sum of elements of list
if int and str in list2:
    print("Not supported")
else:
    temp=sum(list2)
    print("sum of list2 is %d"%temp)

#count - count the occurence of a input elemet
    print("The total occurence of 1 in list1 is %d"%list1.count(1))

#return the index of first occurence of input element
    print("The first occurence of 3 is list1 is %d"%list1.index(3))

#sort - it will sort the list in increasing or decreasing order
    list2.sort(reverse=True)
    print("The asc sorted list2 is %s"%list2)

#remove the element from the list
    list2.remove(23)
    print("New list2 after 23 removal is %s"%list2)

#pop- remove based on the index provided
    list2.pop(2)
    print("new list is %s"%list2)






