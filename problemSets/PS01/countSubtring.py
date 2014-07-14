         
         
# Paste your code into this box 

def equal_string(my_string,sub_string):
    return my_string == sub_string
    
    
s = 'foboboboobjobobobooobobobbbobooeoboyt'
count = 0
sub_string = 'bob'
sub_string_length = len(sub_string)
s_length = len(s)
s_start_index = 0
while s_length - s_start_index >= sub_string_length:
    # both if implementation is ok
    if equal_string(s[s_start_index:s_start_index+3], sub_string):
    # if s[s_start_index:s_start_index+3] == sub_string:
        count += 1
    s_start_index += 1 
print ('Number of times bob occurs is: ' + str(count))