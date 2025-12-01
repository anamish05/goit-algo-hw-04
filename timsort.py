# Comparison of merge sort, insertion sort and timsort algorithms
import timeit
import random


# decorator for time measuring
def calc_time(func, data):
    start=timeit.default_timer()
    sorted_data=func(data[:])
    final=timeit.default_timer() - start
    return final


# Merge sort
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
            right_index += 1

    # Якщо в лівій або правій половині залишилися елементи, 
		# додайте їх до результату
    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    return merge(merge_sort(left_half), merge_sort(right_half))


# Insertion sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j] :
                arr[j+1] = arr[j]
                j -= 1
        arr[j+1] = key 
    return arr


def main():
    # data sets
    data={
        1:[random.randint(1, 1000) for _ in range(300)], 
        2:[random.randint(-5000, 1000) for _ in range(500)], 
        3:[random.randint(1000, 10000) for _ in range(1000)]
    }

    algoritms=[merge_sort, insertion_sort, sorted]   # list of sorting functions

    # for each dataset measure time of sort functions and calculate min time of calc and the function name that it calculated
    for key, lst in data.items():
        times=[]
        print(f"Measuring for list {key}:")
        for alg in algoritms:
            time=calc_time(alg, lst)
            print(f"For function {alg.__name__} sorting time is {time}")
            times.append(time)
        print(f"The most time-efficient algoritm for list {key} is {algoritms[times.index(min(times))].__name__}")


if __name__=="__main__":
    main()


