def test_read_excel_chunksize(self, read_ext):
    with pytest.raises(NotImplementedError):
        pd.read_excel('test1' + read_ext, chunksize=100)