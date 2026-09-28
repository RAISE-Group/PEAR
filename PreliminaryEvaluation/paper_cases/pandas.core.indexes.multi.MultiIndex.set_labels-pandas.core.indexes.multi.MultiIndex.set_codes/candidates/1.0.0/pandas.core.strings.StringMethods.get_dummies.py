@copy(str_get_dummies)
@forbid_nonstring_types(['bytes'])
def get_dummies(self, sep='|'):
    data = self._orig.astype(str) if self._is_categorical else self._parent
    result, name = str_get_dummies(data, sep)
    return self._wrap_result(result, use_codes=not self._is_categorical, name=name, expand=True, returns_string=False)