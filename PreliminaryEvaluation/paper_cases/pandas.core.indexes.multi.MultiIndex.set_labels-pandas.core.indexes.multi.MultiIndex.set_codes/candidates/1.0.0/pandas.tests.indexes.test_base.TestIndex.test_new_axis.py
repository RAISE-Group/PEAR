@pytest.mark.parametrize('index', ['datetime'], indirect=True)
def test_new_axis(self, index):
    with tm.assert_produces_warning(DeprecationWarning):
        new_index = index[None, :]
    assert new_index.ndim == 2
    assert isinstance(new_index, np.ndarray)