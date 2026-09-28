def test_select_dtypes_duplicate_columns(self):
    odict = OrderedDict
    df = DataFrame(odict([('a', list('abc')), ('b', list(range(1, 4))), ('c', np.arange(3, 6).astype('u1')), ('d', np.arange(4.0, 7.0, dtype='float64')), ('e', [True, False, True]), ('f', pd.date_range('now', periods=3).values)]))
    df.columns = ['a', 'a', 'b', 'b', 'b', 'c']
    expected = DataFrame({'a': list(range(1, 4)), 'b': np.arange(3, 6).astype('u1')})
    result = df.select_dtypes(include=[np.number], exclude=['floating'])
    tm.assert_frame_equal(result, expected)