def solution(statues):
    return max(statues) - min(statues) - len(statues) + 1

print(solution([1, 100]))