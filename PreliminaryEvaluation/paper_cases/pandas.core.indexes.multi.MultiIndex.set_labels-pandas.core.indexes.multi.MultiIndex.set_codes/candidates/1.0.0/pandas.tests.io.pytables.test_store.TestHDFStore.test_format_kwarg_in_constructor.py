def test_format_kwarg_in_constructor(self, setup_path):
    msg = 'format is not a defined argument for HDFStore'
    with ensure_clean_path(setup_path) as path:
        with pytest.raises(ValueError, match=msg):
            HDFStore(path, format='table')