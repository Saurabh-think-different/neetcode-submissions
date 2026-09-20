class Solution:

    # d = [dance, dag, danger, damage]
    # da = [dance, dag, danger, damage]
    # dan = [dance, danger]
    # dag = dag
    # dam = damage


    def longestCommonPrefix(self, strs: List[str]) -> str:
        lcp = ""
        small_word, length_of_word = "", 300

        for s in strs:
            if len(s) < length_of_word:
                length_of_word = len(s)
                small_word = s

        for i in range(length_of_word):
            verdict = all([small_word[i]==s[i] for s in strs])
            print(verdict)
            if not verdict:
                break
            lcp += small_word[i]
            
        return lcp