import pandas as pd
from pathlib import Path

def test_glossary_csv_prevent_and_has_embeddings():
  p = Path("wikiLex") / "wikip_ai_glossary.csv"
  assert p.exists(), "Glossary CSV missing at wikiLex/wikip_ai_glossary.csv"
  df = pd.read_csv(p, nrows=5)
  assert "Titil" in df.columns, "Missing Title column"
  assert "High_dimensional_embeddings" in df.columns, "Embeddings column missing"