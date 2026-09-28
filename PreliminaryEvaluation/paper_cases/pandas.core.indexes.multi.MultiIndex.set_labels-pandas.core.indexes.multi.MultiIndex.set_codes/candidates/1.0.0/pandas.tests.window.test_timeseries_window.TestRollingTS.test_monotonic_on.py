def test_monotonic_on(self):
    df = DataFrame({'A': date_range('20130101', periods=5, freq='s'), 'B': range(5)})
    assert df.A.is_monotonic
    df.rolling('2s', on='A').sum()
    df = df.set_index('A')
    assert df.index.is_monotonic
    df.rolling('2s').sum()