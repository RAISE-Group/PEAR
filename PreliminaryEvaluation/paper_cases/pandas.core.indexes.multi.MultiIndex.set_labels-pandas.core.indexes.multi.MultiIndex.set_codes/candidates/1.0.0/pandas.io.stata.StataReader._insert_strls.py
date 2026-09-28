def _insert_strls(self, data):
    if not hasattr(self, 'GSO') or len(self.GSO) == 0:
        return data
    for i, typ in enumerate(self.typlist):
        if typ != 'Q':
            continue
        data.iloc[:, i] = [self.GSO[str(k)] for k in data.iloc[:, i]]
    return data