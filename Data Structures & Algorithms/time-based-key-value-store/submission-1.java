class TimeMap {
    private Map<String, TreeMap<Integer, String>> map;
    public TimeMap() {
        map = new HashMap<>();
    }
    
    public void set(String key, String value, int timestamp) {
        map.computeIfAbsent(key, k -> new TreeMap<Integer, String>()).put(timestamp, value);
    }
    
    public String get(String key, int timestamp) {
        Map<Integer, String> retrievedMap = map.get(key);
        if (retrievedMap == null) {
            return "";
        }
        while (timestamp >= 0) {
            String word = retrievedMap.get(timestamp);
            if (word != null) {
                return word;
            }
            timestamp--;
        }
        return "";
    }
}
