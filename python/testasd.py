arr = [1,2,3,4,5,6]
temp=arr[0]
for i in range(1,len(arr)):
    temp+=arr[i]
    arr[i]=temp
print(max(arr))