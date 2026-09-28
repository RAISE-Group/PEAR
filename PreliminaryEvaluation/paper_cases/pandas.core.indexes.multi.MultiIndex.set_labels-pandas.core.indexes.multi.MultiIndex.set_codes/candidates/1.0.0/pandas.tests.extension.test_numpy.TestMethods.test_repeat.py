@skip_nested
@pytest.mark.parametrize('repeats', [0, 1, 2, [1, 2, 3]])
def test_repeat(self, data, repeats, as_series, use_numpy):
    super().test_repeat(data, repeats, as_series, use_numpy)