from google import genai
from dotenv import load_dotenv
import os
import numpy as np

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

result = client.models.embed_content(
    model="gemini-embedding-001",
    contents="Sinh viên điểm cao nhất"
)
result2 = client.models.embed_content(
    model="gemini-embedding-001",
    contents="Học sinh giỏi nhất lớp"
)
result3 = client.models.embed_content(
    model="gemini-embedding-001",
    contents="Thời tiết hôm nay thế nào"
)

embedding = result.embeddings[0].values
print(len(embedding))     # xem vector có bao nhiêu chiều
print(embedding[:5])      # in thử 5 số đầu tiên


def cosine_similarity(vec1, vec2):
    vec1 = np.array(vec1)
    vec2 = np.array(vec2)
    return np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))

print('cosine_similarity', cosine_similarity(result.embeddings[0].values, result2.embeddings[0].values))
print('cosine_similarity', cosine_similarity(result.embeddings[0].values, result3.embeddings[0].values))