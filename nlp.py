from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer

model = SentenceTransformer('bert-base-nli-mean-tokens')

def sentence_similarity(sentences_1, sentences_2):

	sentence_embeddings_1 = model.encode(sentences_1).reshape(-1, 1)
	sentence_embeddings_2 = model.encode(sentences_2).reshape(-1, 1)

	return cosine_similarity(sentence_embeddings_1, sentence_embeddings_2)