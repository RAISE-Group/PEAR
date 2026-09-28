@skip_nested
@pytest.mark.parametrize('box', [pd.Series, lambda x: x])
@pytest.mark.parametrize('method', [lambda x: x.unique(), pd.unique])
def test_unique(self, data, box, method):
    super().test_unique(data, box, method)