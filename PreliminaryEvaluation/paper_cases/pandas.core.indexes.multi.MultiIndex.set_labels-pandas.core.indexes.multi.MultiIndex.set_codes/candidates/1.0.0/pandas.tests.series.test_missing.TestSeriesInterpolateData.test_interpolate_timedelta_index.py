def test_interpolate_timedelta_index(self, interp_methods_ind):
    """
        Tests for non numerical index types  - object, period, timedelta
        Note that all methods except time, index, nearest and values
        are tested here.
        """
    ind = pd.timedelta_range(start=1, periods=4)
    df = pd.DataFrame([0, 1, np.nan, 3], index=ind)
    method, kwargs = interp_methods_ind
    if method == 'pchip':
        pytest.importorskip('scipy')
    if method in {'linear', 'pchip'}:
        result = df[0].interpolate(method=method, **kwargs)
        expected = pd.Series([0.0, 1.0, 2.0, 3.0], name=0, index=ind)
        tm.assert_series_equal(result, expected)
    else:
        pytest.skip('This interpolation method is not supported for Timedelta Index yet.')