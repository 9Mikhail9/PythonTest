from myfun import get_words_dict

def test_get_words_dict_good():
    assert get_words_dict(['aaaa', 'aaaa', 'aaaa', 'bbbb', 'bbbb', 'cccc', 'ffff', 'they’ll', 'think', 'well']) == {'aaaa': 3, 'bbbb': 2, 'cccc': 1, 'ffff': 1, 'they’ll': 1, 'think': 1, 'well': 1}
