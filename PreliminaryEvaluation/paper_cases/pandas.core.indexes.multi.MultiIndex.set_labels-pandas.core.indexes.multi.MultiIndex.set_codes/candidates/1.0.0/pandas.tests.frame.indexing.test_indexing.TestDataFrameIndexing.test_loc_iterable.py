@pytest.mark.parametrize('key_type', [iter, np.array, Series, Index])
def test_loc_iterable(self, float_frame, key_type):
    idx = key_type(['A', 'B', 'C'])
    result = float_frame.loc[:, idx]
    expected = float_frame.loc[:, ['A', 'B', 'C']]
    tm.assert_frame_equal(result, expected)