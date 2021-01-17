public class Trie {
    private static class Node {
        protected Node[] children;
        protected boolean isEndOfWord;

        public Node() {
            this.children = new Node[26];
            this.isEndOfWord = false;
        }
    }
    private Node root;
    public Trie() {
        this.root = new Node();
    }

    public static void main(String[] args) {
        Trie trie = new Trie();
        String[] words = {"apple", "banana", "orange", "orangutan"};
        for (String word : words)
            trie.add(word);
        System.out.println(trie.search("orange"));
        trie.remove("banana");
        System.out.println(trie.search("banana"));
    }

    public void add(String word) {
        Node tempRoot = root;
        word = word.toLowerCase();
        for (char c : word.toCharArray()) {
            int index = (int)c - (int)'a';
            if (tempRoot.children[index] == null)
                tempRoot.children[index] = new Node();
            tempRoot = tempRoot.children[index];
        }
        tempRoot.isEndOfWord = true;
    }

    public void remove(String word) {
        Node tempRoot = root;
        word = word.toLowerCase();
        for (char c : word.toCharArray()) {
            int index = (int)c - (int)'a';
            if (tempRoot.children[index] == null)
                return;
            tempRoot = tempRoot.children[index];
        }
        tempRoot.isEndOfWord = false;
    }

    public boolean search(String word) {
        Node tempRoot = root;
        word = word.toLowerCase();
        for (char c : word.toCharArray()) {
            int index = (int)c - (int)'a';
            if (tempRoot.children[index] == null)
                return false;
            tempRoot = tempRoot.children[index];
        }
        if (!tempRoot.isEndOfWord)
            return false;
        return true;
    }
}
