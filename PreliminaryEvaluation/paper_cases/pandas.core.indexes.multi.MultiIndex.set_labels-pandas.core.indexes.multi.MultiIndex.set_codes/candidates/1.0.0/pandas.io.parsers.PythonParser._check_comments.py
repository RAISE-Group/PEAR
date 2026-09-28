def _check_comments(self, lines):
    if self.comment is None:
        return lines
    ret = []
    for l in lines:
        rl = []
        for x in l:
            if not isinstance(x, str) or self.comment not in x:
                rl.append(x)
            else:
                x = x[:x.find(self.comment)]
                if len(x) > 0:
                    rl.append(x)
                break
        ret.append(rl)
    return ret