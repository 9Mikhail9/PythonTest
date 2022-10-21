from myfun import get_words

def test_get_words_good():
    assert get_words('TestFiles/test_get_words_good/Test0.txt') == ['aaaa', 'aaaa', 'aaaa', 'aaaa', 'aaaa', 'aaaa', 'aaaa', 'aaaa', 'aaaa']