Given a 0-indexed n x n integer matrix grid, return the number of pairs (ri, cj) such that row ri and column cj are equal.
A row and column pair is considered equal if they contain the same elements in the same order (i.e., an equal array).

Solution:
from typing import List

class Solution:
    def numSpecialEquivGroups(self, words: List[str]) -> int:
        def getSignature(word):
            even = ''.join(sorted(word[0::2]))
            odd = ''.join(sorted(word[1::2]))
            return even + odd
        
        signatures = set()
        
        for word in words:
            signature = getSignature(word)
            signatures.add(signature)
        
        return len(signatures)
