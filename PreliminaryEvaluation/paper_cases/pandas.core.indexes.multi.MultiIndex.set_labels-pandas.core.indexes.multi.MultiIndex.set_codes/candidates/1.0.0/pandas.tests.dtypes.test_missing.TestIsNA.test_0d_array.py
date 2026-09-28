def test_0d_array(self):
    assert isna(np.array(np.nan))
    assert not isna(np.array(0.0))
    assert not isna(np.array(0))
    assert isna(np.array(np.nan, dtype=object))
    assert not isna(np.array(0.0, dtype=object))
    assert not isna(np.array(0, dtype=object))