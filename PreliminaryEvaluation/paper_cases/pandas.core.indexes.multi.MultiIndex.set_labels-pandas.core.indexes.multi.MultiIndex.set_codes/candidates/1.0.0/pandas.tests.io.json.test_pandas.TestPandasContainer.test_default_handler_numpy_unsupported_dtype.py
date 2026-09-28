def test_default_handler_numpy_unsupported_dtype(self):
    df = DataFrame({'a': [1, 2.3, complex(4, -5)], 'b': [float('nan'), None, complex(1.2, 0)]}, columns=['a', 'b'])
    expected = '[["(1+0j)","(nan+0j)"],["(2.3+0j)","(nan+0j)"],["(4-5j)","(1.2+0j)"]]'
    assert df.to_json(default_handler=str, orient='values') == expected