t=int(input())
for _ in range(t):
    left =[]
    right =[]
    letter =input()
    for i in letter:
        if i=="<":
             if left:
                 right.append(left.pop())
        elif i==">":
            if right:
                left.append(right.pop())
        elif i=='-':
            if left:
                left.pop()
        else:
    
    #ó���� �׳� right�� ���ߴ��� Ʋ�Ⱦ���.
            left.append(i)
    answer =left+right[::-1]
    for i in answer:
        print(i, end="")
    print()