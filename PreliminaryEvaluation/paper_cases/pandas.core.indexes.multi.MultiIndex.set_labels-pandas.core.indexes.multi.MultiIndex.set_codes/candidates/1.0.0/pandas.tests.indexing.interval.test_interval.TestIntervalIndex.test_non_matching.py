def test_non_matching(self):
    s = self.s
    with pytest.raises(KeyError, match='^$'):
        s.loc[[-1, 3, 4, 5]]
    with pytest.raises(KeyError, match='^$'):
        s.loc[[-1, 3]]