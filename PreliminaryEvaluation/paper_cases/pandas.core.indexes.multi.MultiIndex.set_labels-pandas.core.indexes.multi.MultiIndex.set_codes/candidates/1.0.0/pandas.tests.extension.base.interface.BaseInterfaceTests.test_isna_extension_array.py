def test_isna_extension_array(self, data_missing):
    na = data_missing.isna()
    if is_extension_array_dtype(na):
        assert na._reduce('any')
        assert na.any()
        assert not na._reduce('all')
        assert not na.all()
        assert na.dtype._is_boolean