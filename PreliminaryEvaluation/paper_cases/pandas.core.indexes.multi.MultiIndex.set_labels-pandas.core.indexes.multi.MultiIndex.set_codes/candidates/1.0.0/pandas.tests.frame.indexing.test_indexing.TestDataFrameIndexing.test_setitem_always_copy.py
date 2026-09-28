def test_setitem_always_copy(self, float_frame):
    s = float_frame['A'].copy()
    float_frame['E'] = s
    float_frame['E'][5:10] = np.nan
    assert notna(s[5:10]).all()