class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for word in strs:
            encoded_string += word + "~"

        return encoded_string

    def decode(self, s: str) -> List[str]:
        listed_string = list(s)
        decoded_string = []
        word = ""
        for letter in listed_string:
            if (letter == "~"):
                decoded_string.append(word)
                word = ""
            else:
                word += letter
        
        return decoded_string