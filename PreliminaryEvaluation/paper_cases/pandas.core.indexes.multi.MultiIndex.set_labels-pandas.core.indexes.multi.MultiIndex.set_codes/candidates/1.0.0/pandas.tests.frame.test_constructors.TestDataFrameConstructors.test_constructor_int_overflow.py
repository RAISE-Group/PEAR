@pytest.mark.parametrize('values', [np.array([2 ** 64], dtype=object), np.array([2 ** 65]), [2 ** 64 + 1], np.array([-2 ** 63 - 4], dtype=object), np.array([-2 ** 64 - 1]), [-2 ** 65 - 2]])
def test_constructor_int_overflow(self, values):
    value = values[0]
    result = DataFrame(values)
    assert result[0].dtype == object
    assert result[0][0] == value