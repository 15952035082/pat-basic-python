n = int(input())
while n != 0:
    n -= 1
    s = input()
    exist_P = False
    exist_A = False
    exist_other = False
    order_fail = False
    have_PAT = False
    index_T = 0
    index_P = 0
    for i in range(0, len(s)):
        temp = s[i]
        if temp != "P" and temp != "A" and temp != "T":
            exist_other = True
            break
        if exist_P:
            if temp == "P":
                order_fail = True
                break
            if exist_A:
                if temp == "T":
                    have_PAT = True
                    index_T = i
                    break
                if temp != "A":
                    order_fail = True
            elif temp == "A":
                exist_A = True
                continue
            else:
                order_fail = True
                break
        else:
            if temp == "P":
                exist_P = True
                index_P = i
                continue
            if temp == "T":
                order_fail = True
                break
    if have_PAT:
        if index_T-index_P == 2:
            print("YES")
        elif index_P == 0 and index_T == len(s) - 1:
            print("YES")
        elif index_P * (index_T-index_P-1) == len(s) - index_T - 1:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")

