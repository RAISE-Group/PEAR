def test_replace_dict_tuple_list_ordering_remains_the_same(self):
    df = DataFrame(dict(A=[np.nan, 1]))
    res1 = df.replace(to_replace={np.nan: 0, 1: -100000000.0})
    res2 = df.replace(to_replace=(1, np.nan), value=[-100000000.0, 0])
    res3 = df.replace(to_replace=[1, np.nan], value=[-100000000.0, 0])
    expected = DataFrame({'A': [0, -100000000.0]})
    tm.assert_frame_equal(res1, res2)
    tm.assert_frame_equal(res2, res3)
    tm.assert_frame_equal(res3, expected)