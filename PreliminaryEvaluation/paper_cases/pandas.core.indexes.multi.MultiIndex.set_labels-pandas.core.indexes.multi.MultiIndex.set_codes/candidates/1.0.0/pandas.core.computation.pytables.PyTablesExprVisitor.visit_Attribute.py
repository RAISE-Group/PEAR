def visit_Attribute(self, node, **kwargs):
    attr = node.attr
    value = node.value
    ctx = type(node.ctx)
    if ctx == ast.Load:
        resolved = self.visit(value)
        try:
            resolved = resolved.value
        except AttributeError:
            pass
        try:
            return self.term_type(getattr(resolved, attr), self.env)
        except AttributeError:
            if isinstance(value, ast.Name) and value.id == attr:
                return resolved
    raise ValueError(f'Invalid Attribute context {ctx.__name__}')