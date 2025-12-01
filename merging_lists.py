def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    return merge(merge_sort(left_half), merge_sort(right_half))

def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    # Спочатку об'єднайте менші елементи
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index+=1

    # Якщо в лівій або правій половині залишилися елементи, 
		# додайте їх до результату
    
    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged


# to merge each list from the list of lists with the next list. Merge newly created llist with the next i list of lists..
def merge_k_lists(lst_sort):
    merged=[]
    for i in range(len(lst_sort)):
        merged=merge(merged,lst_sort[i])
    return merged

def main():
    lst=[[1,2,6],[4,6,7,9],[1,4,6,18],[2,4,7,25]]
    print(merge_k_lists(lst))

if __name__=="__main__":
    main()