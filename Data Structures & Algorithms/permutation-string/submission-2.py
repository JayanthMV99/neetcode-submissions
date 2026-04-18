class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)

        if n > len(s2):
            return False

        s1map = [0] * 26
        s2map = [0] * 26

        for i in range(len(s1)):
            s1map[ord(s1[i]) - ord('a')] += 1
            s2map[ord(s2[i]) - ord('a')] += 1

        for i in range(len(s2) - n):
            if s1map == s2map:
                return True

            s2map[ord(s2[i]) - ord('a')] -= 1
            s2map[ord(s2[i + n]) - ord('a')] += 1

        return s1map == s2map