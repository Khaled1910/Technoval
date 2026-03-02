def split_list (num):
    if len(num) <= 1:
        return num
    mid = len(num) // 2
    left_side = num[:mid]
    right_side = num[mid:]
    sorted_left = split_list(left_side)
    sorted_right = split_list(right_side)
    return merge_sort(sorted_left,sorted_right)

def merge_sort(left,right):
    i=j=0
    result=[]
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i +=1
        else:
            result.append(right[j])
            j +=1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


numbers = [10,2,1,9,15,20]
print(split_list(numbers))