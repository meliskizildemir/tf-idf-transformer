from tfidf import Document
from tfidf import Corpus

def main():
    d1 = Document('some argue that espresso is the strongest coffee of all')
    d2 = Document('compared to the other coffees an espresso is hard to beat')
    d3 = Document('it is understandable for someone who havent tried the turkish coffee to think this')
    d4 = Document('but surely anyone who tasted a turkish coffee would agree that it is stronger than an espresso')
    d5 = Document('it is safe to say coffee beans also have an effect in the strongness of the coffee')
    corpus = Corpus([d1, d2])

    print('unigrams in document 1:', d1.n_gram(1))
    print('bigrams in document 2:', d1.n_gram(2))

    print('Documents in corpus:', corpus.documents)
    corpus.add_documents([d3, d4])
    print('Documents in corpus after addition:', corpus.documents)
    corpus.remove_documents([d4])
    print('Documents in corpus after removal:', corpus.documents)

    tf_idfs, unique_unigrams = corpus.tf_idf([d1, d2, d3, d4, d5], 1)
    print('TFIDFs:', tf_idfs)
    print('Unique Unigrams:', unique_unigrams)
    tf_idfs, unique_bigrams = corpus.tf_idf([d1, d2, d3, d4, d5], 2)
    print('TFIDFs:', tf_idfs)
    print('Unique Bigrams:', unique_bigrams)

if __name__ == "__main__":
    main()