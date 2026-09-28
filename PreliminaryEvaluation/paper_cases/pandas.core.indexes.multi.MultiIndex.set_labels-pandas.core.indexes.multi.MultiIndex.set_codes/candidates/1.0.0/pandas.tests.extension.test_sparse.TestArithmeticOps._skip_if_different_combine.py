def _skip_if_different_combine(self, data):
    if data.fill_value == 0:
        raise pytest.skip('Incorrected expected from Series.combine')