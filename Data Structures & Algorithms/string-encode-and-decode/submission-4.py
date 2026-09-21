class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = ""
        for s in strs:
            ans = ans + str(len(s))+ "#" + s
        return ans
    def decode(self, s: str) -> List[str]:
        ans = []
        i = 0
        count = ""
        while i<len(s):
            if s[i].isdigit():
                count += s[i]
                i+=1
                continue
            if s[i] == "#":
                count = int(count)
                if count == 0:
                    ans.append("")
                    i+=1
                    count = ""
                else:
                    ele = s[i+1:i+count+1]
                    ans.append(ele)
                    i = i+count+1
                    count = ""
        return ans
