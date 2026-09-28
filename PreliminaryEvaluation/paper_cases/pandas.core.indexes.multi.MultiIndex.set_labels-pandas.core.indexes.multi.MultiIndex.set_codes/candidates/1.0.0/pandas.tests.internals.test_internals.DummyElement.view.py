def view(self, dtype):
    return type(self)(self.value.view(dtype), dtype)