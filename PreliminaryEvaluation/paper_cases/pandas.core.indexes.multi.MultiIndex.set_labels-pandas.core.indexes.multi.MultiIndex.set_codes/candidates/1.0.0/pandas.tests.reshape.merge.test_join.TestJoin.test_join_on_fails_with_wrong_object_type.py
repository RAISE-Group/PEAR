@pytest.mark.parametrize('wrong_type', [2, 'str', None, np.array([0, 1])])
def test_join_on_fails_with_wrong_object_type(self, wrong_type):
    df = DataFrame({'a': [1, 1]})
    msg = 'Can only merge Series or DataFrame objects, a {} was passed'.format(str(type(wrong_type)))
    with pytest.raises(TypeError, match=msg):
        merge(wrong_type, df, left_on='a', right_on='a')
    with pytest.raises(TypeError, match=msg):
        merge(df, wrong_type, left_on='a', right_on='a')