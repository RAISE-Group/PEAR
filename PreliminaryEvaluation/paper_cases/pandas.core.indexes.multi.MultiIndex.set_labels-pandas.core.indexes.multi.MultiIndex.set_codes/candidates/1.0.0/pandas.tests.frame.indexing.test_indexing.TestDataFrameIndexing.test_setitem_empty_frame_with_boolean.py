@pytest.mark.parametrize('dtype', ['float', 'int64'])
@pytest.mark.parametrize('kwargs', [dict(), dict(index=[1]), dict(columns=['A'])])
def test_setitem_empty_frame_with_boolean(self, dtype, kwargs):
    kwargs['dtype'] = dtype
    df = DataFrame(**kwargs)
    df2 = df.copy()
    df[df > df2] = 47
    tm.assert_frame_equal(df, df2)