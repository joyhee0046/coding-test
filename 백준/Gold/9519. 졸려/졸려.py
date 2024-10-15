def blink(word):
    n = len(word)
    half = n // 2
    result = list(word)

    for i in range(half):
        result.insert(i * 2 + 1, result.pop())

    return ''.join(result)


def reverse_blink(word):
    n = len(word)
    half = n // 2
    result = list(word)

    for i in range(half - 1, -1, -1):
        result.append(result.pop(i * 2 + 1))

    return ''.join(result)


def solve(X, word):
    # 주기성 탐색
    original_word = word
    seen = {}
    cycle = []

    # 주기 발견
    for i in range(X):
        if word in seen:
            cycle_length = i - seen[word]
            remaining_blinks = (X - i) % cycle_length
            return cycle[remaining_blinks]
        seen[word] = i
        cycle.append(word)
        word = reverse_blink(word)

    return word


# 입력
X = int(input())
word = input()

# 결과 출력
print(solve(X, word))
