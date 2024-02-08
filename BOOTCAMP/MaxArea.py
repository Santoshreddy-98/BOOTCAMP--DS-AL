class Solution:
    def maxArea(self, height):
        max_area = 0
        left_pointer, right_pointer = 0, len(height) - 1

        while left_pointer < right_pointer:
            # Calculate the width between the two lines
            width = right_pointer - left_pointer

            # Calculate the height of the container (the shorter line)
            container_height = min(height[left_pointer], height[right_pointer])

            # Calculate the area and update max_area if necessary
            area = width * container_height
            max_area = max(max_area, area)

            # Move the pointers towards each other
            if height[left_pointer] < height[right_pointer]:
                left_pointer += 1
            else:
                right_pointer -= 1

        return max_area

# Example usage:
height1 = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print("Example 1 - Output:", Solution().maxArea(height1))  

height2 = [1, 1]
print("Example 2 - Output:", Solution().maxArea(height2))  
