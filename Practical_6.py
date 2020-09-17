#NAME    : Daniel Injeti
#ROLL_NO : 4063
#CLASS   : SYCS 
a = str(input("enter the string i for insertion sort , b for bubble sort , s for selection sort : "))
nums = [54,56,72,5,3,0,25,56,88,-1,13]
if a=='i':
    #list = [54,56,72,5,3,0,25,56,88,-1,13]
    for i  in range(1,len(nums)):
        currentvalue = nums[i]
        position = i
        while(position>0 and nums[position-1] > currentvalue):
            nums[position] = nums[position-1]
            position = position-1
    nums[position] = currentvalue
    print(nums)
elif a == 'b' :
    #nums = [5,3,6,8,9]
    def sort(nums):
        for i in range(len(nums)-1,0,-1):
            for j in range(i):
                if nums[j]>nums[j+1]:
                    temp = nums[j]
                    nums[j]=nums[j+1]
                    nums[j+1] = temp 
    sort(nums)
    print(nums)
elif a == 's':
    def sort(nums):
        for i in range(len(nums)):
            minpos = i
            for j in range(i,len(nums)):
                if nums[j] < nums[minpos]:
                    minpos=j
            temp = nums[i]
            nums[i] = nums[minpos]
            nums[minpos] =temp

    nums = [6,5,2,3,0]
    sort(nums)
    print(nums)
else:
    print("Enter valid input")
