class Solution {
    public int lengthOfLongestSubstring(String s) {
        if (s.length() == 0) {
            return 0;
        }

        Set<Character> seenSet = new HashSet<>();
        int l = 0;
        int r = 0;
        int count = 0;
        int ans = 0;

        seenSet.add(s.charAt(l));
        count++;
        ans = count;
        r++;

        while (r < s.length()) {
            while (seenSet.contains(s.charAt(r))) {
                seenSet.remove(s.charAt(l));
                l++;
                count--;
            }

            seenSet.add(s.charAt(r));
            count++;
            if (count > ans) {
                ans = count;
            }
            r++;
        }
        return ans;
    }
}
