def findDuplicates(self, nums):
        """
        Finds all duplicates in an array where elements are in range 1 to n.
        Modifies the input array in-place.
        """
        res = []
        for x in nums:
            index = abs(x) - 1
            if nums[index] < 0:
                res.append(abs(x))
            else:
                nums[index] = -nums[index]
        return res

def compress(self, chars):
        """
        Compresses the list of characters in-place using the counts of repeated characters.
        Returns the new length of the compressed list.
        """
        i = 0  
        j = 0 
        while j < len(chars):
            char = chars[j]
            count = 0
            while j < len(chars) and chars[j] == char:
                j += 1
                count += 1
            chars[i] = char
            i += 1
            if count > 1:
                for c in str(count):
                    chars[i] = c
                    i += 1
        return i

