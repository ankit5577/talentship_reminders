def fib(n):
    a, b = 0, 1
    c = 0
    while c < n:
        a, b = b, a+b
        c += 1
    return a


def fib2(n):
    if n <= 2:
        return 1
    return fib2(n-1) + fib(n-2)


n = 53
# print(fib(n))
# print(fib2(n))


def gridtravel(n, m, memo={}):
    key = str(n) + ',' + str(m)
    if key in memo:
        return memo[key]
    if n == 1 & m == 1:
        return 1
    if n == 0 or m == 0:
        return 0
    memo[key] = gridtravel(n-1, m, memo) + gridtravel(n, m-1, memo)
    return memo[key]

# print(gridtravel(18, 18))


def canSum(target, numbers, memo={}):
    if target in memo:
        return memo[target]

    if target == 0:
        return True
    if target < 0:
        return False

    for num in numbers:
        balance = target-num
        if canSum(balance, numbers, memo):
            memo[balance] = True
            return memo[balance]

    memo[balance] = False
    return False


def shortestHowSum(target, numbers, memo={}):
    if target in memo:
        return memo[target]

    if target == 0:
        return []

    if target < 0:
        memo[target] = False
        return memo[target]

    shortesCombination = None

    for num in numbers:
        balance = target-num
        remainderResult = shortestHowSum(balance, numbers)
        if remainderResult is not None and remainderResult is not False:
            memo[target] = remainderResult + [num]
            if shortesCombination is None or len(shortesCombination) > len(memo[target]):
                shortesCombination = memo[target]

    memo[target] = shortesCombination
    return memo[target]


# print(shortestHowSum(7987, [9, 3, 2, 87, 99]))

def canConstruct(target, words, memo={}):
    if target in memo:
        return memo[target]

    if target == '':
        return 1

    counts = 0

    for word in words:
        prefix = target[:len(word)]
        if word == prefix:
            suffix = target[len(word):]
            counts += canConstruct(suffix, words)

    memo[target] = counts
    return memo[target]


def allConstruct(target, words):
    if target == '':
        return []

    result = []
    for word in words:
        if word == target[:len(word)]:
            suffix = target[len(word):]
            suffixways = allConstruct(suffix, words)
            result.append([word]+suffixways)
    return result


# print(allConstruct('purple', ['purp', 'p', 'ur', 'le', 'purpl', 'ag', 'pa', 'hehe']))

def canSumTab(target, nums):
    dp = [False]*(target+1)
    dp[0] = True

    for i in range(target):
        if dp[i]:
            for num in nums:
                if (i+num) < len(dp):
                    dp[i+num] = True

    return dp[target]


def bestSumTab(target, nums):
    dp = [None]*(target+1)
    dp[0] = []
    for i in range(target):
        if dp[i] is not None:
            for num in nums:
                if num+i <= target:
                    local = dp[i] + [num]
                    if not dp[i+num] or len(local) < len(dp[i+num]):
                        dp[i+num] = local
    return dp[target]


def countConstruct(target, words):
    dp = [0]*(len(target)+1)
    dp[0] = 1

    for i in range(len(target)+1):
        for word in words:
            if word == target[i:i+len(word)] and len(word)+i <= len(target):
                dp[i+len(word)] += dp[i]

    return dp


def bestConstruct(target, words):
    table = [[]]*(len(target)+1)
    table[0] = [[]]

    for i in range(len(target)+1):
        for word in words:
            sliced = target[i:i+len(word)]
            if sliced == word:
                local = table[i]
                local.extend([word])
                table[i+len(word)].append(local)

    return table[-1]


# print(*bestSumTab(7, [2, 2, 3]))
print(bestConstruct('purple', ['purp', 'p',
      'ur', 'le', 'purpl', 'ag', 'pa', 'hehe']))


def climbing_stairs()
