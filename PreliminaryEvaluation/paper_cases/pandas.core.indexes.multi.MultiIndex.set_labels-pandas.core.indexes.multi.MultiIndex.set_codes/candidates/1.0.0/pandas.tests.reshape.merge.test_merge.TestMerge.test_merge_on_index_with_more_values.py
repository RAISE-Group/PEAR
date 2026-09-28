@pytest.mark.parametrize('how', ['right', 'outer'])
@pytest.mark.parametrize('index,expected_index', [(CategoricalIndex([1, 2, 4]), CategoricalIndex([1, 2, 4, None, None, None])), (DatetimeIndex(['2001-01-01', '2002-02-02', '2003-03-03']), DatetimeIndex(['2001-01-01', '2002-02-02', '2003-03-03', pd.NaT, pd.NaT, pd.NaT])), (Float64Index([1, 2, 3]), Float64Index([1, 2, 3, None, None, None])), (Int64Index([1, 2, 3]), Float64Index([1, 2, 3, None, None, None])), (IntervalIndex.from_tuples([(1, 2), (2, 3), (3, 4)]), IntervalIndex.from_tuples([(1, 2), (2, 3), (3, 4), np.nan, np.nan, np.nan])), (PeriodIndex(['2001-01-01', '2001-01-02', '2001-01-03'], freq='D'), PeriodIndex(['2001-01-01', '2001-01-02', '2001-01-03', pd.NaT, pd.NaT, pd.NaT], freq='D')), (TimedeltaIndex(['1d', '2d', '3d']), TimedeltaIndex(['1d', '2d', '3d', pd.NaT, pd.NaT, pd.NaT]))])
def test_merge_on_index_with_more_values(self, how, index, expected_index):
    df1 = pd.DataFrame({'a': [1, 2, 3], 'key': [0, 2, 2]}, index=index)
    df2 = pd.DataFrame({'b': [1, 2, 3, 4, 5]})
    result = df1.merge(df2, left_on='key', right_index=True, how=how)
    expected = pd.DataFrame([[1.0, 0, 1], [2.0, 2, 3], [3.0, 2, 3], [np.nan, 1, 2], [np.nan, 3, 4], [np.nan, 4, 5]], columns=['a', 'key', 'b'])
    expected.set_index(expected_index, inplace=True)
    tm.assert_frame_equal(result, expected)