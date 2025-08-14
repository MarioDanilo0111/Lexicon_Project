import pandas as pd
from sentence_transformers import SentenceTransformer
import json

# Load the model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Load your original CSV
df = pd.read_csv('wikiLex/wikip_ai_glossary.csv')

# Generate embeddings for each title
embeddings = model.encode(df['Title'].astype(str).tolist())

# Add as a new column (convert list to JSON-style string)
df['High_dimensional_embeddings'] = [json.dumps(vec.tolist()) for vec in embeddings]

# Save to the same file (or change filename if you want to keep original)
df.to_csv('wikiLex/wikip_ai_glossary.csv', index=False)

print("✅ Embeddings generated and saved successfully.")
