def visit_Compare(self, node, **kwargs):
    ops = node.ops
    comps = node.comparators
    if len(comps) == 1:
        op = self.translate_In(ops[0])
        binop = ast.BinOp(op=op, left=node.left, right=comps[0])
        return self.visit(binop)
    left = node.left
    values = []
    for op, comp in zip(ops, comps):
        new_node = self.visit(ast.Compare(comparators=[comp], left=left, ops=[self.translate_In(op)]))
        left = comp
        values.append(new_node)
    return self.visit(ast.BoolOp(op=ast.And(), values=values))