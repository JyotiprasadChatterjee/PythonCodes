from fileinput import close


def twosum( nums, target):
    for i in range(len(nums)):
        for j in range(len(nums)):
            if j==i:
                continue

            else:
                if nums[i] + nums[j] == target:
                    print(nums[i], nums[j])
                    return()

    return None


twosum([1,2,3,4,5],5)