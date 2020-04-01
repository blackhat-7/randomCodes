public class Trie {

    static final int ALPHABET_SIZE = 26;
    TrieNode root;
    public Trie() {
        root = new TrieNode();
    }
    
    class TrieNode {
        TrieNode children[];
        boolean isEndOfWord;

        TrieNode() {
            children = new TrieNode[ALPHABET_SIZE];
            for(int i=0; i<ALPHABET_SIZE; ++i) {
                children[i] = null;
            }
            isEndOfWord = false;
        }
    }

    public void insert(String key) {
        int length = key.length();
        TrieNode pCrawl = root;
        int index;

        for(int i=0; i<length; ++i) {
            index = key.charAt(i) - 'a';
            if(pCrawl.children[index] == null)
                pCrawl.children[index] = new TrieNode();
            pCrawl = pCrawl.children[index];
        }

        pCrawl.isEndOfWord = true;
    }

    public boolean search(String key) {
        int length = key.length();
        TrieNode pCrawl = root;
        int index;

        for(int i=0; i<length; ++i) {
            index = key.charAt(i) - 'a';
            if(pCrawl.children[index] == null)
                return false;
            pCrawl = pCrawl.children[index];
        }
        return pCrawl != null && pCrawl.isEndOfWord;
    }

    public static void main(String[] args) {
        Trie myTrie = new Trie();
        String keys[] = {"my", "name", "is", "shaunak"};
        for(int i=0; i<keys.length; ++i) {
            myTrie.insert(keys[i]);
        }
        for(int i=0; i<keys.length; ++i) {
            System.out.println(myTrie.search(keys[i]));
        }
    }


}