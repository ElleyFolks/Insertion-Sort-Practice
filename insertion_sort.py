# organizes based on if numbers are greater, then swap; similar to shell sort, but with a gap value of 1 (compared values are adjacent).
def insertion_sort(unordered_list):
    # assume that first element at index 0 is sorted
    for i in range(1, len(unordered_list)):
        insert_index = i
        print("    current index: ", i)

        # will swap any values before the current index if they are greater
        while (insert_index > 0 and (unordered_list[insert_index] < unordered_list[insert_index-1])):

            temp1 = unordered_list[insert_index]
            temp2 = unordered_list[insert_index-1]

            # swaping these values
            unordered_list[insert_index] = temp2
            unordered_list[insert_index-1] = temp1
            print("        swapped {a} and {b}".format(
                a=unordered_list[insert_index], b=unordered_list[insert_index-1]))
            # to check all previous indices, must reduce by one each time.
            insert_index -= 1
            print("        updated list: ", unordered_list)
    print("final ordered list: ", unordered_list)


# main program
numbers = [70, 20, 1, 5, 100]
print("initial list: ", numbers)
result = insertion_sort(numbers)
