class Solution {
    public boolean isValid(String s) {
        Deque<Character> stack = new ArrayDeque<>();

        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (c == '(' || c == '[' || c == '{') {
                stack.push(c);
            } else if (stack.isEmpty()) {
                return false;
            } else {
                char p = stack.pop();
                if ((c == ')' && p != '(') || (c == ']' && p != '[') ||
                    (c == '}' && p != '{')) {
                    return false;
                }
            }
        }
        if (stack.isEmpty() == false)
            return false;
        return true;
    }
}
