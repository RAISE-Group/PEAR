@pytest.mark.slow
def test_multiindex_header(self):
    df = self._bank_data(header=[0, 1])[0]
    assert isinstance(df.columns, MultiIndex)