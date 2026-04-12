class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int l = 0;
        int r = numbers.length - 1;

        while (numbers[l] + numbers[r] != target) {
            int sum = numbers[l] + numbers[r];
            if (sum < target) {
                l++;
            } else {
                r--;
            }
        }
        int[] ans = {l + 1, r + 1};
        return ans;
    }
}
