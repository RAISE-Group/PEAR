@pytest.mark.parametrize('attr_name', ['_start', '_stop', '_step'])
def test_deprecated_start_stop_step_attrs(self, attr_name):
    idx = self.create_index()
    with tm.assert_produces_warning(FutureWarning):
        getattr(idx, attr_name)