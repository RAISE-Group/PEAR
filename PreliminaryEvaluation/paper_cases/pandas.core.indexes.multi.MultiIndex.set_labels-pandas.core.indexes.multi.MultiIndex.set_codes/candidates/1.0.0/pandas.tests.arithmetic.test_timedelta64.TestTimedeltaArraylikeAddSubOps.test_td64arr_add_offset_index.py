@pytest.mark.parametrize('names', [(None, None, None), ('foo', 'bar', None), ('foo', 'foo', 'foo')])
def test_td64arr_add_offset_index(self, names, box):
    if box is pd.DataFrame and names[1] == 'bar':
        pytest.skip('Name propagation for DataFrame does not behave like it does for Index/Series')
    tdi = TimedeltaIndex(['1 days 00:00:00', '3 days 04:00:00'], name=names[0])
    other = pd.Index([pd.offsets.Hour(n=1), pd.offsets.Minute(n=-2)], name=names[1])
    expected = TimedeltaIndex([tdi[n] + other[n] for n in range(len(tdi))], freq='infer', name=names[2])
    tdi = tm.box_expected(tdi, box)
    expected = tm.box_expected(expected, box)
    warn = PerformanceWarning if box is not pd.DataFrame else None
    with tm.assert_produces_warning(warn):
        res = tdi + other
    tm.assert_equal(res, expected)
    with tm.assert_produces_warning(warn):
        res2 = other + tdi
    tm.assert_equal(res2, expected)