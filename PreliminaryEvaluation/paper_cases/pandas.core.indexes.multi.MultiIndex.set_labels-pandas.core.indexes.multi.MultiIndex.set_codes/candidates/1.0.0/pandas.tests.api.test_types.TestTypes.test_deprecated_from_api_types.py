def test_deprecated_from_api_types(self):
    for t in self.deprecated:
        with tm.assert_produces_warning(FutureWarning, check_stacklevel=False):
            getattr(types, t)(1)