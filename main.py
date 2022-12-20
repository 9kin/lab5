def knapsack(ws, W):
    dp = [0 for i in range(W + 1)]
    dp[0] = 1
    for cur in ws:
        for w in range(W, cur - 1, -1):
            if dp[w - cur]:
                dp[w] = 1
    res = []
    for i in range(W):
        if dp[i]:
            res.append(i)
    return res


# for i in range(100):
#    test = test_n(10, 1000000)
#    print('self.assertEqual(knapsack(', test[0], ',', test[1], '),', knapsack(*test), ')')


