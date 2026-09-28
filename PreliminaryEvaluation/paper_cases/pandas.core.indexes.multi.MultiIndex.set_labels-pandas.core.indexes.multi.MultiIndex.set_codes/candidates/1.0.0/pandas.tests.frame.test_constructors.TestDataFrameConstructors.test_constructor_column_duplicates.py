def test_constructor_column_duplicates(self):
    df = DataFrame([[8, 5]], columns=['a', 'a'])
    edf = DataFrame([[8, 5]])
    edf.columns = ['a', 'a']
    tm.assert_frame_equal(df, edf)
    idf = DataFrame.from_records([(8, 5)], columns=['a', 'a'])
    tm.assert_frame_equal(idf, edf)
    msg = 'If using all scalar values, you must pass an index'
    with pytest.raises(ValueError, match=msg):
        DataFrame.from_dict(OrderedDict([('b', 8), ('a', 5), ('a', 6)]))