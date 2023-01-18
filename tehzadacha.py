
text = 'dfsgdfshgnhdg dfghfgd jfdgj  fdgh  fnfbv ndfghfdg'
def fuction(text):
    s = text
    if len(s) <= 25 and ' ' in s:
        result = s.rindex(' ', 0, 25)
        vivod = s[0:result] + '...'
    elif ' ' not in s:
        vivod = s[0:25]+'...'
    else:
        s = text[0:25]
        result = s.rindex(' ', 0, 25)
        vivod = s[0:result]+'...'
    return vivod
fuction(text)

class Test_suit():


    def test_25_whithout_space(self):
        text = 'dfsgdfshgnhdgfnfbvndfghfd'
        assert fuction(text) == 'dfsgdfshgnhdgfnfbvndfghfd...'

    def test_24_whithout_space(self):
        text = 'dfsgdfshgnhdgfnfbvndfghd'
        assert fuction(text) == 'dfsgdfshgnhdgfnfbvndfghd...'

    def test_26_whithout_space(self):
        text = 'dfsgdfshgnhdgfnfbvndfghfdg'
        assert fuction(text) == 'dfsgdfshgnhdgfnfbvndfghfd...'

    def test_25_whith_space(self):
        text = 'dfsgdfs hgnhdgfnfbvn dfghfd'
        assert fuction(text) == 'dfsgdfs hgnhdgfnfbvn...'

    def test_30_whith_space_in_25_position(self):
        text = 'dfsgdfs hgnhdgfnfbvn dfs gdrt'
        assert fuction(text) == 'dfsgdfs hgnhdgfnfbvn dfs...'

    def test_30_whith_space_in_26_position(self):
        text = 'dfsgdfs hgnhdgfnfbvn dfjs gdrt'
        assert fuction(text) == 'dfsgdfs hgnhdgfnfbvn...'

    def test_35_whith_space_after_25_position(self):
        text = 'dfsgdfs hgnhdgfnfbvn dsgdhdfhj dr t'
        assert fuction(text) == 'dfsgdfs hgnhdgfnfbvn...'

    def test_24_whith_space(self):
        text = 'vfdege hrth nbrthy nrtgh'
        assert fuction(text) == 'vfdege hrth nbrthy...'