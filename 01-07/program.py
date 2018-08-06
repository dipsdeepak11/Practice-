#program to find input variable type and than add to the respective type of list

int_list=[]
string_list=[]

def add_list_int(user_input):
    int_list.append(user_input)
    

def add_list_string(user_input):
    string_list.append(user_input)

#main program

input_list=[1,2,3,"hello","world",34,"deepak"]

for item in input_list:
    if type(item) is int:
        add_list_int(item)
    else:
        add_list_string(item)

print("At the end, the int list is %s and string list is %s" %(int_list,string_list))


