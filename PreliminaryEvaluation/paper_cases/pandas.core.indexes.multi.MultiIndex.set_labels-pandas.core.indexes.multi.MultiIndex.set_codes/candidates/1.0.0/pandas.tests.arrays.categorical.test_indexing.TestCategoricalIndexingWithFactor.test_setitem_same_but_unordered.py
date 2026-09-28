@pytest.mark.parametrize('other', [pd.Categorical(['b', 'a']), pd.Categorical(['b', 'a'], categories=['b', 'a'])])
def test_setitem_same_but_unordered(self, other):
    target = pd.Categorical(['a', 'b'], categories=['a', 'b'])
    mask = np.array([True, False])
    target[mask] = other[mask]
    expected = pd.Categorical(['b', 'b'], categories=['a', 'b'])
    tm.assert_categorical_equal(target, expected)