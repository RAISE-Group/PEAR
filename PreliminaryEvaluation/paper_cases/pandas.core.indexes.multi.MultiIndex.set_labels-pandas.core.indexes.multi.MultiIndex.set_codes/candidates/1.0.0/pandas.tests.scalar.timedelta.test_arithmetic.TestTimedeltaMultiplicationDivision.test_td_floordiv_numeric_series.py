def test_td_floordiv_numeric_series(self):
    td = Timedelta(hours=3, minutes=4)
    ser = pd.Series([1], dtype=np.int64)
    res = td // ser
    assert res.dtype.kind == 'm'