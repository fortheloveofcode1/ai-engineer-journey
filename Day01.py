print('Day 1 : AI journey')
def count_numbers(numbers):
    count = {}
    for number in numbers :
        if number in count:
            count[number] +=1
        else:
            count[number]=1
    return count

numbers = [2,5,2,8,5,2,10]  
result = count_numbers(numbers)
print(result)   

def most_frequent(numbers):
    count = {}
    highest_count = 0
    most_common = None
    for number in numbers:
        if number in count:
            count[number] += 1
        else:
            count[number] = 1
    
    for number in count:
        if count[number] > highest_count:
            highest_count = count[number]
            most_common = number

    return most_common
numbers = [4, 7, 4, 9, 7, 4, 9, 9, 9]

frequent = most_frequent(numbers)
print(frequent)

def two_sum(nums, target):
    seen = {}
    for index,number in enumerate(nums):
        needed = target - number
        if needed in seen:
            return [seen[needed],index]
        else:
            seen[number] = index
    
    

nums=[2,6,7,6,7,11,15]
target=9
print(two_sum(nums,target))
nums=[3,2,4]
target = 6
print(two_sum(nums,target))
            
        




