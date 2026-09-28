def test_depr(self):
    deprecated_list = self.deprecated_modules + self.deprecated_classes + self.deprecated_classes_in_future + self.deprecated_funcs + self.deprecated_funcs_in_future
    for depr in deprecated_list:
        with tm.assert_produces_warning(FutureWarning):
            deprecated = getattr(pd, depr)
            if not compat.PY37:
                if depr == 'datetime':
                    deprecated.__getattr__(dir(pd.datetime.datetime)[-1])
                elif depr == 'SparseArray':
                    deprecated([])
                else:
                    deprecated.__getattr__(dir(deprecated)[-1])