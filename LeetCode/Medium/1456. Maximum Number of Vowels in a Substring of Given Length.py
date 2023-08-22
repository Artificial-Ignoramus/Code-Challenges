class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        s = tuple( 1 if ch in "aeiou" else 0 for ch in s )
        ans = m = sum( s[ : k ] )

        for i in range( len( s ) - k ):
            m += s[ i + k ] - s[i]

            if m > ans:
                if m == k:
                    return m
                else:
                    ans = m

        return ans
