@pytest.mark.parametrize('bad_input,exc_type,kwargs', [([{}, []], ValueError, {}), ([42, None], TypeError, {}), ([['a'], 42], ValueError, {}), ([42, {}, 'a'], TypeError, {}), ([42, ['a'], 42], ValueError, {}), (['a', 'b', [], 'c'], ValueError, {}), ([{'a': 'b'}], ValueError, dict(labelled=True)), ({'a': {'b': {'c': 42}}}, ValueError, dict(labelled=True)), ([{'a': 42, 'b': 23}, {'c': 17}], ValueError, dict(labelled=True))])
def test_array_numpy_except(self, bad_input, exc_type, kwargs):
    with pytest.raises(exc_type):
        ujson.decode(ujson.dumps(bad_input), numpy=True, **kwargs)