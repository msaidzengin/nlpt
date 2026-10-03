# nlpt

Scripts for Turkish text cleanup, Word2Vec word embeddings, and sentence similarity.

## nlpt

Helpers that fold Turkish letters into ASCII, strip punctuation, and drop non-ASCII characters.

From the repository root:

```bash
python -c "from nlpt.preprocess import tr2eng, clean_words, clean_words_upper; print(tr2eng('İstanbul'))"
```

To install the package:

```bash
pip install .
```

## word-embeddings

`train.py` reads one sentence per line from `sentences.txt` and writes a Word2Vec file. `predict.py` loads that file and prints nearest-word examples. Training uses the Gensim 3 argument `size` (Gensim 4 renamed it to `vector_size`).

```bash
cd word-embeddings
pip install 'gensim>=3.8,<4'
```

Put the corpus in `sentences.txt` in this directory before training: one sentence per line, words separated by spaces. `predict.py` looks up `aselsan`, `silah`, `uçak`, `araba`, `iha`, `roket`, `motor`, and `füze`, so those words have to appear in the corpus.

```bash
python train.py
python predict.py
```

`train.py` writes `wordEmbeddings.txt` in the same directory. Run it before `predict.py`.

## document-similarity

`main.py` compares two built-in paragraphs with a multilingual sentence transformer and prints a similarity score from 0 to 100.

```bash
cd document-similarity
pip install pandas scikit-learn sentence-transformers
python main.py
```

The first run downloads the `xlm-r-100langs-bert-base-nli-mean-tokens` model.
