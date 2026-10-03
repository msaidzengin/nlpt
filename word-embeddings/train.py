import multiprocessing
from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence


model = Word2Vec(LineSentence("sentences.txt"), size=400, window=5, min_count=1, workers=multiprocessing.cpu_count())
model.wv.save_word2vec_format("wordEmbeddings.txt")
print("done")
