def row_sum_odd_numbers(n):
    sum_odd_int = []
    for i in range(1, n+1):
        sum_odd_int.append(i * i **2)
    return(sum_odd_int[-1])
