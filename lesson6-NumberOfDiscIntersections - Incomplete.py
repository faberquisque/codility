def solution(A):
    # write your code in Python 3.6
    N = len(A)
    lower = [0] * N
    upper = [0] * N
    for center, radius in enumerate(A)
        lower[center] = center - radius
        upper[center] = center + radius
    lower.sort()
    upper.sort()
    
    active = 0
    intersections = 0
    
    for l in lower:
        