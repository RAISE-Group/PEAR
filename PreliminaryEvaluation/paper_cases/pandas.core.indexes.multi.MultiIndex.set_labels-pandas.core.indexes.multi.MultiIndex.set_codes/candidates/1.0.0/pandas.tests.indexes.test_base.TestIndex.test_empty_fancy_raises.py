@pytest.mark.parametrize('index', ['string', 'int', 'float'], indirect=True)
def test_empty_fancy_raises(self, index):
    empty_farr = np.array([], dtype=np.float_)
    empty_index = type(index)([])
    assert index[[]].identical(empty_index)
    msg = 'arrays used as indices must be of integer \\(or boolean\\) type'
    with pytest.raises(IndexError, match=msg):
        index[empty_farr]