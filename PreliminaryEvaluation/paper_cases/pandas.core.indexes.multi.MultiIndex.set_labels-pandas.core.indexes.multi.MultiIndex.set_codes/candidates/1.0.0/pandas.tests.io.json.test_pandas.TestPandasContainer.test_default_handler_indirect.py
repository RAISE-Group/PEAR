def test_default_handler_indirect(self):
    from pandas.io.json import dumps

    def default(obj):
        if isinstance(obj, complex):
            return [('mathjs', 'Complex'), ('re', obj.real), ('im', obj.imag)]
        return str(obj)
    df_list = [9, DataFrame({'a': [1, 'STR', complex(4, -5)], 'b': [float('nan'), None, 'N/A']}, columns=['a', 'b'])]
    expected = '[9,[[1,null],["STR",null],[[["mathjs","Complex"],["re",4.0],["im",-5.0]],"N\\/A"]]]'
    assert dumps(df_list, default_handler=default, orient='values') == expected