def get_op_from_name(self, op_name):
    short_opname = op_name.strip('_')
    try:
        op = getattr(operator, short_opname)
    except AttributeError:
        rop = getattr(operator, short_opname[1:])
        op = lambda x, y: rop(y, x)
    return op