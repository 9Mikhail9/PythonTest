from myfun import opening_file

def test_opening_file_good():
    assert opening_file('Test0.txt','TestFiles/test_opening_file') == True

def test_opening_file_bad():
    assert opening_file('Test1.txt','TestFiles/test_opening_file') == False