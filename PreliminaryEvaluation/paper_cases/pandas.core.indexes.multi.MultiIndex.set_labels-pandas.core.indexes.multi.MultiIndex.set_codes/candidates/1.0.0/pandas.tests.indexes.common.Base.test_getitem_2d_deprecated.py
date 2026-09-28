def test_getitem_2d_deprecated(self):
    idx = self.create_index()
    with tm.assert_produces_warning(DeprecationWarning, check_stacklevel=False):
        res = idx[:, None]
    assert isinstance(res, np.ndarray), type(res)