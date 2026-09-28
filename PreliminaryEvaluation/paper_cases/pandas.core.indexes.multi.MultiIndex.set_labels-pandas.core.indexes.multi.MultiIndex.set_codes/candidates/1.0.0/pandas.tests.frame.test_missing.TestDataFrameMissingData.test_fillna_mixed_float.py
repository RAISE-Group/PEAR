def test_fillna_mixed_float(self, mixed_float_frame):
    mf = mixed_float_frame.reindex(columns=['A', 'B', 'D'])
    mf.loc[mf.index[-10:], 'A'] = np.nan
    result = mf.fillna(value=0)
    _check_mixed_float(result, dtype=dict(C=None))
    result = mf.fillna(method='pad')
    _check_mixed_float(result, dtype=dict(C=None))