from myfun import get_file_name

def test_get_file_name_good():
    assert get_file_name('TestFiles/test_get_file_name',True,True,True,True,True) == ['Test0.txt', 'Test1.txt', 'Test2.txt', 'Test3.txt']


def test_get_file_name_oll_files():
    assert get_file_name('TestFiles/test_get_file_name/test_get_file_name_oll_files',True,True,True,True,True) == ['Test0.txt', 'Test1.xlsx','Test2.xls','Test3.docx','Test4.doc','Test5.pdf','Test6.pptx','Test7.ppt']

def test_get_file_name_txt():
    assert get_file_name('TestFiles/test_get_file_name/test_get_file_name_oll_files',True,False,False,False,False) == ['Test0.txt']
def test_get_file_name_without_txt():
    assert get_file_name('TestFiles/test_get_file_name/test_get_file_name_oll_files',False,True,True,True,True) == ['Test1.xlsx','Test2.xls','Test3.docx','Test4.doc','Test5.pdf','Test6.pptx','Test7.ppt']

def test_get_file_name_xlsx():
    assert get_file_name('TestFiles/test_get_file_name/test_get_file_name_oll_files',False,False,False,False,True) == ['Test1.xlsx','Test2.xls']
def test_get_file_name_without_xlsx():
    assert get_file_name('TestFiles/test_get_file_name/test_get_file_name_oll_files',True,True,True,True,False) == ['Test0.txt','Test3.docx','Test4.doc','Test5.pdf','Test6.pptx','Test7.ppt']

def test_get_file_name_docx():
    assert get_file_name('TestFiles/test_get_file_name/test_get_file_name_oll_files',False,True,False,False,False) == ['Test3.docx','Test4.doc']
def test_get_file_name_without_docx():
    assert get_file_name('TestFiles/test_get_file_name/test_get_file_name_oll_files',True,False,True,True,True) == ['Test0.txt', 'Test1.xlsx','Test2.xls','Test5.pdf','Test6.pptx','Test7.ppt']

def test_get_file_name_pdf():
    assert get_file_name('TestFiles/test_get_file_name/test_get_file_name_oll_files',False,False,True,False,False) == ['Test5.pdf']
def test_get_file_name_without_pdf():
    assert get_file_name('TestFiles/test_get_file_name/test_get_file_name_oll_files',True,True,False,True,True) == ['Test0.txt', 'Test1.xlsx','Test2.xls','Test3.docx','Test4.doc','Test6.pptx','Test7.ppt']

def test_get_file_name_pptx():
    assert get_file_name('TestFiles/test_get_file_name/test_get_file_name_oll_files',False,False,False,True,False) == ['Test6.pptx','Test7.ppt']
def test_get_file_name_without_pptx():
    assert get_file_name('TestFiles/test_get_file_name/test_get_file_name_oll_files',True,True,True,False,True) == ['Test0.txt', 'Test1.xlsx','Test2.xls','Test3.docx','Test4.doc','Test5.pdf']
