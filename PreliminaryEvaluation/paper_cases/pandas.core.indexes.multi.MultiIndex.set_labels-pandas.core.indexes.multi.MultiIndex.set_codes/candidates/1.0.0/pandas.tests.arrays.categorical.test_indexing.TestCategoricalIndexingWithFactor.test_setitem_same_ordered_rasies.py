@pytest.mark.parametrize('other', [pd.Categorical(['b', 'a']), pd.Categorical(['b', 'a'], categories=['b', 'a'], ordered=True), pd.Categorical(['b', 'a'], categories=['a', 'b', 'c'], ordered=True)])
def test_setitem_same_ordered_rasies(self, other):
    target = pd.Categorical(['a', 'b'], categories=['a', 'b'], ordered=True)
    mask = np.array([True, False])
    msg = 'Cannot set a Categorical with another, without identical categories'
    with pytest.raises(ValueError, match=msg):
        target[mask] = other[mask]