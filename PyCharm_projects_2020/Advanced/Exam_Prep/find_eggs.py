def find_strongest_eggs(i_list, n):
    sublist = [i_list[i::n] for i in range(n)]
    result_list = []
    for s in sublist:
        mid_ind = int(len(s) // 2)
        if s[mid_ind - 1] < s[mid_ind] > s[mid_ind + 1]:
            if [i < j for i, j in zip(s[:mid_ind], s[mid_ind + 1:])]:
                result_list.append(s[mid_ind])
    return result_list



test = ([-1, 7, 3, 15, 2, 12], 2)
print(find_strongest_eggs(*test))

test = ([-1, 0, 2, 5, 2, 3], 2)
print(find_strongest_eggs(*test))

test = ([51, 21, 83, 52, 55], 1)
print(find_strongest_eggs(*test))