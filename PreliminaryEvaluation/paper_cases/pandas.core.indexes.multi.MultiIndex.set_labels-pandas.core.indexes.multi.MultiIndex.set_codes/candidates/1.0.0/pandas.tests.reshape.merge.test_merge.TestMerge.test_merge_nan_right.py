def test_merge_nan_right(self):
    df1 = DataFrame({'i1': [0, 1], 'i2': [0, 1]})
    df2 = DataFrame({'i1': [0], 'i3': [0]})
    result = df1.join(df2, on='i1', rsuffix='_')
    expected = DataFrame({'i1': {0: 0.0, 1: 1}, 'i2': {0: 0, 1: 1}, 'i1_': {0: 0, 1: np.nan}, 'i3': {0: 0.0, 1: np.nan}, None: {0: 0, 1: 0}}).set_index(None).reset_index()[['i1', 'i2', 'i1_', 'i3']]
    tm.assert_frame_equal(result, expected, check_dtype=False)
    df1 = DataFrame({'i1': [0, 1], 'i2': [0.5, 1.5]})
    df2 = DataFrame({'i1': [0], 'i3': [0.7]})
    result = df1.join(df2, rsuffix='_', on='i1')
    expected = DataFrame({'i1': {0: 0, 1: 1}, 'i1_': {0: 0.0, 1: np.nan}, 'i2': {0: 0.5, 1: 1.5}, 'i3': {0: 0.7, 1: np.nan}})[['i1', 'i2', 'i1_', 'i3']]
    tm.assert_frame_equal(result, expected)