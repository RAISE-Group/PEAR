@cache_readonly
def mdiffs(self):
    nmonths = self.fields['Y'] * 12 + self.fields['M']
    return unique_deltas(nmonths.astype('i8'))