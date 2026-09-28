def test_apply_bad_labels(self):

    def f(x):
        return pd.DataFrame(index=[1, 2], columns=['a', 'b'])
    df = pd.DataFrame([[1, 2], [3, 4]])
    with pytest.raises(ValueError):
        df.style._apply(f, axis=None)