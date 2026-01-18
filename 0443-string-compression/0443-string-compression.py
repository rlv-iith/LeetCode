class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 0
        write_index=0
        while i<len(chars):
            current_char=chars[i]
            count =0
            while i<len(chars) and chars[i]==current_char:
                i+=1
                count+=1
            chars[write_index]=current_char
            write_index+=1
            if count >1:
                for digit in str(count):
                    chars[write_index]=digit
                    write_index +=1
        return write_index
