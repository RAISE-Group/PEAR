@pytest.mark.parametrize('method', ['abs', 'shift', 'pct_change', 'cumsum', 'rank'])
def test_transform_method_name(self, method):
    df = pd.DataFrame({'A': [-1, 2]})
    result = df.transform(method)
    expected = operator.methodcaller(method)(df)
    tm.assert_frame_equal(result, expected)