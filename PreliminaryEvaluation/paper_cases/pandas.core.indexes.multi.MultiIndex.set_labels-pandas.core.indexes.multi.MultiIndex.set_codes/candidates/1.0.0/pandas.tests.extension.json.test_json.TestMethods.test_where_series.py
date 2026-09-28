@pytest.mark.skip(reason='broadcasting error')
def test_where_series(self, data, na_value):
    super().test_where_series(data, na_value)