def test_array_numpy_labelled(self):
    labelled_input = {'a': []}
    output = ujson.loads(ujson.dumps(labelled_input), numpy=True, labelled=True)
    assert (np.empty((1, 0)) == output[0]).all()
    assert (np.array(['a']) == output[1]).all()
    assert output[2] is None
    labelled_input = [{'a': 42}]
    output = ujson.loads(ujson.dumps(labelled_input), numpy=True, labelled=True)
    assert (np.array(['a']) == output[2]).all()
    assert (np.array([42]) == output[0]).all()
    assert output[1] is None
    input_dumps = '[{"a": 42, "b":31}, {"a": 24, "c": 99}, {"a": 2.4, "b": 78}]'
    output = ujson.loads(input_dumps, numpy=True, labelled=True)
    expected_vals = np.array([42, 31, 24, 99, 2.4, 78], dtype=int).reshape((3, 2))
    assert (expected_vals == output[0]).all()
    assert output[1] is None
    assert (np.array(['a', 'b']) == output[2]).all()
    input_dumps = '{"1": {"a": 42, "b":31}, "2": {"a": 24, "c": 99}, "3": {"a": 2.4, "b": 78}}'
    output = ujson.loads(input_dumps, numpy=True, labelled=True)
    expected_vals = np.array([42, 31, 24, 99, 2.4, 78], dtype=int).reshape((3, 2))
    assert (expected_vals == output[0]).all()
    assert (np.array(['1', '2', '3']) == output[1]).all()
    assert (np.array(['a', 'b']) == output[2]).all()