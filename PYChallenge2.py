
def decryption(crypted_text, the_alphabet, shift):

    alphabet_letters = []
    letters_and_equivalents = {}
    decrypted_string = ""

    for each_char in the_alphabet:
        alphabet_letters.append(each_char)

    # put into a dictionary all the letters of the alphabet as keys, and the correspondentent letter as values

    for i in range(0,len(alphabet_letters)-shift):
        letters_and_equivalents[alphabet_letters[i]] = alphabet_letters[i+shift]

    for i in range((len(alphabet_letters)-shift), len(alphabet_letters)):
        letters_and_equivalents[alphabet_letters[i]] = alphabet_letters[(i+2) % 26]

    """for i in range((len(alphabet_letters)-shift), len(alphabet_letters)):
        letters_and_equivalents[alphabet_letters(len(alphabet_letters[i] = alphabet_letters[j]
        j = j+ 1"""

    for each_char in crypted_text:
        if each_char in letters_and_equivalents:
            decrypted_string += letters_and_equivalents[each_char]
        else:
            decrypted_string += each_char

    #find each_char in dict and give me value
    return decrypted_string


the_alphabet = "abcdefghijklmnopqrstuvwxyz"
crypted_text = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

print decryption(crypted_text,the_alphabet,2)


# version 2

from string import maketrans
def short_decryption(crypted_text):

    initial_letters = "abcdefghijklmnopqrstuvwxyz"
    equivalent_letters = "cdefghijklmnopqrstuvwxyzab"
    mapping = maketrans(initial_letters, equivalent_letters)

    uncrypted_text = crypted_text.translate(mapping)

    return uncrypted_text

crypted_text = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
print short_decryption(crypted_text)


