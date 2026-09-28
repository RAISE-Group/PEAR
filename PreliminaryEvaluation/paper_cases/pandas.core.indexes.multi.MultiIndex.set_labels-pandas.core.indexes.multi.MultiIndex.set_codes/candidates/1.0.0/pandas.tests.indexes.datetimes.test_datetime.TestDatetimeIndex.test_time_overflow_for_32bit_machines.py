def test_time_overflow_for_32bit_machines(self):
    periods = np.int_(1000)
    idx1 = pd.date_range(start='2000', periods=periods, freq='S')
    assert len(idx1) == periods
    idx2 = pd.date_range(end='2000', periods=periods, freq='S')
    assert len(idx2) == periods