from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


# Load AI model
model = SentenceTransformer("all-MiniLM-L6-v2")


def calculate_semantic_match(resume_text, job_description):

    # Convert resume and job description into AI embeddings
    resume_embedding = model.encode([resume_text])
    job_embedding = model.encode([job_description])

    # Calculate similarity
    similarity = cosine_similarity(
        resume_embedding,
        job_embedding
    )[0][0]

    # Convert NumPy value to normal Python float
    score = float(similarity * 100)

    # Round the score
    score = round(score, 2)

    return score