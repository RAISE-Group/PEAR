def test_label_overflow(self):
    result = pd.DataFrame({'bar' * 100000: [1], 'foo': [1337]}).to_json()
    expected = f'''{{"{'bar' * 100000}":{{"0":1}},"foo":{{"0":1337}}}}'''
    assert result == expected