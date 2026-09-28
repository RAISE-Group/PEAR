def test_transform_and_agg_err(self, axis, float_frame):
    with pytest.raises(ValueError):
        float_frame.transform(['max', 'min'], axis=axis)
    with pytest.raises(ValueError):
        with np.errstate(all='ignore'):
            float_frame.agg(['max', 'sqrt'], axis=axis)
    with pytest.raises(ValueError):
        with np.errstate(all='ignore'):
            float_frame.transform(['max', 'sqrt'], axis=axis)
    df = pd.DataFrame({'A': range(5), 'B': 5})

    def f():
        with np.errstate(all='ignore'):
            df.agg({'A': ['abs', 'sum'], 'B': ['mean', 'max']}, axis=axis)