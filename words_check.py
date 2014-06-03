__author__ = 'ada'


def is_greater_word(expected, answered):
    if len(expected) >= len(answered):
        return len(expected)
    else:
        return len(answered)

def is_correct(expected, answered):
    if answered.lower() == expected.lower():
        return "OK"
    if answered in expected or expected in answered:
        return "TYPO"
    # if answered in expected and "to" in expected:
    #     return "OK"
    if expected == "to " + answered:
        return "OK"

    counter = 0
    for i in is_greater_word(expected, answered):
        for answ_letter in answered:
            for exp_letter in expected:
                if answ_letter[i] != exp_letter[i]:
                    counter += 1
    if counter < len(expected)/2:
        return "TYPO"
    else:
        return "WRONG WORD"


    if len(expected) > len(answered) and expected[:3] == "to " and expected[3:] == answered[3:]:
        return "OK"





assert is_correct("welcome", "WELCOME") == "OK"
assert is_correct("welcome", "elcome") == "TYPO"
assert is_correct("cranberies", "coanbelies")
assert is_correct("cranberies", "strawberies")
assert is_correct ("merry, happy, joyful", "merry") == "TYPO"



# alte posibilitati: parti de vorbire diferite






