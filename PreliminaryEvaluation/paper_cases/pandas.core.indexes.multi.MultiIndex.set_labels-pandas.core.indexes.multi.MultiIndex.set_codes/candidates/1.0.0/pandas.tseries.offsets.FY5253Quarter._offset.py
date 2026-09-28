@cache_readonly
def _offset(self):
    return FY5253(startingMonth=self.startingMonth, weekday=self.weekday, variation=self.variation)