def test_replace_swapping_bug(self):
    df = pd.DataFrame({'a': [True, False, True]})
    res = df.replace({'a': {True: 'Y', False: 'N'}})
    expect = pd.DataFrame({'a': ['Y', 'N', 'Y']})
    tm.assert_frame_equal(res, expect)
    df = pd.DataFrame({'a': [0, 1, 0]})
    res = df.replace({'a': {0: 'Y', 1: 'N'}})
    expect = pd.DataFrame({'a': ['Y', 'N', 'Y']})
    tm.assert_frame_equal(res, expect)