class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {

        Map<List<Integer>, List<String>>words = new HashMap<>();

        for (int i = 0; i < strs.length; i++) {
            int[] alphabet = new int[26];
            
            for (int j = 0; j < strs[i].length(); j++) {
                int charType = ((int) strs[i].charAt(j)) - 97;
                System.out.println(charType);
                alphabet[charType]++;
            }
            ArrayList<Integer> alpha = new ArrayList<>();
            for (int k : alphabet) {
                alpha.add(k);
            }

            if (words.containsKey(alpha)) {
                List<String> anagrams = words.get(alpha);
                anagrams.add(strs[i]);
                words.put(alpha, anagrams);
            } else {
                List<String> anagrams = new ArrayList<>();
                anagrams.add(strs[i]);
                words.put(alpha, anagrams);
            }
        }
        List<List<String>> values = new ArrayList<>(words.values());
        return values;
    }
}
