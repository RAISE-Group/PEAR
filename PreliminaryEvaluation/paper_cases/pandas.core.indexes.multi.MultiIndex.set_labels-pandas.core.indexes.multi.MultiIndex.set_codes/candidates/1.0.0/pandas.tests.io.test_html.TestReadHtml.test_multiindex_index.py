@pytest.mark.slow
def test_multiindex_index(self):
    df = self._bank_data(index_col=[0, 1])[0]
    assert isinstance(df.index, MultiIndex)