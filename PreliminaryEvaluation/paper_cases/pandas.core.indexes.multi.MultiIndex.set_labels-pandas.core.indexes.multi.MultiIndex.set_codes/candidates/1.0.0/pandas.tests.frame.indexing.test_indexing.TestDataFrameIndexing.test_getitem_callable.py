def test_getitem_callable(self, float_frame):
    result = float_frame[lambda x: 'A']
    tm.assert_series_equal(result, float_frame.loc[:, 'A'])
    result = float_frame[lambda x: ['A', 'B']]
    tm.assert_frame_equal(result, float_frame.loc[:, ['A', 'B']])
    df = float_frame[:3]
    result = df[lambda x: [True, False, True]]
    tm.assert_frame_equal(result, float_frame.iloc[[0, 2], :])