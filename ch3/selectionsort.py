def selection_sort(A):
    n = len(A)
    for i in range(n - 1):
        minIdx = i
        for j in range(i + 1, n):
            if A[j] < A[i]:
                minIdx = j
        A[i], A[minIdx] = A[minIdx], A[i]
    

def main():
    A = [89, 45, 68, 90, 34, 17]
    print(A)
    selection_sort(A)
    print(A)
    
    


if __name__ == '__main__':
    main()