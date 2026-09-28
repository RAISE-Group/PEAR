def test_getitem_2d_deprecated(self):
    idx = self.create_index()
    with pytest.raises(ValueError, match='multi-dimensional indexing not allowed'):
        with tm.assert_produces_warning(DeprecationWarning, check_stacklevel=False):
            idx[:, None]