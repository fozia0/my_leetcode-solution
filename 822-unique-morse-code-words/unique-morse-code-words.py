class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = {'a':".-", 'b':"-...", 'c':"-.-.", 'd':"-..", 'e':".", 'f':"..-.", 'g':"--.", 'h':"....", 'i':"..", 'j':".---", 'k':"-.-", 'l':".-..", 'm':"--", 'n':"-.", 'o':"---", 'p':".--.", 'q':"--.-", 'r':".-.", 's':"...", 't':"-", 'u':"..-", 'v':"...-", 'w':".--", 'x':"-..-", 'y':"-.--", 'z':"--.."}
        tran = set()
        for word in words:
            temp = ""
            for i in range(len(word)):
                temp += morse[word[i]]
            tran.add(temp)
        return len(tran)