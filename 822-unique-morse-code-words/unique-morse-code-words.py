class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = {'a':".-", 'b':"-...", 'c':"-.-.", 'd':"-..", 'e':".", 'f':"..-.", 'g':"--.", 'h':"....", 'i':"..", 'j':".---", 'k':"-.-", 'l':".-..", 'm':"--", 'n':"-.", 'o':"---", 'p':".--.", 'q':"--.-", 'r':".-.", 's':"...", 't':"-", 'u':"..-", 'v':"...-", 'w':".--", 'x':"-..-", 'y':"-.--", 'z':"--.."}
        resu = set()
        for word in words:
            tran = ""
            for i in range(len(word)):
                tran += morse[word[i]]
            resu.add(tran)
        return len(resu)