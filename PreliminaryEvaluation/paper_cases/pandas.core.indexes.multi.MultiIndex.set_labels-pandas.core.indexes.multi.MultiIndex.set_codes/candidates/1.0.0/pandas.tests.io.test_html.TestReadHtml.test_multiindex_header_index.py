@pytest.mark.slow
def test_multiindex_header_index(self):
    df = self._bank_data(header=[0, 1], index_col=[0, 1])[0]
    assert isinstance(df.columns, MultiIndex)
    assert isinstance(df.index, MultiIndex)