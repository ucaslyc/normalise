import pickle
from collections import defaultdict

from nltk.corpus import brown


def store_pos_tag_dicts():
    pos_tag_dict = defaultdict(tuple)
    tagged = brown.tagged_sents()
    for sent in tagged:
        for tup in sent:
            if not tup[1] in pos_tag_dict[tup[0].lower()]:
                pos_tag_dict[tup[0].lower()] += (tup[1],)

    pos_tag_dict_univ = defaultdict(tuple)
    tagged_univ = brown.tagged_sents(tagset='universal')
    for sent in tagged_univ:
        for tup in sent:
            if not tup[1] in pos_tag_dict_univ[tup[0].lower()]:
                pos_tag_dict_univ[tup[0].lower()] += (tup[1],)
    dicts = (pos_tag_dict, pos_tag_dict_univ)
    with open('pos_dicts.pickle', 'wb') as file:
        pickle.dump(dicts, file)
