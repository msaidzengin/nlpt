from gensim.test.utils import common_texts
from gensim.models import Word2Vec
from gensim.models import KeyedVectors

model = KeyedVectors.load_word2vec_format('wordEmbeddings.txt', binary=False)
print(model.most_similar("aselsan")) # prints tusaş, roketsan, havelsan, tai, ssb ...
print(model.most_similar(positive=['silah','uçak'],negative=['araba'],topn=1)) # prints iha
print(model.most_similar(positive=['silah','uçak'],negative=['iha'],topn=1)) # prints muharebe
print(model.similarity('roket','silah')) # 0.7742
print(model.most_similar('motor')) # dizel, pompa, servo, döner, valf
print(model.most_similar('füze')) # roket, fırlatma, denizaltı,
