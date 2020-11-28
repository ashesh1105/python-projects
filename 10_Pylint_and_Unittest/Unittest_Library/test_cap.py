import unittest
import cap

class TestCap(unittest.TestCase):
    
    '''
    This is how you declare a test. You must import unittest.TestCase in you test class!
    '''

    def test_one_word(self):
        text = 'python'
        result = cap.cap_text(text)
        self.assertEqual(result, 'Python')

    def test_multiple_words(self):
        text = 'monty python'
        result = cap.cap_text(text)
        self.assertEqual(result, 'Monty Python')


if __name__ == '__main__':
	unittest.main()