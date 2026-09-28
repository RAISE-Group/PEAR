def test_stack_dropna(self):
    df = DataFrame({'A': ['a1', 'a2'], 'B': ['b1', 'b2'], 'C': [1, 1]})
    df = df.set_index(['A', 'B'])
    stacked = df.unstack().stack(dropna=False)
    assert len(stacked) > len(stacked.dropna())
    stacked = df.unstack().stack(dropna=True)
    tm.assert_frame_equal(stacked, stacked.dropna())