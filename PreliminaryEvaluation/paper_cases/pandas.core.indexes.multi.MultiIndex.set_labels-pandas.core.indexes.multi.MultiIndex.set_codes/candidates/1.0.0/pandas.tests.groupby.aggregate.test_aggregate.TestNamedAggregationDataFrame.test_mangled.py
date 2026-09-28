def test_mangled(self):
    df = pd.DataFrame({'A': [0, 1], 'B': [1, 2], 'C': [3, 4]})
    result = df.groupby('A').agg(b=('B', lambda x: 0), c=('C', lambda x: 1))
    expected = pd.DataFrame({'b': [0, 0], 'c': [1, 1]}, index=pd.Index([0, 1], name='A'))
    tm.assert_frame_equal(result, expected)