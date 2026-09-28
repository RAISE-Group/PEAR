def test_tolist(self, data):
    result = pd.Series(data).tolist()
    expected = list(data)
    assert result == expected