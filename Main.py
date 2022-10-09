from typing import List

def merge_sort(data) -> None:
    
    if len(data) > 1:
        mid = len(data)//2
        left_list = data[:mid]
        right_list = data[mid:]
    
        merge_sort(left_list)
        merge_sort(right_list)

        i=0
        j=0
        k=0

        while i<len(left_list) and j<len(right_list):
            if left_list[i] <= right_list[j]:
                data[k] = left_list[i]
                i=i+1
            
            else:
                data[k] = right_list[j]
                j=j+1
            k=k+1

        while i<len(left_list) :
            data[k] = left_list[i]
            i=i+1
            k= k+1

        while j<len(right_list) :
            data[k] = right_list[j]
            j=j+1
            k= k+1
    
    

# Do not change the following code
input_data = input()
data = []
for item in input_data.split(', '):
  if item.isnumeric():
    data.append(int(item))
  elif item.lstrip("-").isnumeric():
    data.append(int(item))
merge_sort(data)
print(data)
