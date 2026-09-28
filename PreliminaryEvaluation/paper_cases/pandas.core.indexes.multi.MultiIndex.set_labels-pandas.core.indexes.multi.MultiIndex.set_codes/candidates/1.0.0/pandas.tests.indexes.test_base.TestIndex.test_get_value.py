@pytest.mark.parametrize('index', ['string', 'int', 'datetime', 'timedelta'], indirect=True)
def test_get_value(self, index):
    values = np.random.randn(100)
    value = index[67]
    tm.assert_almost_equal(index.get_value(values, value), values[67])