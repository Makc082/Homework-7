def find_min_max(list):
    if list == 0:
        return 0

    min_value = min(list)
    max_value = max(list)
    
    min_index = list.index(min_value)
    max_index = list.index(max_value)
    
    print(f"Min: {min_value} on index {min_index}")
    print(f"Max: {max_value} on index {max_index}")
    
find_min_max([34, 76, 8, 12, 16])    