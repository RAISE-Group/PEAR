def test_getitem_boolean_list(self):
    df = DataFrame(np.arange(12).reshape(3, 4))

    def _checkit(lst):
        result = df[lst]
        expected = df.loc[df.index[lst]]
        tm.assert_frame_equal(result, expected)
    _checkit([True, False, True])
    _checkit([True, True, True])
    _checkit([False, False, False])