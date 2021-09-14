import spellchecker


def SpellChecker2(word):
    spell = spellchecker.SpellChecker()
    # Get the one `most likely` answer
    print(spell.correction(word))

    # Get a list of `likely` options
    print(spell.candidates(word))


if __name__ == '__main__':
    SpellChecker2("Compter")
