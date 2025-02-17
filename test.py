def even_elements(input_list):
    for num in input_list:
        if num % 2 == 0:
            output_list.append(num)
    return output_list

print(even_elements([1, 2, 3, 4, 5, 6]))