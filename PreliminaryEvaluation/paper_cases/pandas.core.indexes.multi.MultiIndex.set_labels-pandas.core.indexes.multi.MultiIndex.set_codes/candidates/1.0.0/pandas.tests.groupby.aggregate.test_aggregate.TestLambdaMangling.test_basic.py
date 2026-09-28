def test_basic(self):
    df = pd.DataFrame({'A': [0, 0, 1, 1], 'B': [1, 2, 3, 4]})
    result = df.groupby('A').agg({'B': [lambda x: 0, lambda x: 1]})
    expected = pd.DataFrame({('B', '<lambda_0>'): [0, 0], ('B', '<lambda_1>'): [1, 1]}, index=pd.Index([0, 1], name='A'))
    tm.assert_frame_equal(result, expected)