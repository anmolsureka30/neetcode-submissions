class Solution:

    def encode(self, strs: List[str]) -> str:
        # encode a list of strings to a string
        # decode the string back to the list
        # need to attach a parameter to count the no of chars 
        encoded_string = ""
        for word in strs:
            encoded_string += str(len(word))+ "#"+ word
        return encoded_string
    def decode(self, s: str) -> List[str]:
        strs=[]
        i = 0
        while i < len(s):
                j = s.find("#",i)
                length = int(s[i:j])
                start = j+1
                end = start+length
                strs.append(s[start:end])
                i = end
        return strs        
