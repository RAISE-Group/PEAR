def test_deprecated_import(self):
    with tm.assert_produces_warning(FutureWarning):
        from pandas.io.json import json_normalize
        recs = [{'a': 1, 'b': 2, 'c': 3}, {'a': 4, 'b': 5, 'c': 6}]
        json_normalize(recs)