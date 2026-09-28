def test_concat_keys_with_none(self):
    df0 = DataFrame([[10, 20, 30], [10, 20, 30], [10, 20, 30]])
    result = concat(dict(a=None, b=df0, c=df0[:2], d=df0[:1], e=df0))
    expected = concat(dict(b=df0, c=df0[:2], d=df0[:1], e=df0))
    tm.assert_frame_equal(result, expected)
    result = concat([None, df0, df0[:2], df0[:1], df0], keys=['a', 'b', 'c', 'd', 'e'])
    expected = concat([df0, df0[:2], df0[:1], df0], keys=['b', 'c', 'd', 'e'])
    tm.assert_frame_equal(result, expected)