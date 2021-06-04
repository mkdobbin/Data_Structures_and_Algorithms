# python3

def max_pairwise_product(n, A):
    """
    # Multiply two largest numbers in list
    """
    # Find largest number in list
    index1 = 0
    for i in range(0, n):
        if A[i] > A[index1]:
            index1 = i
    
    # Find second largest number in list        
    index2 = 0
    if index1 == 0:
        index2 = 1
    for i in range(0,n):
        if i != index1 and A[i] > A[index2]:
            index2 = i

    return A[index1]*A[index2]
    
if __name__ == '__main__':
    n = int(input())
    A = [int(x) for x in input().split()]
    print(max_pairwise_product(n,A))