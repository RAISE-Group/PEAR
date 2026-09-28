@pytest.mark.parametrize('dims', [1, 2])
def test_iloc_getitem_invalid_scalar(self, dims):
    if dims == 1:
        s = Series(np.arange(10))
    else:
        s = DataFrame(np.arange(100).reshape(10, 10))
    with pytest.raises(TypeError, match='Cannot index by location index'):
        s.iloc['a']