# impliment stack
stack = []
stack.append(10)
stack.append(20)
stack.append(30)
print("Stack is: ",stack)
stack.pop()
print("Stack",stack)
stack.pop()
stack.pop()
print(len(stack)==0)
# impliment queue
queue = []
queue.append(40)
queue.append(50)
queue.append(60)
print("Queue is:",queue)
queue.pop(-1)
print("Queue",queue)
queue.pop(-1)
queue.pop(-1)
print(queue)
#impliment binary search on arry
array = []
n=int(input("Enter range of array:"))
for i in range(n):
    num=int(input("Enter array value:"))
    array.append(num)
print("Array is: ",array)
array.sort()
print("Sorted Array:",array)
target=int(input("Enter value to search:"))
low=0
high=len(array)-1
while low<=high:
    mid=(low+high)//2
    if array[mid]==target:
        print("Element found at :",mid)
        break
    elif array[mid]<target:
        low=mid+1
    elif array[mid]>target:
        high=mid-1
    else:
        print("Element not found")