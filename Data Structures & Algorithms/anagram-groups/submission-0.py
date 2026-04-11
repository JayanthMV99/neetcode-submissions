class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = {}

        for s in strs:
            key_list = [0] * 26

            for i in range(len(s)):
                key_list[ord(s[i])-ord('a')] += 1
            key = tuple(key_list)
            if key not in map:
                map[key] = []
            map[key].append(s)

        return list(map.values())