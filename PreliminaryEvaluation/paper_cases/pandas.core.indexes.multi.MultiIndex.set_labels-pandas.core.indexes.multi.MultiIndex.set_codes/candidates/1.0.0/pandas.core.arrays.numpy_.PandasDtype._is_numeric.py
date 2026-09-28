@property
def _is_numeric(self):
    return self.kind in set('biufc')