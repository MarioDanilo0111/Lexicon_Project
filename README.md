# Lexicon_Project

---

title: Lexicon (clean)
emoji: 📚
colorFrom: blue
colorTo: indigo
sdk: docker
app_port: 7860
pinned: false

---

## Deploy updates (Hugging Face)

Live Space: [Hugging Face - Lexicon App](https://huggingface.co/spaces/maridanilo/lexicon-clean)

### Option A - Fast and simple (recomended)

```bash
  hf upload --repo-type space maridanilo/lexicon-clean . . --exclude 'env/*' '__pycache__/*' '.git/*' --commit-message 'Update'
```

### Option B - Git push

```bash
  git remote add hf-clean https://huggingface.co/spaces/maridanilo/lexicon-clean
```

# deploy

```bash
  git push hf-clean main
```

### Check logs

Open the Space → Logs to confirm build/runtime status.

## Overview

Lexicon_Project is an application designed to assist users in understanding programming language concepts through AI-driven explanations and examples. It enhances learning by providing related links and terms, making complex coding terminology more accessible.

## Description

The Lexicon_Project leverages a machine learning model to interpret and respond to user queries regarding programming terms. It not only offers clear explanations and relevant examples but also suggests additional resources to deepen the user's understanding. This interactive tool is ideal for both novice and experienced programmers seeking to expand their technical vocabulary.

### Dataset

The model utilizes a dataset maintained by Antoine Bourgois, which is continuously updated to reflect the latest in AI and programming terminologies. The dataset can be accessed on [Kaggle](https://www.kaggle.com/datasets/antoinebourgois2/wikipedia-ai-glossary).

## Getting Started

### Dependencies

Ensure you have the following Python libraries installed:

- streamlit
- pandas
- sklearn.metrics.pairwise (part of scikit-learn)
- plotly.graph_objects

### Installation

Install the required dependencies via pip:

```bash
pip install streamlit pandas scikit-learn plotly

```

## Usage

To run the application, execute the following command in your terminal:

```bash
streamlit run main.py
```

Replace main.py with the path to the script if your setup requires it.

## Contributing

Contributions to the Lexicon_Project are welcome!
Please refer to the project's issues tracker to report bugs or suggest enhancements.

[![Open in Spaces](https://img.shields.io/badge/HF%20Space-lexicon--clean-blue)](https://huggingface.co/spaces/maridanilo/lexicon-clean)
