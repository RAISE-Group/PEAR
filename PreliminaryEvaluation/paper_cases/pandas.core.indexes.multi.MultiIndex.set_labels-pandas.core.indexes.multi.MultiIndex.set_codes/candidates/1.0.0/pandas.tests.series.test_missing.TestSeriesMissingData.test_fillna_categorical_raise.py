def test_fillna_categorical_raise(self):
    data = ['a', np.nan, 'b', np.nan, np.nan]
    s = Series(Categorical(data, categories=['a', 'b']))
    with pytest.raises(ValueError, match='fill value must be in categories'):
        s.fillna('d')
    with pytest.raises(ValueError, match='fill value must be in categories'):
        s.fillna(Series('d'))
    with pytest.raises(ValueError, match='fill value must be in categories'):
        s.fillna({1: 'd', 3: 'a'})
    msg = '"value" parameter must be a scalar or dict, but you passed a "list"'
    with pytest.raises(TypeError, match=msg):
        s.fillna(['a', 'b'])
    msg = '"value" parameter must be a scalar or dict, but you passed a "tuple"'
    with pytest.raises(TypeError, match=msg):
        s.fillna(('a', 'b'))
    msg = '"value" parameter must be a scalar, dict or Series, but you passed a "DataFrame"'
    with pytest.raises(TypeError, match=msg):
        s.fillna(DataFrame({1: ['a'], 3: ['b']}))