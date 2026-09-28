@pytest.mark.skip(reason='test not written correctly for categorical')
def test_reindex(self, data, na_value):
    super().test_reindex(data, na_value)