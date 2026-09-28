def _maybe_eval(self, binop, eval_in_python):
    return binop.evaluate(self.env, self.engine, self.parser, self.term_type, eval_in_python)