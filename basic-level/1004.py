n = int(input())
largest_grader = -1
minimum_grader = 101
the_best_name = ""
the_best_number = ""
the_lowest_name = ""
the_lowest_number = ""
temp_name = ""
temp_number = ""
temp_grader = 0
while n > 0:
    n -= 1
    ss = input().split()
    if int(ss[2]) > largest_grader:
        the_best_name = ss[0]
        the_best_number = ss[1]
        largest_grader = int(ss[2])
    if int(ss[2]) < minimum_grader:
        the_lowest_name = ss[0]
        the_lowest_number = ss[1]
        minimum_grader = int(ss[2])
print(the_best_name, the_best_number)
print(the_lowest_name, the_lowest_number, end="")




