def read_matrix():
    rows_count = int(input())
    return [[int(x)
            for x in input().split(', ')]
            for _ in range(rows_count)]


matrix = read_matrix()
flattened = [num
             for row in matrix
             for num in row]
print(flattened)


#
# flattened2 = []
# for row in matrix:
#     [flattened2.append(x) for x in row]
#     # for num in row:
#     #     flattened2.append(num)
#
# print(flattened2)