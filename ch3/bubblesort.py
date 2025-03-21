
def bubble_sort(A):
    n = len(A)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if A[j + 1] < A[j]:
                A[j + 1], A[j] = A[j], A[j + 1]


def main():
    A = [89, 45, 68, 90, 34, 17]
    print(A)
    bubble_sort(A)
    print(A)
    
    


if __name__ == '__main__':
    main()