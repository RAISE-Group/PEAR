def _next_line(self):
    if isinstance(self.data, list):
        while self.skipfunc(self.pos):
            self.pos += 1
        while True:
            try:
                line = self._check_comments([self.data[self.pos]])[0]
                self.pos += 1
                if not self.skip_blank_lines and (self._is_line_empty(self.data[self.pos - 1]) or line):
                    break
                elif self.skip_blank_lines:
                    ret = self._remove_empty_lines([line])
                    if ret:
                        line = ret[0]
                        break
            except IndexError:
                raise StopIteration
    else:
        while self.skipfunc(self.pos):
            self.pos += 1
            next(self.data)
        while True:
            orig_line = self._next_iter_line(row_num=self.pos + 1)
            self.pos += 1
            if orig_line is not None:
                line = self._check_comments([orig_line])[0]
                if self.skip_blank_lines:
                    ret = self._remove_empty_lines([line])
                    if ret:
                        line = ret[0]
                        break
                elif self._is_line_empty(orig_line) or line:
                    break
    if self.pos == 1:
        line = self._check_for_bom(line)
    self.line_pos += 1
    self.buf.append(line)
    return line