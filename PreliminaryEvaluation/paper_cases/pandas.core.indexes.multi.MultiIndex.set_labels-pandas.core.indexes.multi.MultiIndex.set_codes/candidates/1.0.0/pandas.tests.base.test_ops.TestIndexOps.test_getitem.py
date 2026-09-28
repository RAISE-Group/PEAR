def test_getitem(self):
    for i in self.indexes:
        s = pd.Series(i)
        assert i[0] == s.iloc[0]
        assert i[5] == s.iloc[5]
        assert i[-1] == s.iloc[-1]
        assert i[-1] == i[9]
        with pytest.raises(IndexError):
            i[20]
        with pytest.raises(IndexError):
            s.iloc[20]