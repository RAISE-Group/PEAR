def test_pivot_table_categorical_observed_equal(self, observed):
    df = pd.DataFrame({'col1': list('abcde'), 'col2': list('fghij'), 'col3': [1, 2, 3, 4, 5]})
    expected = df.pivot_table(index='col1', values='col3', columns='col2', aggfunc=np.sum, fill_value=0)
    expected.index = expected.index.astype('category')
    expected.columns = expected.columns.astype('category')
    df.col1 = df.col1.astype('category')
    df.col2 = df.col2.astype('category')
    result = df.pivot_table(index='col1', values='col3', columns='col2', aggfunc=np.sum, fill_value=0, observed=observed)
    tm.assert_frame_equal(result, expected)