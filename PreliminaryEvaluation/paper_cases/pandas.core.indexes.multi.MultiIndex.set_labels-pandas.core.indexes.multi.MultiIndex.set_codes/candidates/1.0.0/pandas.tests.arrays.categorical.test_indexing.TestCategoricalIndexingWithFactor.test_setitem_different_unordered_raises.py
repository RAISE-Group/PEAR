@pytest.mark.parametrize('other', [pd.Categorical(['b', 'a'], categories=['b', 'a', 'c']), pd.Categorical(['b', 'a'], categories=['a', 'b', 'c']), pd.Categorical(['a', 'a'], categories=['a']), pd.Categorical(['b', 'b'], categories=['b'])])
def test_setitem_different_unordered_raises(self, other):
    target = pd.Categorical(['a', 'b'], categories=['a', 'b'])
    mask = np.array([True, False])
    msg = 'Cannot set a Categorical with another, without identical categories'
    with pytest.raises(ValueError, match=msg):
        target[mask] = other[mask]