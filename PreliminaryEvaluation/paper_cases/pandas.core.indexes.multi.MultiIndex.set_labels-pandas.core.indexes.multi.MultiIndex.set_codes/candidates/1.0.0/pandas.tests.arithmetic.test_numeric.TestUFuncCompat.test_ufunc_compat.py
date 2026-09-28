@pytest.mark.parametrize('holder', [pd.Int64Index, pd.UInt64Index, pd.Float64Index, pd.RangeIndex, pd.Series])
def test_ufunc_compat(self, holder):
    box = pd.Series if holder is pd.Series else pd.Index
    if holder is pd.RangeIndex:
        idx = pd.RangeIndex(0, 5)
    else:
        idx = holder(np.arange(5, dtype='int64'))
    result = np.sin(idx)
    expected = box(np.sin(np.arange(5, dtype='int64')))
    tm.assert_equal(result, expected)