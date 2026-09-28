@pytest.mark.parametrize('test_input,error_type', [(pd.Series([], dtype='float64'), ValueError), (pd.Series(['foo', 'bar', 'baz']), TypeError), (pd.Series([(1,), (2,)]), TypeError), (pd.Series(['foo', 'foo', 'bar', 'bar', None, np.nan, 'baz']), TypeError)])
def test_assert_idxminmax_raises(self, test_input, error_type):
    """
        Cases where ``Series.argmax`` and related should raise an exception
        """
    with pytest.raises(error_type):
        test_input.idxmin()
    with pytest.raises(error_type):
        test_input.idxmin(skipna=False)
    with pytest.raises(error_type):
        test_input.idxmax()
    with pytest.raises(error_type):
        test_input.idxmax(skipna=False)