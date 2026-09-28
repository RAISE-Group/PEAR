@pytest.mark.parametrize('scalar_td', [timedelta(minutes=10, seconds=7), Timedelta('10m7s'), Timedelta('10m7s').to_timedelta64()], ids=lambda x: type(x).__name__)
def test_td64arr_rfloordiv_tdlike_scalar(self, scalar_td, box_with_array):
    tdi = TimedeltaIndex(['00:05:03', '00:05:03', pd.NaT], freq=None)
    expected = pd.Index([2.0, 2.0, np.nan])
    tdi = tm.box_expected(tdi, box_with_array, transpose=False)
    expected = tm.box_expected(expected, box_with_array, transpose=False)
    res = tdi.__rfloordiv__(scalar_td)
    tm.assert_equal(res, expected)
    expected = pd.Index([0.0, 0.0, np.nan])
    expected = tm.box_expected(expected, box_with_array, transpose=False)
    res = tdi // scalar_td
    tm.assert_equal(res, expected)