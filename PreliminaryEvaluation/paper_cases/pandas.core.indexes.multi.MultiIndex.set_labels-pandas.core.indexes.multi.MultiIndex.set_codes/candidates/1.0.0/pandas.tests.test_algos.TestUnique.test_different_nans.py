def test_different_nans(self):
    NAN1 = struct.unpack('d', struct.pack('=Q', 9221120237041090560))[0]
    NAN2 = struct.unpack('d', struct.pack('=Q', 9221120237041090561))[0]
    assert NAN1 != NAN1
    assert NAN2 != NAN2
    a = np.array([NAN1, NAN2])
    result = pd.unique(a)
    expected = np.array([np.nan])
    tm.assert_numpy_array_equal(result, expected)