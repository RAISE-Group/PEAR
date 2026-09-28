@pytest.mark.parametrize('orient', ['split', 'values'])
@pytest.mark.parametrize('data', [[['a', 'b'], ['c', 'd']], [[1.5, 2.5], [3.5, 4.5]], [[1, 2.5], [3, 4.5]], [[Timestamp('20130101'), 3.5], [Timestamp('20130102'), 4.5]]])
def test_frame_non_unique_columns(self, orient, data):
    df = DataFrame(data, index=[1, 2], columns=['x', 'x'])
    result = read_json(df.to_json(orient=orient), orient=orient, convert_dates=['x'])
    if orient == 'values':
        expected = pd.DataFrame(data)
        if expected.iloc[:, 0].dtype == 'datetime64[ns]':
            expected.iloc[:, 0] = expected.iloc[:, 0].astype(np.int64) // 1000000
    elif orient == 'split':
        expected = df
    tm.assert_frame_equal(result, expected)