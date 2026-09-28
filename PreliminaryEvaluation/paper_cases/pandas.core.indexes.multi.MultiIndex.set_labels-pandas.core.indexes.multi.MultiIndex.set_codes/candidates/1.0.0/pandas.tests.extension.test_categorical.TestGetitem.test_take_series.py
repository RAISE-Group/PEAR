@pytest.mark.skip(reason='GH-20747. Unobserved categories.')
def test_take_series(self, data):
    super().test_take_series(data)