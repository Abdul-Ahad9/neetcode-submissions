class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for word in strs:
            count = [0] * 26

            for ch in word:
                count[ord(ch) - ord('a')] += 1
            print(tuple(count))
            print(word)
            groups[tuple(count)].append(word)
        print(groups)
        return list(groups.values())