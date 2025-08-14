import pandas as pd
from pathlib import Path

def test_glossary_csv_present_and_has_embeddings():
  p = Path("wikiLex") / "wikip_ai_glossary.csv"
  assert p.exists(), "Glossary CSV missing at wikiLex/wikip_ai_glossary.csv"
  df = pd.read_csv(p, nrows=5)
  required = {"Title", "Link", "Wikipedia_page_description", "High_dimensional_embeddings"}
  missing = required.difference(df.columns)
  assert not missing, f"Missing required columns: {', '.join(sorted(missing))}"
  assert "Title" in df.columns, "Missing Title column"
  assert len(df) > 0, "Grossary appears empty"