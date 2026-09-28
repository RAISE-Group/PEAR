@pytest.mark.parametrize('periods,fill_method,limit,exp', [(1, 'ffill', None, [np.nan, np.nan, np.nan, 1, 1, 1.5, 0, 0]), (1, 'ffill', 1, [np.nan, np.nan, np.nan, 1, 1, 1.5, 0, np.nan]), (1, 'bfill', None, [np.nan, 0, 0, 1, 1, 1.5, np.nan, np.nan]), (1, 'bfill', 1, [np.nan, np.nan, 0, 1, 1, 1.5, np.nan, np.nan]), (-1, 'ffill', None, [np.nan, np.nan, -0.5, -0.5, -0.6, 0, 0, np.nan]), (-1, 'ffill', 1, [np.nan, np.nan, -0.5, -0.5, -0.6, 0, np.nan, np.nan]), (-1, 'bfill', None, [0, 0, -0.5, -0.5, -0.6, np.nan, np.nan, np.nan]), (-1, 'bfill', 1, [np.nan, 0, -0.5, -0.5, -0.6, np.nan, np.nan, np.nan])])
def test_pct_change(self, periods, fill_method, limit, exp):
    vals = [np.nan, np.nan, 1, 2, 4, 10, np.nan, np.nan]
    obj = self._typ(vals)
    func = getattr(obj, 'pct_change')
    res = func(periods=periods, fill_method=fill_method, limit=limit)
    if type(obj) is DataFrame:
        tm.assert_frame_equal(res, DataFrame(exp))
    else:
        tm.assert_series_equal(res, Series(exp))