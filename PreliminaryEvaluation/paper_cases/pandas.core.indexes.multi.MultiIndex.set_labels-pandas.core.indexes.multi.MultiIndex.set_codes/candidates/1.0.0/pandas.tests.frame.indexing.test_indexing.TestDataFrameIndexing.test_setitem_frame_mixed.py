def test_setitem_frame_mixed(self, float_string_frame):
    f = float_string_frame.copy()
    piece = DataFrame([[1.0, 2.0], [3.0, 4.0]], index=f.index[0:2], columns=['A', 'B'])
    key = (slice(None, 2), ['A', 'B'])
    f.loc[key] = piece
    tm.assert_almost_equal(f.loc[f.index[0:2], ['A', 'B']].values, piece.values)
    f = float_string_frame.copy()
    piece = DataFrame([[1.0, 2.0], [3.0, 4.0], [5.0, 6.0], [7.0, 8.0]], index=list(f.index[0:2]) + ['foo', 'bar'], columns=['A', 'B'])
    key = (slice(None, 2), ['A', 'B'])
    f.loc[key] = piece
    tm.assert_almost_equal(f.loc[f.index[0:2], ['A', 'B']].values, piece.values[0:2])
    f = float_string_frame.copy()
    piece = f.loc[f.index[:2], ['A']]
    piece.index = f.index[-2:]
    key = (slice(-2, None), ['A', 'B'])
    f.loc[key] = piece
    piece['B'] = np.nan
    tm.assert_almost_equal(f.loc[f.index[-2:], ['A', 'B']].values, piece.values)
    f = float_string_frame.copy()
    piece = float_string_frame.loc[f.index[:2], ['A', 'B']]
    key = (slice(-2, None), ['A', 'B'])
    f.loc[key] = piece.values
    tm.assert_almost_equal(f.loc[f.index[-2:], ['A', 'B']].values, piece.values)