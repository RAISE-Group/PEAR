def test_info_categorical(self):
    idx = pd.CategoricalIndex(['a', 'b'])
    df = pd.DataFrame(np.zeros((2, 2)), index=idx, columns=idx)
    buf = StringIO()
    df.info(buf=buf)