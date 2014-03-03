__author__ = 'ada'


class SmartText:
    def __init__(self, text, source):
        import re
        self.text = text
        self.words = re.findall(r"[\w']+", self.text)
        self.source = source

    def compute_difficulty(self, word_difficulties):
        import re
        sum_difficulties = 0
        words_self.text = re.findall(r"[\w']+", self.text)

        for each_word in words_self.text:
            if word_difficulties.has_key(each_word):
                sum_difficulties += word_difficulties[each_word]
            else:
                sum_difficulties+=21

        return words_self.text, sum_difficulties

    def generate_quiz(self, word):

        words_up_to_word = []
        words_after_word = []
        self.text_split = self.text.split()
        missing_word = ""

        for i in range(0, self.text_split.index(word)):
            words_up_to_word.append(self.text_split[i])
        self.text_up_to_word = ' '.join(words_up_to_word)

        for j in range(self.text_split.index(word)+1, len(text_split)):
            words_after_word.append(self.text_split[j])
        self.text_after_word = ' '.join(words_after_word)

        for i in range(0, len(word)):
            missing_word += "."

        return self.text_up_to_word + ' ' + missing_word + ' ' + self.text_after_word

    def shorten_word_context(self, given_word, max_length):
        final_self.text = ""

        forty_list=[]
        list_of_self.text = self.text.split() # ==> gives me a list of the words ["these", "types", ",", "the"]
        word_count = len(list_of_self.text)

        if word_count <= max_length:
            return self.text.capitalize()
        #  len(list_of_text)=10
        for i in range(0,max_length):
            forty_list.append(list_of_self.text[i]) # lista cu primele 42 cuvinte
        string_forty_list = ' '.join(forty_list) # string cu primele 42 cuv

        if list_of_self.text.index(given_word) <= max_length:
            final_self.text = final_self.text + string_forty_list
            return final_self.text.capitalize()

        else:
            for i in range(max_length + 1, list_of_self.text.index(given_word) + 1):
                forty_list.append(list_of_self.text[i])
                string_forty_list = ' '.join(forty_list)
            final_self.text = final_self.text + string_forty_list
            return final_self.text.capitalize()



rose = SmartText("A rose by any other name would smell just as sweet", "Shakespeare")

stiinta = SmartText("Ca schiintza nu-i vaca de muls", "I.L. Caragiale")


print rose.compute_difficulty({"a":5,"rose":5,"name":5,"smell":5})
print rose.generate_quiz("sweet")
print stiinta.shorten_word_context("smell", 42)
