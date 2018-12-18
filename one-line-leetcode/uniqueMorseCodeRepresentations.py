# International Morse Code defines a standard encoding where each letter is 
# mapped to a series of dots and dashes, as follows: "a" maps to ".-", "b" maps 
# to "-...", "c" maps to "-.-.", and so on.
# Now, given a list of words, each word can be written as a concatenation of 
# the Morse code of each letter. For example, "cba" can be written as 
# "-.-..--...", (which is the concatenation "-.-." + "-..." + ".-"). We'll call 
# such a concatenation, the transformation of a word.
# Return the number of different transformations among all words we have.

def uniqueMorseRepresentations(words): return len(set((map(lambda L: ''.join(L), map(lambda L: map(lambda x: [".-", "-...", "-.-.", "-..", ".","..-.", "--.", "....", "..", ".---","-.-", ".-..", "--", "-.", "---",".--.", "--.-", ".-.", "...", "-","..-", "...-", ".--", "-..-", "-.--","--.."][ord(x) - ord('a')], L), map(lambda s: list(s), words))))))
