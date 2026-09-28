def test_info_duplicate_columns_shows_correct_dtypes(self):
    io = StringIO()
    frame = DataFrame([[1, 2.0]], columns=['a', 'a'])
    frame.info(buf=io)
    io.seek(0)
    lines = io.readlines()
    assert ' 0   a       1 non-null      int64  \n' == lines[5]
    assert ' 1   a       1 non-null      float64\n' == lines[6]