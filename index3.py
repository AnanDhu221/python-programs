string=input("enter the string")
print("orginal string",string)
first_char=string[0]
lenght=len(string)
middle_index=int(lenght/2)
middle_char=string[middle_index]
last_char=string[-1]
new_string=first_char+middle_char+last_char
print("new string",new_string)