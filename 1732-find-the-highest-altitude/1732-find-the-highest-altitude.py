class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        
        alt = [0]
        
        
        for g in gain:
        
            new_height = alt[-1] + g
            alt.append(new_height)
            
        
        return max(alt)