def preorder(l,ind1,ind2):
    if ind2>=ind1:
        mid=int(ind1+((ind2-ind1)/2))
        print(l[mid],end=' ')
        preorder(l,ind1,mid-1)
        preorder(l,mid+1,ind2)
    


for i in range(int(input())):
    k=int(input())
    l=[int(i) for i in input().split()]
    preorder(l,0,k-1)
    print()
