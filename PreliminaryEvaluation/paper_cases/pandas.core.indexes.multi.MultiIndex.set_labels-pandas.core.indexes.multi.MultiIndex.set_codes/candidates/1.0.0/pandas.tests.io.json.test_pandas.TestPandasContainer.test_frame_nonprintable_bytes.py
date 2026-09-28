def test_frame_nonprintable_bytes(self):

    class BinaryThing:

        def __init__(self, hexed):
            self.hexed = hexed
            self.binary = bytes.fromhex(hexed)

        def __str__(self) -> str:
            return self.hexed
    hexed = '574b4454ba8c5eb4f98a8f45'
    binthing = BinaryThing(hexed)
    df_printable = DataFrame({'A': [binthing.hexed]})
    assert df_printable.to_json() == f'{{"A":{{"0":"{hexed}"}}}}'
    df_nonprintable = DataFrame({'A': [binthing]})
    msg = 'Unsupported UTF-8 sequence length when encoding string'
    with pytest.raises(OverflowError, match=msg):
        df_nonprintable.to_json()
    df_mixed = DataFrame({'A': [binthing], 'B': [1]}, columns=['A', 'B'])
    with pytest.raises(OverflowError):
        df_mixed.to_json()
    result = df_nonprintable.to_json(default_handler=str)
    expected = f'{{"A":{{"0":"{hexed}"}}}}'
    assert result == expected
    assert df_mixed.to_json(default_handler=str) == f'{{"A":{{"0":"{hexed}"}},"B":{{"0":1}}}}'