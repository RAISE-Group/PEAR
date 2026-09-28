def test_add_string(self):
    index = pd.Index(['a', 'b', 'c'])
    index2 = index + 'foo'
    assert 'a' not in index2
    assert 'afoo' in index2