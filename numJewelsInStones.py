def numJewelsInStones(J, S):
    return sum(map(lambda jewel: S.count(jewel), J))
