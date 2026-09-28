def test_compare_unordered_different_order(self):
    a = pd.Categorical(['a'], categories=['a', 'b'])
    b = pd.Categorical(['b'], categories=['b', 'a'])
    assert not a.equals(b)