import unittest
from tfidf import Document
from tfidf import Corpus
import math
import numpy as np

class TestCorpus(unittest.TestCase):
    def test_initialization(self):
        d1 = Document('lorem ipsum dolor sit amet consectetur adipiscing elit sed do eiusmod tempor incididunt ut labore et dolore magna aliqua')
        d2 = Document('ut enim ad minim veniam quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat')
        
        #initialization w/acceptable input
        try:
            Corpus([d1,d2])
        except:
            self.fail('Initialization test failed because a Document cannot be created with an acceptable input.')

        #initialization with duplicate input
        with self.assertWarns(UserWarning, msg='Initialization test failed because warning is not produced for duplicate Documents.'):
            Corpus([d1,d1])

        #type checking
        with self.assertRaises(TypeError, msg='Initialization test failed because a Corpus is created without any parameters.'):
            Corpus()
        with self.assertRaises(TypeError, msg='Initialization test failed because Corpus object accepted None as input.'):
            Corpus(None)
        with self.assertRaises(TypeError, msg='Initialization test failed because Corpus object accepted empty list as input.'):
            Corpus([])
        with self.assertRaises(TypeError, msg='Initialization test failed because Corpus object accepted str as input.'):
            Corpus('lorem ipsum dolor sit amet consectetur adipiscing elit sed do eiusmod tempor incididunt ut labore et dolore magna aliqua')
        with self.assertRaises(TypeError, msg='Initialization test failed because Corpus object accepted str as input.'):
            Corpus([d1, 'lorem ipsum dolor sit amet consectetur adipiscing elit sed do eiusmod tempor incididunt ut labore et dolore magna aliqua'])

    def test_get_documents(self):
        d1 = Document('lorem ipsum dolor sit amet consectetur adipiscing elit sed do eiusmod tempor incididunt ut labore et dolore magna aliqua')
        d2 = Document('ut enim ad minim veniam quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat')
        corpus = Corpus([d1, d2])

        self.assertEqual(len((d1, d2)), len(corpus.documents), 'Get documents test failed.')
        self.assertEqual(set((d1,d2)), set(corpus.documents), 'Get documents test failed.')

    def test_add_documents(self):
        d1 = Document('lorem ipsum dolor sit amet consectetur adipiscing elit sed do eiusmod tempor incididunt ut labore et dolore magna aliqua')
        d2 = Document('ut enim ad minim veniam quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat')
        corpus = Corpus([d1, d2])

        #adding acceptable documents
        d3 = Document('duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur')
        d4 = Document('excepteur sint occaecat cupidatat non proident sunt in culpa qui officia deserunt mollit anim id est laborum')
        corpus.add_documents([d3, d4])

        self.assertEqual(len((d1, d2, d3, d4)), len(corpus.documents), 'Add documents test failed.')
        self.assertEqual(set((d1, d2, d3, d4)), set(corpus.documents), 'Add documents test failed.')

        #adding duplicate documents
        with self.assertWarns(UserWarning, msg='Add documents test failed because warning is not produced for duplicate documents.'):
            corpus.add_documents([d3])

        #type checking
        with self.assertRaises(TypeError, msg='Add documents test failed because add_documents is executed without any parameters.'):
            corpus.add_documents()
        with self.assertRaises(TypeError, msg='Add documents test failed because add_documents accepted None as input.'):
            corpus.add_documents(None)
        with self.assertRaises(TypeError, msg='Add documents test failed because add_documents accepted empty list as input.'):
            corpus.add_documents([])
        with self.assertRaises(TypeError, msg='Add documents test failed because add_documents accepted str as input.'):
            corpus.add_documents('lorem ipsum dolor sit amet consectetur adipiscing elit sed do eiusmod tempor incididunt ut labore et dolore magna aliqua')
        with self.assertRaises(TypeError, msg='Add documents test failed because add_documents accepted str as input.'):
            corpus.add_documents([d1, 'lorem ipsum dolor sit amet consectetur adipiscing elit sed do eiusmod tempor incididunt ut labore et dolore magna aliqua'])

    def test_remove_documents(self):
        d1 = Document('lorem ipsum dolor sit amet consectetur adipiscing elit sed do eiusmod tempor incididunt ut labore et dolore magna aliqua')
        d2 = Document('ut enim ad minim veniam quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat')
        d3 = Document('duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur')
        d4 = Document('excepteur sint occaecat cupidatat non proident sunt in culpa qui officia deserunt mollit anim id est laborum')
        corpus = Corpus([d1, d2, d3])

        #removing present documents
        corpus.remove_documents([d3])
        self.assertEqual(len((d1, d2)), len(corpus.documents), 'Remove documents test failed.')
        self.assertEqual(set((d1, d2)), set(corpus.documents), 'Remove documents test failed.')

        #removing documents that are not present
        with self.assertWarns(UserWarning, msg='Remove documents test failed because warning is not produced for removing nonexistent document/s.'):
            corpus.remove_documents([d1, d4])
        self.assertEqual(len((d2,)), len(corpus.documents), 'Remove documents test failed.')
        self.assertEqual(set((d2,)), set(corpus.documents), 'Remove documents test failed.')

        #removing all of the present documents
        with self.assertRaises(ValueError, msg='Remove documents test failed because all of the documents in corpus is removed.'):
            corpus.remove_documents([d2])

        #type checking
        with self.assertRaises(TypeError, msg='Remove documents test failed because remove_documents is executed without any parameters.'):
            corpus.remove_documents()
        with self.assertRaises(TypeError, msg='Remove documents test failed because remove_documents accepted None as input.'):
            corpus.remove_documents(None)
        with self.assertRaises(TypeError, msg='Remove documents test failed because remove_documents accepted empty list as input.'):
            corpus.remove_documents([])
        with self.assertRaises(TypeError, msg='Remove documents test failed because remove_documents accepted str as input.'):
            corpus.remove_documents('lorem ipsum dolor sit amet consectetur adipiscing elit sed do eiusmod tempor incididunt ut labore et dolore magna aliqua')
        with self.assertRaises(TypeError, msg='Remove documents test failed because remove_documents accepted str as input.'):
            corpus.remove_documents([d1, 'lorem ipsum dolor sit amet consectetur adipiscing elit sed do eiusmod tempor incididunt ut labore et dolore magna aliqua'])

    def test_get_n_documents(self):
        d1 = Document('lorem ipsum dolor sit amet consectetur adipiscing elit sed do eiusmod tempor incididunt ut labore et dolore magna aliqua')
        d2 = Document('ut enim ad minim veniam quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat')
        corpus = Corpus([d1,d2])

        self.assertEqual(len((d1,d2)), len(corpus.documents), 'Get documents test failed.')

    def test_exists(self):
        d1 = Document('lorem ipsum dolor sit amet consectetur adipiscing elit sed do eiusmod tempor incididunt ut labore et dolore magna aliqua')
        d2 = Document('ut enim ad minim veniam quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat')
        d3 = Document('duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur')
        d4 = Document('excepteur sint occaecat cupidatat non proident sunt in culpa qui officia deserunt mollit anim id est laborum')
        corpus = Corpus([d1, d3])

        self.assertEqual([True, False, True, False], corpus.exists([d1, d2, d3, d4]), 'Get documents test failed.')

        #type checking
        with self.assertRaises(TypeError, msg='Exists test failed because exists is executed without any parameters.'):
            corpus.exists()
        with self.assertRaises(TypeError, msg='Exists test failed because exists accepted None as input.'):
            corpus.exists(None)
        with self.assertRaises(TypeError, msg='Exists test failed because exists accepted empty list as input.'):
            corpus.exists([])
        with self.assertRaises(TypeError, msg='Exists test failed because exists accepted str as input.'):
            corpus.exists('lorem ipsum dolor sit amet consectetur adipiscing elit sed do eiusmod tempor incididunt ut labore et dolore magna aliqua')
        with self.assertRaises(TypeError, msg='Exists test failed because exists accepted str as input.'):
            corpus.exists([d1, 'lorem ipsum dolor sit amet consectetur adipiscing elit sed do eiusmod tempor incididunt ut labore et dolore magna aliqua'])          

    def test_tf_idf(self):
        d1 = Document('lorem ipsum dolor sit amet consectetur adipiscing elit sed do eiusmod tempor incididunt ut labore et dolore magna aliqua')
        d2 = Document('ut enim ad minim veniam quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat')
        d3 = Document('duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur')
        d4 = Document('excepteur sint occaecat cupidatat non proident sunt in culpa qui officia deserunt mollit anim id est laborum')
        corpus = Corpus([d1, d2, d3])

        #type checking
        with self.assertRaises(TypeError, msg='TF-IDF test failed because TF-IDF is executed without any parameters.'):
            corpus.tf_idf()
        with self.assertRaises(TypeError, msg='TF-IDF documents test failed because TF-IDF accepted None as input.'):
            corpus.tf_idf(None, 2)
        with self.assertRaises(TypeError, msg='TF-IDF documents test failed because TF-IDF accepted empty list as input.'):
            corpus.tf_idf([], 2)
        with self.assertRaises(TypeError, msg='TF-IDF documents test failed because TF-IDF accepted str as input.'):
            corpus.tf_idf('lorem ipsum dolor sit amet consectetur adipiscing elit sed do eiusmod tempor incididunt ut labore et dolore magna aliqua', 2)
        with self.assertRaises(TypeError, msg='TF-IDF documents test failed because TF-IDF accepted str as input.'):
            corpus.tf_idf([d1, 'lorem ipsum dolor sit amet consectetur adipiscing elit sed do eiusmod tempor incididunt ut labore et dolore magna aliqua'], 2)
        with self.assertRaises(TypeError, msg='TF-IDF documents test failed because TF-IDF accepted str as input.'):
            corpus.tf_idf([d1, d3, d4])

        #check n value
        with self.assertRaises(ValueError, msg='TF-IDF documents test failed because TF-IDF accepted n > max len(doc) as input.'):
            corpus.tf_idf([d1, d3, d4], 100)
        with self.assertRaises(ValueError, msg='TF-IDF documents test failed because TF-IDF accepted 0 as input.'):
            corpus.tf_idf([d1, d3, d4], 100)
        with self.assertRaises(ValueError, msg='TF-IDF documents test failed because TF-IDF accepted str as input.'):
            corpus.tf_idf([d1, d3, d4], '2')
        with self.assertRaises(ValueError, msg='TF-IDF documents test failed because TF-IDF accepted None as input.'):
            corpus.tf_idf([d1, d3, d4], None)

        docs = [d2, d4]

        unique_ngrams = set()
        for d in corpus.documents + tuple(docs):
            unique_ngrams.update(d.n_gram(2))
        unique_ngrams = list(unique_ngrams)

        tf_idfs = list()
        for d in docs:
            tfidf = np.zeros(len(unique_ngrams))
            ngram_list = d.n_gram(2)
            #print(ngram_list)
            for item in ngram_list:
                tf = ngram_list.count(item)/len(ngram_list)
                d_count = 1
                for d in corpus.documents:
                    if item in d.n_gram(2):
                        d_count += 1
                idf = math.log(corpus.n_documents/d_count)
                tfidf[unique_ngrams.index(item)] = tf*idf
            tf_idfs.append(tfidf)

        test_tf_idfs, test_ngrams = corpus.tf_idf(docs, 2)
        self.assertEqual(len(tf_idfs), len(test_tf_idfs))
        for i, tf_idf in enumerate(tf_idfs):
            self.assertTrue(np.array_equal(tf_idf, test_tf_idfs[i]))
        self.assertEqual(unique_ngrams, test_ngrams)

if __name__ == '__main__':
    unittest.main()