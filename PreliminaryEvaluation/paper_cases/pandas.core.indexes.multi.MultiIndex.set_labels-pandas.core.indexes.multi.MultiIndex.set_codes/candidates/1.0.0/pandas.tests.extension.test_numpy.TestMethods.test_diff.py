@pytest.mark.xfail(reason='PandasArray.diff may fail on dtype')
def test_diff(self, data, periods):
    return super().test_diff(data, periods)