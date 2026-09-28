def _resolve_name(self):
    if self.side == 'left':
        if self.name not in self.env.queryables:
            raise NameError(f'name {repr(self.name)} is not defined')
        return self.name
    try:
        return self.env.resolve(self.name, is_local=False)
    except UndefinedVariableError:
        return self.name