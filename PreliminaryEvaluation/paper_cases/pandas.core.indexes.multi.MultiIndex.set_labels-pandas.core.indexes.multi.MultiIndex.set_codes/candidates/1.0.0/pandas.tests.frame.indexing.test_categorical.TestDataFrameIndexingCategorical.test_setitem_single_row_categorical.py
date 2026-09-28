def test_setitem_single_row_categorical(self):
    df = DataFrame({'Alpha': ['a'], 'Numeric': [0]})
    categories = pd.Categorical(df['Alpha'], categories=['a', 'b', 'c'])
    df.loc[:, 'Alpha'] = categories
    result = df['Alpha']
    expected = Series(categories, index=df.index, name='Alpha')
    tm.assert_series_equal(result, expected)