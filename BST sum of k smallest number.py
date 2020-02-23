for i in range(int(input())):
    k= int(input())
    l=[int(i) for i in input().split()]
    p=int(input())
    l=sorted(list(set(l)))
    print(sum(l[ :p]))
