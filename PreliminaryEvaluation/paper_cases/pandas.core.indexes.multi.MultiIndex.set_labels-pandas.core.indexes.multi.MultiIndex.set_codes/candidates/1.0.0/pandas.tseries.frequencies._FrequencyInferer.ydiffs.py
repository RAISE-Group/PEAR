@cache_readonly
def ydiffs(self):
    return unique_deltas(self.fields['Y'].astype('i8'))