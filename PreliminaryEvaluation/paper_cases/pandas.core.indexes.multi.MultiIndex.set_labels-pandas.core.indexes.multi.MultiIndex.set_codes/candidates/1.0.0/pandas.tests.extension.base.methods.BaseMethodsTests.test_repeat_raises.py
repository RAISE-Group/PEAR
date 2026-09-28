@pytest.mark.parametrize('repeats, kwargs, error, msg', [(2, dict(axis=1), ValueError, "'axis"), (-1, dict(), ValueError, 'negative'), ([1, 2], dict(), ValueError, 'shape'), (2, dict(foo='bar'), TypeError, "'foo'")])
def test_repeat_raises(self, data, repeats, kwargs, error, msg, use_numpy):
    with pytest.raises(error, match=msg):
        if use_numpy:
            np.repeat(data, repeats, **kwargs)
        else:
            data.repeat(repeats, **kwargs)