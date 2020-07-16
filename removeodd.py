num=[7,8,120,25,44,20,27]
print("Original List: ",num)
for x in num:
    if x%2!=0:
        num.remove(x)
print("List after removing odd numbers: ",num)    
