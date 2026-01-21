class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_water = 0
        
        while left < right:
            # 1. Calculate the dimensions
            current_width = right - left
            # The container height is limited by the shorter side
            current_height = min(height[left], height[right])
            
            # 2. Calculate area and update the record
            current_area = current_width * current_height
            max_water = max(max_water, current_area)
            
            # 3. Greedy Move: Move the pointer that points to the SHORTER wall
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
                
        return max_water