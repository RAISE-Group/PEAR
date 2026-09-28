def test_first_nan_kept(self):
    bits_for_nan1 = 18444492273895866369
    bits_for_nan2 = 9221120237041090561
    NAN1 = struct.unpack('d', struct.pack('=Q', bits_for_nan1))[0]
    NAN2 = struct.unpack('d', struct.pack('=Q', bits_for_nan2))[0]
    assert NAN1 != NAN1
    assert NAN2 != NAN2
    for el_type in [np.float64, np.object]:
        a = np.array([NAN1, NAN2], dtype=el_type)
        result = pd.unique(a)
        assert result.size == 1
        result_nan_bits = struct.unpack('=Q', struct.pack('d', result[0]))[0]
        assert result_nan_bits == bits_for_nan1