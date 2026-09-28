def test_mixed_index_no_fallback(self):
    s = Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 1, 2])
    with pytest.raises(KeyError, match='^0$'):
        s.at[0]
    with pytest.raises(KeyError, match='^4$'):
        s.at[4]