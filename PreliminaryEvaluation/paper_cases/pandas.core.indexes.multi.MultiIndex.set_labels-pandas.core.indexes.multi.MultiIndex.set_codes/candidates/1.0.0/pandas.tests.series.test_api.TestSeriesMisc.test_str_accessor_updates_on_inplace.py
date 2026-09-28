def test_str_accessor_updates_on_inplace(self):
    s = pd.Series(list('abc'))
    s.drop([0], inplace=True)
    assert len(s.str.lower()) == 2