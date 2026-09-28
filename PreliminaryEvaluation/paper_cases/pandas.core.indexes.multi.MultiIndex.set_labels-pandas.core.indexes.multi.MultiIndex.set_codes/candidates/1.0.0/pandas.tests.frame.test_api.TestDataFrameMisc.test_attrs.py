def test_attrs(self):
    df = pd.DataFrame({'A': [2, 3]})
    assert df.attrs == {}
    df.attrs['version'] = 1
    result = df.rename(columns=str)
    assert result.attrs == {'version': 1}