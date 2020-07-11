def sentence_maker(phrase):
    interrogatives = ("how", "what", "who", "why")
    capitalized = phrase.capitalize()
    if phrase.startswith(interrogatives):
        return "{}?".format(capitalized)
    else:
        return "{}.".format(capitalized)

user_sentences = []
while True:
    user_input = input("Say something: ")
    if user_input == "\end":
        break
    else:
        user_sentences.append(sentence_maker(user_input))
print(" ".join(user_sentences))
