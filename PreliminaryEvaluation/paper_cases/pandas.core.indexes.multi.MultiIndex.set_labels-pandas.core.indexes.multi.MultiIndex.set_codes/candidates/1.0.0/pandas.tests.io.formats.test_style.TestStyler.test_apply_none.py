def test_apply_none(self):

    def f(x):
        return pd.DataFrame(np.where(x == x.max(), 'color: red', ''), index=x.index, columns=x.columns)
    result = pd.DataFrame([[1, 2], [3, 4]]).style.apply(f, axis=None)._compute().ctx
    assert result[1, 1] == ['color: red']