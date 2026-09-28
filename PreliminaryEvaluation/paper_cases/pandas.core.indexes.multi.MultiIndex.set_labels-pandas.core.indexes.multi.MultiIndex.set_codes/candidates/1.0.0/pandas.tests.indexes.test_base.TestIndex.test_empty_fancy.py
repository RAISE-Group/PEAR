@pytest.mark.parametrize('index', ['string', 'int', 'float'], indirect=True)
@pytest.mark.parametrize('dtype', [np.int_, np.bool_])
def test_empty_fancy(self, index, dtype):
    empty_arr = np.array([], dtype=dtype)
    empty_index = type(index)([])
    assert index[[]].identical(empty_index)
    assert index[empty_arr].identical(empty_index)