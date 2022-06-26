def maxProductSubarray1(nums):
    '''
    n3
    '''
    result = float("-inf")
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            prod = 1
            for k in range(i, j):
                prod *= nums[k]
            result = max(result, prod)


def maxProductSubarray2(nums):
    # n2
    result = nums[0]
    for i in range(len(nums)):
        p = nums[i]
        for j in range(i+1, len(nums)):
            result = max(result, p)
            p *= nums[j]
        result = max(result, p)
    return result


def maxProductSubarray3(arr):
    # n
    maxLeft = arr[0]
    maxRight = arr[0]

    zeroPresent = False
    prod = 1
    for num in arr:
        prod *= num
        if num == 0:
            zeroPresent = True
            prod = 1
            continue
        maxLeft = max(maxLeft, prod)

    prod = 1
    for j in range(len(arr), 0, -1):
        prod *= arr[j]
        if arr[j] == 0:
            zeroPresent = True
            prod = 1
            continue
        maxRight = max(maxRight, prod)

    if zeroPresent:
        return max(max(maxLeft, maxRight), 0)
    return max(maxRight, maxLeft)


def maxProductSubarray4(arr):
    # n
    prod1, prod2, result = arr[0], arr[0], arr[0]

    for num in arr:
        temp = max(num, max(prod1*num, prod2*num))
        prod2 = min(num, min(prod1*num, prod2*num))
        prod1 = temp

        result = max(result, prod1)
    return result


print(maxProductSubarray4([1, 2, -3, 0, -4, -5]))
