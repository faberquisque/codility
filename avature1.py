def solution(A)
    N = len(A)
    if N == 1:
        return 0
    A.sort(key = abs, reverse = True)
    for i in range(N-1):
        if A[i+1] == -A[i]:
            return abs(A[i])
    return 0
