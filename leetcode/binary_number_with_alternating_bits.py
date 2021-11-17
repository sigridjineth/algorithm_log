class Solution(object):
    def hasAlternatingBits(self, n):
        val = n & 1
        n >>= 1
        while n > 0:
            last = n & 1
            if (val ^ last) == 0:
                return False
            val = last
            n >>= 1
        return True
