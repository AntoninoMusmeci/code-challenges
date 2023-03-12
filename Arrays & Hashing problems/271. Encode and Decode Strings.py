#https://leetcode.com/problems/encode-and-decode-strings/editorial/
class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        encoded = ""
        for s in strs:
            n = len(s)
            encoded += str(n) + "s" + s
        return encoded

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        decoded = []
        i = 0
        
        while i in range(len(s)):
            number = ""
            while s[i] != "s":
                number += s[i]
                i += 1
            i += 1 #skip the s
            number = int(number)
            decoded_string = ""
            while number:
                number -= 1
                decoded_string += s[i]
                i+= 1
            decoded.append(decoded_string)
        return decoded 