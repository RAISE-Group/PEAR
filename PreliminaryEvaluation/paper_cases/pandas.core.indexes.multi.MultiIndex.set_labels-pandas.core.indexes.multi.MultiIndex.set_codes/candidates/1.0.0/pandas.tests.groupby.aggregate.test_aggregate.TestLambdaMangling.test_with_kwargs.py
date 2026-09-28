@pytest.mark.xfail(reason='GH-26611. kwargs for multi-agg.')
def test_with_kwargs(self):
    f1 = lambda x, y, b=1: x.sum() + y + b
    f2 = lambda x, y, b=2: x.sum() + y * b
    result = pd.Series([1, 2]).groupby([0, 0]).agg([f1, f2], 0)
    expected = pd.DataFrame({'<lambda_0>': [4], '<lambda_1>': [6]})
    tm.assert_frame_equal(result, expected)
    result = pd.Series([1, 2]).groupby([0, 0]).agg([f1, f2], 0, b=10)
    expected = pd.DataFrame({'<lambda_0>': [13], '<lambda_1>': [30]})
    tm.assert_frame_equal(result, expected)