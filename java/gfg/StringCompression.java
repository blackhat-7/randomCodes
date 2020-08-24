class StringCompression {

    String compress(String s1) {
        StringBuilder s2 = new StringBuilder(s1.length());
        int count = 1, i = 1;
        s2.append(s1.charAt(0));

        while (i < s1.length()) {
            if (s1.charAt(i) != s1.charAt(i-1)) {
                s2.append(count);
                s2.append(s1.charAt(i));
                count = 1;
            }
            count++;
            i++;
        }
        if (Character.isAlphabetic(s2.charAt(s2.length()-1))) {
            s2.append(count);
        }

        return s2.toString();
    }
    public static void main(String[] args) {
        StringCompression main = new StringCompression();
        String s1 = "aabcccccaaa";
        String s2 = main.compress(s1);
        System.out.println(s1 + " " + s2);
    }
}