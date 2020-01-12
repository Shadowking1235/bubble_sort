def bubble_sort(bubble_list):
    for i in range(len(bubble_list) - 1, 0, -1):
        for j in range(i):
            if bubble_list[j] > bubble_list[j + 1]:
                temp = bubble_list[j]
                bubble_list[j] = bubble_list[j+1]
                bubble_list[j+1] = temp


king_list = [67, 33, 299,234,56,78,0, 98,-56,21,4,21,34.54, 33, 5]
bubble_sort(king_list)
print(king_list)
bubble_sort(bubble_list=king_list)

