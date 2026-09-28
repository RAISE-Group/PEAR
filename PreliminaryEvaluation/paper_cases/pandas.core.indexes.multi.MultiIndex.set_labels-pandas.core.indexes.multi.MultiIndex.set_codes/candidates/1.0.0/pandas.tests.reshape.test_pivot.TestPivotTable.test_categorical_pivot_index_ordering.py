def test_categorical_pivot_index_ordering(self, observed):
    df = pd.DataFrame({'Sales': [100, 120, 220], 'Month': ['January', 'January', 'January'], 'Year': [2013, 2014, 2013]})
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    df['Month'] = df['Month'].astype('category').cat.set_categories(months)
    result = df.pivot_table(values='Sales', index='Month', columns='Year', dropna=observed, aggfunc='sum')
    expected_columns = pd.Int64Index([2013, 2014], name='Year')
    expected_index = pd.CategoricalIndex(['January'], categories=months, ordered=False, name='Month')
    expected = pd.DataFrame([[320, 120]], index=expected_index, columns=expected_columns)
    if not observed:
        result = result.dropna().astype(np.int64)
    tm.assert_frame_equal(result, expected)