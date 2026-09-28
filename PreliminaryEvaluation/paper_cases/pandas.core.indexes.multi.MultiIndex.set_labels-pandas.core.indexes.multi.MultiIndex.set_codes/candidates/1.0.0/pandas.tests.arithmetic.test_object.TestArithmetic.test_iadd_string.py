def test_iadd_string(self):
    index = pd.Index(['a', 'b', 'c'])
    assert 'a' in index
    index += '_x'
    assert 'a_x' in index