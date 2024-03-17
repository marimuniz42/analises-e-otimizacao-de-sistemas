def find_subconjunto(nums, resp):
    def backtrack(start, path, curr_sum):
        if curr_sum == resp:
            result.append(path)
            return
        if curr_sum > resp:
            return
        for i in range(start, len(nums)):
            backtrack(i + 1, path + [nums[i]], curr_sum + nums[i])

    result = []
    backtrack(0, [], 0)
    return result

nums = [33, 20, 15, 33, 40, 51, 46, 26]
resp = 66
subsets = find_subconjunto(nums, resp)
print(f"Subconjuntos cuja soma é {resp}:", (subsets))