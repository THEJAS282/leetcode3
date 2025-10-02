class Solution {
    public int pivotIndex(int[] nums) {
        int total = 0;
        for (int num : nums) {
            total += num;
        }

        int leftTotal = 0;
        for (int i = 0; i < nums.length; i++) {
            int rightTotal = total - leftTotal - nums[i];
            if (rightTotal == leftTotal) {
                return i;
            }
            leftTotal += nums[i];
        }

        return -1;        
    }

    // Main method to test
    public static void main(String[] args) {
        Solution sol = new Solution();

        int[] nums1 = {1, 7, 3, 6, 5, 6};
        System.out.println("Pivot index of nums1: " + sol.pivotIndex(nums1)); // Output: 3

        int[] nums2 = {1, 2, 3};
        System.out.println("Pivot index of nums2: " + sol.pivotIndex(nums2)); // Output: -1

        int[] nums3 = {2, 1, -1};
        System.out.println("Pivot index of nums3: " + sol.pivotIndex(nums3)); // Output: 0
    }
}
