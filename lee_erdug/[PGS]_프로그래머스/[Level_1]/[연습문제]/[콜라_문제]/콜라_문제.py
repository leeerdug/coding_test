def solution(a, b, n):
    answer = 0
    m = 0

    while n >= a:
        m = n % a
        d = n // a
        n = d * b + m
        answer += d * b

    return answer