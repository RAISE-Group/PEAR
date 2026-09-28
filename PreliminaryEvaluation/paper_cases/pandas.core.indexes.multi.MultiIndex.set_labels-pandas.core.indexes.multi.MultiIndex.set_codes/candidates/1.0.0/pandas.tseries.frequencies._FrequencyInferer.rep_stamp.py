@cache_readonly
def rep_stamp(self):
    return Timestamp(self.values[0])