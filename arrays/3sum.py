# approach 1: triple loop (TLE)



# approach 2: double loop double Hashset without checking duplicates (TLE)
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        st = set()
        result = set()
        for i in range(len(nums)):
            # i ll add check here
            st.clear()
            for j in range(i+1, len(nums)):
                target = -nums[i]-nums[j]

                if target in st:
                    t = tuple(sorted([nums[i], nums[j], target]))
                    if target not in result:
                        result.add(t)
                    
                st.add(nums[j])
        return [list(a) for a in result]



                    
# approach 2: double loop double Hashset without checking duplicates (Passed)
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        st = set()
        result = set()
        for i in range(len(nums)):
            # added a check here to skip duplicates
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            st.clear()
            for j in range(i+1, len(nums)):
                target = -nums[i]-nums[j]

                if target in st:
                    t = tuple(sorted([nums[i], nums[j], target]))
                    if target not in result:
                        result.add(t)
                    
                st.add(nums[j])
        return [list(a) for a in result]
                    


# using sorting and two pointer approach (passed)
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        st = set()
        for i, vi in enumerate(nums):
            j = i+1
            k = len(nums)-1

            while j<k:
                target = nums[j] + nums[k]
                if  target < -vi:
                    j+=1
                elif target > -vi:
                    k-=1
                else:
                    t = (nums[i], nums[j], nums[k])
                    st.add(t)
                    j+=1
                    k-=1
        return [list(a) for a in st]

                    
                
                


