class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        print("nums:", nums , "val:" ,val)
        print(len(nums))

        k=0
        for i , num in enumerate(nums):
            
            if num != val:
                nums[k] = num
                k = k + 1

        
        return k
                
        