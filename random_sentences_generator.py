# RandomSentencesGeneratorByaqcchi
import random
def get_random_word(words):
    return random.choice(words)

names = ["Naruto", "Sasuke", "Sakura", "Gaara", "Orochimaru", "Itachi", "Neji", "Deidara", "Hinata", "Obito"]
places = ["the Leaf Village", "the Sand Village", "Mount Myouboku", "the Land of Waves", "the Mist Village", "the Sound Village", "the Final Valley", "the Akatsuki hideout", "Orochimaru's hideout", "the moon"]
verbs = ["eats", "destroys", "sees", "plays with", "brings", "kisses", "crashes into", "throws", "slips on", "climbs"]
nouns = ["stones", "cake", "apple", "camera", "bikes", "ramen", "cactus", "explosives", "shuriken", "kunai"]
adverbs = ["slowly", "diligently", "warmly", "sadly", "rapidly", "angrily", "quickly", "stupidly", "impatiently", "happily"]
details = ["near the river", "at home", "in the park", "under the bridge", "above the clouds", "on the street", "under the waterfall", "at Ichiraku ramen", "in the Kage's office", "at the pub"]

while True:
    input("Click [Enter] to generate a random sentence.")

    random_name = get_random_word(names)
    random_place = get_random_word(places)
    random_adverb = get_random_word(adverbs)
    random_verb = get_random_word(verbs)
    random_noun = get_random_word(nouns)
    random_detail = get_random_word(details)

    print(f"{random_name} {random_adverb} {random_verb} {random_noun} {random_detail} at {random_place}.")
