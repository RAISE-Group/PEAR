def _evaluate(self):
    import numexpr as ne
    s = self.convert()
    env = self.expr.env
    scope = env.full_scope
    _check_ne_builtin_clash(self.expr)
    return ne.evaluate(s, local_dict=scope)