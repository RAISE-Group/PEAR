@pytest.mark.parametrize('obj', ['series', 'frame'])
def test_unstack(self, obj):
    data = DatetimeArray._from_sequence(['2000', '2001', '2002', '2003'], tz='US/Central')
    index = pd.MultiIndex.from_product([['A', 'B'], ['a', 'b']], names=['a', 'b'])
    if obj == 'series':
        ser = pd.Series(data, index=index)
        expected = pd.DataFrame({'A': data.take([0, 1]), 'B': data.take([2, 3])}, index=pd.Index(['a', 'b'], name='b'))
        expected.columns.name = 'a'
    else:
        ser = pd.DataFrame({'A': data, 'B': data}, index=index)
        expected = pd.DataFrame({('A', 'A'): data.take([0, 1]), ('A', 'B'): data.take([2, 3]), ('B', 'A'): data.take([0, 1]), ('B', 'B'): data.take([2, 3])}, index=pd.Index(['a', 'b'], name='b'))
        expected.columns.names = [None, 'a']
    result = ser.unstack(0)
    self.assert_equal(result, expected)