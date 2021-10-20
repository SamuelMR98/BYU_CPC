
from typing import List
def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) <= 1:
            return [nums]
        
        result = []
        for i in range(len(nums)):
            v = nums[0:i] + nums[i+1:]
            res = self.permute(v);
            
            for j in range(len(res)):
                _v = res[j];
                _v = [nums[i]] + _v
                result.append(_v);
            
        return result;