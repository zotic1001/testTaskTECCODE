from typing import List


def prime_numbers_series_generator(start: int, end: int) -> List[int]:
    prime_numbers = []
    for i in range(start, end):
        flag = True
        for j in range(2, round(end ** 0.5) + 1):
            if i % j == 0:
                flag = False
                break
        if flag:
            prime_numbers.append(i)
    return prime_numbers
