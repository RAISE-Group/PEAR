@pytest.mark.parametrize('klass', [None, np.asarray, Series, Index])
def test_merge_datetime_index(self, klass):
    df = DataFrame([1, 2, 3], ['2016-01-01', '2017-01-01', '2018-01-01'], columns=['a'])
    df.index = pd.to_datetime(df.index)
    on_vector = df.index.year
    if klass is not None:
        on_vector = klass(on_vector)
    expected = DataFrame({'a': [1, 2, 3], 'key_1': [2016, 2017, 2018]})
    result = df.merge(df, on=['a', on_vector], how='inner')
    tm.assert_frame_equal(result, expected)
    expected = DataFrame({'key_0': [2016, 2017, 2018], 'a_x': [1, 2, 3], 'a_y': [1, 2, 3]})
    result = df.merge(df, on=[df.index.year], how='inner')
    tm.assert_frame_equal(result, expected)