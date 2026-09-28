@pytest.mark.xfail(reason='GH#20441: setitem on extension types.')
def test_setitem_tuple_index(self, data):
    s = pd.Series(data[:2], index=[(0, 0), (0, 1)])
    expected = pd.Series(data.take([1, 1]), index=s.index)
    s[0, 1] = data[1]
    self.assert_series_equal(s, expected)