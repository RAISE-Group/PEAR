def test_infer_from_tdi(self):
    tdi = pd.timedelta_range('1 second', periods=10 ** 7, freq='1s')
    result = pd.TimedeltaIndex(tdi, freq='infer')
    assert result.freq == tdi.freq
    assert 'inferred_freq' not in getattr(result, '_cache', {})