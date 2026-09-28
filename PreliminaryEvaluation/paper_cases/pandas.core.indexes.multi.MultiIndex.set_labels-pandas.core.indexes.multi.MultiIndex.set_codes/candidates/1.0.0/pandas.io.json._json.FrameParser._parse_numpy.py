def _parse_numpy(self):
    json = self.json
    orient = self.orient
    if orient == 'columns':
        args = loads(json, dtype=None, numpy=True, labelled=True, precise_float=self.precise_float)
        if len(args):
            args = (args[0].T, args[2], args[1])
        self.obj = DataFrame(*args)
    elif orient == 'split':
        decoded = loads(json, dtype=None, numpy=True, precise_float=self.precise_float)
        decoded = {str(k): v for k, v in decoded.items()}
        self.check_keys_split(decoded)
        self.obj = DataFrame(**decoded)
    elif orient == 'values':
        self.obj = DataFrame(loads(json, dtype=None, numpy=True, precise_float=self.precise_float))
    else:
        self.obj = DataFrame(*loads(json, dtype=None, numpy=True, labelled=True, precise_float=self.precise_float))