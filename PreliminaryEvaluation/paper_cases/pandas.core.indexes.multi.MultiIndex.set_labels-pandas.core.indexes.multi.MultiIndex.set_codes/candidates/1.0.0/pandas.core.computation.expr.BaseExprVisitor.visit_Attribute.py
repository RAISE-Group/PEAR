def visit_Attribute(self, node, **kwargs):
    attr = node.attr
    value = node.value
    ctx = node.ctx
    if isinstance(ctx, ast.Load):
        resolved = self.visit(value).value
        try:
            v = getattr(resolved, attr)
            name = self.env.add_tmp(v)
            return self.term_type(name, self.env)
        except AttributeError:
            if isinstance(value, ast.Name) and value.id == attr:
                return resolved
    raise ValueError(f'Invalid Attribute context {ctx.__name__}')