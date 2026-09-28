def test_negative_ordinals(self):
    Period(ordinal=-1000, freq='A')
    Period(ordinal=0, freq='A')
    idx1 = PeriodIndex(ordinal=[-1, 0, 1], freq='A')
    idx2 = PeriodIndex(ordinal=np.array([-1, 0, 1]), freq='A')
    tm.assert_index_equal(idx1, idx2)