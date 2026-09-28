def test_get_indexer_strings_raises(self):
    index = pd.Index(['b', 'c'])
    msg = "unsupported operand type\\(s\\) for -: 'str' and 'str'"
    with pytest.raises(TypeError, match=msg):
        index.get_indexer(['a', 'b', 'c', 'd'], method='nearest')
    with pytest.raises(TypeError, match=msg):
        index.get_indexer(['a', 'b', 'c', 'd'], method='pad', tolerance=2)
    with pytest.raises(TypeError, match=msg):
        index.get_indexer(['a', 'b', 'c', 'd'], method='pad', tolerance=[2, 2, 2, 2])