@cache_readonly
def fields(self):
    return build_field_sarray(self.values)