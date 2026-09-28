@pytest.mark.parametrize('klass', [pd.Series, pd.DataFrame])
def test_iter_raises(self, klass):
    obj = klass([1, 2, 3, 4])
    with pytest.raises(NotImplementedError):
        iter(obj.expanding(2))