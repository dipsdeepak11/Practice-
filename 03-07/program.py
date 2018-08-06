#program to split the list in given no. of chunks

def split_list(input_list,input_chunk):
    start=0
    size=len(input_list)
    print("Total no. of chunks possible is %d"%size)
    for item in range(start,size,input_chunk):
        start=item
        print(input_list[start:start+input_chunk])


#main program
list1=[1,2,3,5,4,33,25,66,444,66]
chunks1=3
split_list(list1,chunks1)

list2=["a",12,11,"v",555,"dfff","223",33]
chunks2=4
split_list(list2,chunks2)
    
    
    
    
