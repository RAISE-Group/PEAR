def test_concat_single_with_key(self):
    df = DataFrame(np.random.randn(10, 4))
    result = concat([df], keys=['foo'])
    expected = concat([df, df], keys=['foo', 'bar'])
    tm.assert_frame_equal(result, expected[:10])