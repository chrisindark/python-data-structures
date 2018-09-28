# n = 10, coins = [1, 5, 10]
# 1 - 1+1+1+1+1+1+1+1+1+1
# 2 - 5 + 5
# 3 - 5 + 1+1+1+1+1
# 4 - 10


def rec_coin(target, coins):
    min_coins = target

    if target in coins:
        return 1
    else:
        for i in [c for c in coins if c <= target]:
            num_coins = 1 + rec_coin(target - i, coins)

            if num_coins < min_coins:
                min_coins = num_coins

    return min_coins


# print(rec_coin(10, [1, 5, 10]))
# print(rec_coin(15, [1, 5, 10]))
# print(rec_coin(63, [1, 5, 10, 25]))


def rec_coin_dyn(target, coins, cache):
    min_coins = target
    # print(cache)

    if target in coins:
        cache[target] = 1
        return 1

    if cache.get(target) is not None and cache[target] > 0:
        return cache[target]
    else:
        for i in [c for c in coins if c <= target]:
            num_coins = 1 + rec_coin_dyn(target - i, coins, cache)
            if num_coins < min_coins:
                min_coins = num_coins

                cache[target] = min_coins

    return min_coins


print(rec_coin_dyn(10, [1, 5, 10], {}))
print(rec_coin_dyn(15, [1, 5, 10], {}))
print(rec_coin_dyn(45, [1, 5, 10, 25], {}))
print(rec_coin_dyn(23, [1, 5, 10, 25], {}))
print(rec_coin_dyn(74, [1, 5, 10, 25], {}))
