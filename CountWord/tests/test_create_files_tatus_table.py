import pandas as pd
import pytest

from myfun import create_files_tatus_table
@pytest.mark.skip(reason="no way of currently testing this")
def test_create_files_tatus_table():
    data_file = pd.DataFrame(columns=['File Name', 'Read/Not Read'])
    create_files_tatus_table(data_file,)