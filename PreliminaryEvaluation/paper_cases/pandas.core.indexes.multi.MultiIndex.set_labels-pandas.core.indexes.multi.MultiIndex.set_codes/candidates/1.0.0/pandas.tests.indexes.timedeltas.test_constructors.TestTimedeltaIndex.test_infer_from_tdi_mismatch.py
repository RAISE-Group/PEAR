def test_infer_from_tdi_mismatch(self):
    tdi = pd.timedelta_range('1 second', periods=100, freq='1s')
    msg = 'Inferred frequency .* from passed values does not conform to passed frequency'
    with pytest.raises(ValueError, match=msg):
        TimedeltaIndex(tdi, freq='D')
    with pytest.raises(ValueError, match=msg):
        TimedeltaArray(tdi, freq='D')