 # Paste your code into this box 
s = 'aaabeuoi'
count = 0
for index in range(len(s)) :
    if s[index] == 'a' or s[index] == 'e' or \
    s[index] == 'i' or s[index] == 'o' or s[index] == 'u':
        count = count + 1
        
print('count is ' + str(count))

def a(x, y, z):
     if x:
         return y
     else:
         return z
         
