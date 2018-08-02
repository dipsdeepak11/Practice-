#program to find all palindrome numbers in a input list

def find_palindrome_in_list(input_list):
    counter=0
    palin_list=[]

    for item in input_list:
        #finding reverse of the current item
        temp=item
        reverse=0
        while temp > 0:
            reverse = reverse * 10 + temp %10
            temp=temp / 10
        #comparing reverse with the actual number
        if reverse == item:
            palin_list.append(item)
            counter = counter+1
    print("the count now is %D" ,counter)

    return palin_list,counter

def print_palindrome_list(palindrom_list):
    for item in palindrom_list:
        print("%d" , item)

#main program
list_first=[11,2321,12321,121,221,252]
palindrom_list,count = find_palindrome_in_list(list_first)
print_palindrome_list(palindrom_list)
print("total count in list first is ",count)
                
