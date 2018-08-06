#program to remove the duplicate from the list

def remove_duplicate(input_list):
    temp_list=[]
    for item in input_list:
        if item not in temp_list:
            temp_list.append(item)
    return temp_list


#main program
input_list=[1,3,44,33,3,4555,33]
out_list=remove_duplicate(input_list)
print("The output list is %s"%out_list)


input_list2=["a",23,"b",455,23,"a","fvv"]
out_list2=remove_duplicate(input_list2)
print("The second output list is %s"%out_list2)
