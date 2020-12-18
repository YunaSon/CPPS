class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        dp={} #dp선언
        lis={} #
        if nums[0]==0:
            dp[nums[0]]=2
        else:
            dp[nums[0]]=1
            dp[-nums[0]]=1
        for i in range(1,len(nums)):
            for key,value in dp.items():
                if key+nums[i] not in lis:
                    lis[key+nums[i]]=value
                else:
                    lis[key+nums[i]]+=value
                if key-nums[i] not in lis:
                    lis[key-nums[i]]=value
                else:
                    lis[key-nums[i]]+=value
            dp=lis
            lis={}
        if S in dp:
            return dp[S]
        else:
            return 0    
