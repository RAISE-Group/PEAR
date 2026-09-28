def _parse_no_numpy(self):
    json = self.json
    orient = self.orient
    if orient == 'columns':
        self.obj = DataFrame(loads(json, precise_float=self.precise_float), dtype=None)
    elif orient == 'split':
        decoded = {str(k): v for k, v in loads(json, precise_float=self.precise_float).items()}
        self.check_keys_split(decoded)
        self.obj = DataFrame(dtype=None, **decoded)
    elif orient == 'index':
        self.obj = DataFrame.from_dict(loads(json, precise_float=self.precise_float), dtype=None, orient='index')
    elif orient == 'table':
        self.obj = parse_table_schema(json, precise_float=self.precise_float)
    else:
        self.obj = DataFrame(loads(json, precise_float=self.precise_float), dtype=None)