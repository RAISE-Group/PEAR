def _read_header(self):
    self.filepath_or_buffer.seek(0)
    line1 = self._get_row()
    if line1 != _correct_line1:
        self.close()
        raise ValueError('Header record is not an XPORT file.')
    line2 = self._get_row()
    fif = [['prefix', 24], ['version', 8], ['OS', 8], ['_', 24], ['created', 16]]
    file_info = _split_line(line2, fif)
    if file_info['prefix'] != 'SAS     SAS     SASLIB':
        self.close()
        raise ValueError('Header record has invalid prefix.')
    file_info['created'] = _parse_date(file_info['created'])
    self.file_info = file_info
    line3 = self._get_row()
    file_info['modified'] = _parse_date(line3[:16])
    header1 = self._get_row()
    header2 = self._get_row()
    headflag1 = header1.startswith(_correct_header1)
    headflag2 = header2 == _correct_header2
    if not (headflag1 and headflag2):
        self.close()
        raise ValueError('Member header not found')
    fieldnamelength = int(header1[-5:-2])
    mem = [['prefix', 8], ['set_name', 8], ['sasdata', 8], ['version', 8], ['OS', 8], ['_', 24], ['created', 16]]
    member_info = _split_line(self._get_row(), mem)
    mem = [['modified', 16], ['_', 16], ['label', 40], ['type', 8]]
    member_info.update(_split_line(self._get_row(), mem))
    member_info['modified'] = _parse_date(member_info['modified'])
    member_info['created'] = _parse_date(member_info['created'])
    self.member_info = member_info
    types = {1: 'numeric', 2: 'char'}
    fieldcount = int(self._get_row()[54:58])
    datalength = fieldnamelength * fieldcount
    if datalength % 80:
        datalength += 80 - datalength % 80
    fielddata = self.filepath_or_buffer.read(datalength)
    fields = []
    obs_length = 0
    while len(fielddata) >= fieldnamelength:
        field, fielddata = (fielddata[:fieldnamelength], fielddata[fieldnamelength:])
        field = field.ljust(140)
        fieldstruct = struct.unpack('>hhhh8s40s8shhh2s8shhl52s', field)
        field = dict(zip(_fieldkeys, fieldstruct))
        del field['_']
        field['ntype'] = types[field['ntype']]
        fl = field['field_length']
        if field['ntype'] == 'numeric' and (fl < 2 or fl > 8):
            self.close()
            msg = f'Floating field width {fl} is not between 2 and 8.'
            raise TypeError(msg)
        for k, v in field.items():
            try:
                field[k] = v.strip()
            except AttributeError:
                pass
        obs_length += field['field_length']
        fields += [field]
    header = self._get_row()
    if not header == _correct_obs_header:
        self.close()
        raise ValueError('Observation header not found.')
    self.fields = fields
    self.record_length = obs_length
    self.record_start = self.filepath_or_buffer.tell()
    self.nobs = self._record_count()
    self.columns = [x['name'].decode() for x in self.fields]
    dtypel = [('s' + str(i), 'S' + str(field['field_length'])) for i, field in enumerate(self.fields)]
    dtype = np.dtype(dtypel)
    self._dtype = dtype