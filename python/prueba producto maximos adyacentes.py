def adjacent_elements_product(array):
    max_product = float('-inf')  # Initialize with negative infinity

    for i in range(len(array) - 1):
        product = array[i] * array[i + 1]
        if product > max_product:
            max_product = product

    return max_product

print(adjacent_elements_product([1, -4, 50, 6, 90, 8, 1, -9]))