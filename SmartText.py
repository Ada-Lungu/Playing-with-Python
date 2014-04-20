__author__ = 'ada'


class SmartText:
    def __init__(self, text, source):
        import re
        self.text = text
        self.words = re.findall(r"[\w']+", self.text)
        self.source = source # string


    def compute_difficulty(self, word_difficulties):
        sum_difficulties = 0

        for each_word in self.words:
            if word_difficulties.has_key(each_word):
                sum_difficulties += word_difficulties[each_word]
            else:
                sum_difficulties+=21

        return sum_difficulties

    def generate_quiz(self, word):

        words_up_to_word = []
        words_after_word = []
        missing_word = ""

        for i in range(0, self.text.split().index(word)):
            words_up_to_word.append(self.text.split()[i])
        text_up_to_word = ' '.join(words_up_to_word)

        for j in range(self.text.split().index(word)+1, len(self.text.split())):
            words_after_word.append(self.text.split()[j])
        text_after_word = ' '.join(words_after_word)

        for i in range(0, len(word)):
            missing_word += "."

        return text_up_to_word + ' ' + missing_word + ' ' + text_after_word

    def shorten_word_context(self, given_word, max_length):
        final_text = ""
        forty_list=[]
        word_count = len(self.words)

        if word_count <= max_length:
            return self.text.capitalize()
        #  len(list_of_text)=10
        for i in range(0, max_length):
            forty_list.append(self.words[i]) # lista cu primele 42(max length) cuvinte
        string_forty_list = ' '.join(forty_list) # string cu primele 42 cuv

        if self.words.index(given_word) <= max_length:
            final_text = final_text + string_forty_list
            return final_text.capitalize()

        else:
            for i in range(max_length + 1, self.words.index(given_word) + 1):
                forty_list.append(self.words[i])
                string_forty_list = ' '.join(forty_list)
            final_text = final_text + string_forty_list
        return final_text.capitalize()



rose = SmartText("A rose by any other name would smell just as sweet", "Shakespeare")

stiinta = SmartText("Ca schiintza nu-i vaca de muls", "I.L. Caragiale")


print rose.compute_difficulty({"a":5,"rose":5,"name":5,"smell":5})
print rose.generate_quiz("sweet")
print stiinta.shorten_word_context("vaca", 10)
