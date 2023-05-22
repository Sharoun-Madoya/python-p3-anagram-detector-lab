# your code goes here!

class Anagram:
    def __init__(self, word):
        self.word = word.lower()
        self.sorted_word = self.sort_word(self.word)

    def match(self, word_list):
        anagrams = []
        for word in word_list:
            if self.is_anagram(word):
                anagrams.append(word)
        return anagrams

    def is_anagram(self, word):
        word = word.lower()
        return word != self.word and self.sort_word(word) == self.sorted_word

    @staticmethod
    def sort_word(word):
        return ''.join(sorted(word.lower()))


# Example usage
anagram = Anagram("listen")
possible_anagrams = ["enlist", "silent", "inlets", "banana"]

matches = anagram.match(possible_anagrams)
print(matches)