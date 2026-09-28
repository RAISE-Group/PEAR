def test_api(self):
    checkthese = self.lib + self.misc + self.modules + self.classes + self.funcs + self.funcs_option + self.funcs_read + self.funcs_json + self.funcs_to + self.private_modules
    if not compat.PY37:
        checkthese.extend(self.deprecated_modules + self.deprecated_classes + self.deprecated_classes_in_future + self.deprecated_funcs_in_future + self.deprecated_funcs)
    self.check(pd, checkthese, self.ignored)