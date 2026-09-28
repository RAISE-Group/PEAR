@pytest.mark.parametrize('cls_name', ['Day', 'Hour', 'Minute', 'Second', 'Milli', 'Micro', 'Nano'])
def test_dt64arr_add_sub_tick_DateOffset_smoke(self, cls_name, box_with_array):
    ser = Series([Timestamp('20130101 9:01'), Timestamp('20130101 9:02')])
    ser = tm.box_expected(ser, box_with_array)
    offset_cls = getattr(pd.offsets, cls_name)
    ser + offset_cls(5)
    offset_cls(5) + ser
    ser - offset_cls(5)