def test_dataframe_numpy_labelled(self, orient):
    if orient in ('split', 'values'):
        pytest.skip('Incompatible with labelled=True')
    df = DataFrame([[1, 2, 3], [4, 5, 6]], index=['a', 'b'], columns=['x', 'y', 'z'], dtype=np.int)
    kwargs = {} if orient is None else dict(orient=orient)
    output = DataFrame(*ujson.decode(ujson.encode(df, **kwargs), numpy=True, labelled=True))
    if orient is None:
        df = df.T
    elif orient == 'records':
        df.index = [0, 1]
    tm.assert_frame_equal(output, df)