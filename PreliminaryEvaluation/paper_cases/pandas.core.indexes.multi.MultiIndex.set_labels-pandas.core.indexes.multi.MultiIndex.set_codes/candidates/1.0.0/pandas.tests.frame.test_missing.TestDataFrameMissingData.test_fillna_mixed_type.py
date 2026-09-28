def test_fillna_mixed_type(self, float_string_frame):
    mf = float_string_frame
    mf.loc[mf.index[5:20], 'foo'] = np.nan
    mf.loc[mf.index[-10:], 'A'] = np.nan
    mf.fillna(value=0)
    mf.fillna(method='pad')