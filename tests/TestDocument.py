import unittest
from tfidf import Document

class TestDocument(unittest.TestCase):
    def test_initialization(self):

        #initialization w/acceptable input
        text = 'lorem ipsum dolor sit amet consectetur adipiscing elit sed do eiusmod tempor incididunt ut labore et dolore magna aliqua'
        try:
            doc = Document(text)
        except:
            self.fail('Initialization test failed because a Document cannot be created with an acceptable input.')
        self.assertIsInstance(doc, Document)

        #type checking
        with self.assertRaises(TypeError, msg='Initialization test failed because a Document is created without any parameters.'):
            Document()
        with self.assertRaises(TypeError, msg='Initialization test failed because Document object accepted None as input.'):
            Document(None)
        with self.assertRaises(TypeError, msg='Initialization test failed because Document object accepted empty string as input.'):
            Document('')
        with self.assertRaises(TypeError, msg='Initialization test failed because Document object accepted a str list as input.'):
            Document([text])
        with self.assertRaises(TypeError, msg='Initialization test failed because Document object accepted an int as input.'):
            Document(3)

        #initialization w/html input
        with self.assertRaises(ValueError, msg='Initialization test failed because Document object accepted HTML as input.'):
            html_text = '<html><body><h1>lorem ipsum</h1><p>dolor sit amet consectetur</p></body></html>'
            Document(html_text)

        #initialization w/URL input
        with self.assertRaises(ValueError, msg='Initialization test failed because Document object accepted string with URL as input.'):
            email = 'lorem ipsum https://www.lorem.com/ipsum.php?q=suas dolor sit amet consectetur adipiscing elit sed do eiusmod tempor incididunt ut labore et dolore magna aliqua'
            Document(email)

        #initialization w/email input
        with self.assertRaises(ValueError, msg='Initialization test failed because Document object accepted string with email as input.'):
            email = 'lorem ipsum lorem@ipsum.com dolor sit amet consectetur adipiscing elit sed do eiusmod tempor incididunt ut labore et dolore magna aliqua'
            Document(email)

        #initialization w/uppercase input
        with self.assertRaises(ValueError, msg='Initialization test failed because Document object accepted str with uppercased letters as input.'):
            text2 = 'Lorem ipsum dolor sit amet consectetur adipiscing elit sed do eiusmod tempor incididunt ut labore et dolore magna aliqua'
            Document(text2)
        with self.assertRaises(ValueError, msg='Initialization test failed because Document object accepted str with uppercased letters as input.'):
            text3 = 'LOREM IPSUM'
            Document(text3)

        #initialization w/input with punctuation
        with self.assertRaises(ValueError, msg='Initialization test failed because Document object accepted str with punctuation as input.'):
            text4 = 'lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.'
            Document(text4)
        with self.assertRaises(ValueError, msg='Initialization test failed because Document object accepted str with punctuation as input.'):
            text5 = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
            Document(text5)

        #initialization w/input with numbers
        with self.assertRaises(ValueError, msg='Initialization test failed because Document object accepted str with numbers as input.'):
            text6 = '0 1 2 3 4 5 6 7 8 9'
            Document(text6)
        with self.assertRaises(ValueError, msg='Initialization test failed because Document object accepted str with numbers as input.'):
            text7 = '123 456'
            Document(text7)

        #initialization w/input with whitespace other than space
        with self.assertRaises(ValueError, msg='Initialization test failed because Document object accepted str with whitespace other than space.'):
            text8 = 'lorem  ipsum'
            Document(text8)
        with self.assertRaises(ValueError, msg='Initialization test failed because Document object accepted str with whitespace other than space.'):
            text9 = '\t\n\r\x0b\x0c'
            Document(text9)

    def test_get_content(self):
        text = 'lorem ipsum dolor sit amet consectetur adipiscing elit sed do eiusmod tempor incididunt ut labore et dolore magna aliqua'
        doc = Document(text)

        self.assertEqual(text, doc.content, 'Get content test failed.')

    def test_get_words(self):
        text = 'lorem ipsum dolor sit amet consectetur adipiscing elit sed do eiusmod tempor incididunt ut labore et dolore magna aliqua'
        doc = Document(text)

        self.assertEqual(text.split(), doc.words, 'Get words test failed.')

    def test_get_unique_words(self):
        text = 'lorem ipsum dolor sit amet consectetur adipiscing elit sed do eiusmod tempor incididunt ut labore et dolore magna aliqua'
        doc = Document(text)

        self.assertEqual(set(text.split()), doc.unique_words, 'Get unique words test failed.')

    def test_get_ngram(self):
        text = 'lorem ipsum dolor sit amet consectetur adipiscing elit sed do eiusmod tempor incididunt ut labore et dolore magna aliqua'
        doc = Document(text)

        with self.assertRaises(TypeError, msg='Ngram test failed because ngram accepted str as input.'):
            doc.n_gram('1')
        with self.assertRaises(TypeError, msg='Ngram test failed because ngram accepted empty parameters.'):
            doc.n_gram()
        with self.assertRaises(TypeError, msg='Ngram test failed because ngram accepted float as input.'):
            doc.n_gram(0.2)

        with self.assertRaises(ValueError, msg='Ngram test failed because ngram accepted 0 as input.'):
            doc.n_gram(0)
        with self.assertRaises(ValueError, msg='Ngram test failed because ngram accepted > len(content) as input.'):
            doc.n_gram(len(text.split()))

        unigrams = doc.n_gram(1)
        self.assertEqual(text.split(), unigrams, 'Ngram test failed because ngram function failed to generate unigrams.')
        ngrams = doc.n_gram(len(text.split())-1)
        self.assertEqual([' '.join(text.split()[:-1]), ' '.join(text.split()[1:])], ngrams, 'Ngram test failed because ngram function failed to generate unigrams.')

    def test_equality(self):
        text = 'lorem ipsum dolor sit amet consectetur adipiscing elit sed do eiusmod tempor incididunt ut labore et dolore magna aliqua'
        doc1 = Document(text)
        doc2 = Document(text)
        doc3 = Document('lorem ipsum')

        self.assertEqual(doc1, doc2, 'Equality (equal) test failed.')
        self.assertNotEqual(doc1, doc3, 'Equality (not equal) test failed.')

if __name__ == '__main__':
    unittest.main()