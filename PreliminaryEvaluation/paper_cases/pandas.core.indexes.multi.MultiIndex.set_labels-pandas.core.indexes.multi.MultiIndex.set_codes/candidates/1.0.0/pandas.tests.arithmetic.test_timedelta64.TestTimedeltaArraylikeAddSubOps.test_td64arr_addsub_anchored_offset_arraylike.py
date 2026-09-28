@pytest.mark.parametrize('obox', [np.array, pd.Index, pd.Series])
def test_td64arr_addsub_anchored_offset_arraylike(self, obox, box_with_array):
    tdi = TimedeltaIndex(['1 days 00:00:00', '3 days 04:00:00'])
    tdi = tm.box_expected(tdi, box_with_array)
    anchored = obox([pd.offsets.MonthEnd(), pd.offsets.Day(n=2)])
    with pytest.raises(TypeError):
        with tm.assert_produces_warning(PerformanceWarning):
            tdi + anchored
    with pytest.raises(TypeError):
        with tm.assert_produces_warning(PerformanceWarning):
            anchored + tdi
    with pytest.raises(TypeError):
        with tm.assert_produces_warning(PerformanceWarning):
            tdi - anchored
    with pytest.raises(TypeError):
        with tm.assert_produces_warning(PerformanceWarning):
            anchored - tdi