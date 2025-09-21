def productExceptSelf(self, nums):
        length = len(nums)
        products = [1] * length
        
        # Calculate left prefix products
        for i in range(1, length):
            products[i] = products[i - 1] * nums[i - 1]

        # Calculate right suffix products and multiply with the left
        right = 1  # Fix: should start at 1, not nums[-1]
        for i in range(length - 1, -1, -1):
            products[i] *= right
            right *= nums[i]
        
        return products
