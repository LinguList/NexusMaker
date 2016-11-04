import unittest

from nexusmaker import Record

class TestRecord(unittest.TestCase):
    
    def test_simple(self):
        r = Record(ID=1, WID=2, LID=3, Language='English', Word='Hand', Item='hand', Annotation='?', Cognacy=None, Loan="L")
        assert r.ID == 1
        assert r.WID == 2
        assert r.LID == 3
        assert r.Language == 'English'
        assert r.Word == 'Hand'
        assert r.Item == 'hand'
        assert r.Annotation == '?'
        assert r.Loan == "L"
        assert r.Cognacy == None
    
    def test_is_loan(self):
        assert not Record(Loan="").is_loan
        assert not Record(Loan=None).is_loan
        
        assert Record(Loan="L").is_loan
        assert Record(Loan="English").is_loan
        assert Record(Loan=True).is_loan
    
        
if __name__ == '__main__':
    unittest.main()

