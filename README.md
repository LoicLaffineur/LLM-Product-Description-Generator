# 🤖 Generate Product Descriptions with Fine-Tuned LLMs

## 🎯 Business Problem

E-commerce catalogs grow quickly, but high-quality product descriptions remain expensive and time-consuming to write manually.

How can we automatically generate accurate, engaging, and scalable product descriptions using Large Language Models—and measure whether fine-tuning actually improves over prompt engineering alone?

## 💡 Proposed Solution

This repository builds a full end-to-end pipeline to generate product descriptions from structured product metadata (e.g., `title`, `brand`, `category`, `price`) and compare:

- a base LLM generation using prompt engineering,
- a fine-tuned variant using QLoRA (PEFT) with Mistral7B,
- an optional RAG-enhanced generation step to inject retrieved context.

The workflow is organized as 6 notebooks (data preparation → prompt generation → evaluation → RAG → fine-tuning → deployment) plus a Streamlit UI.

### Key steps:

- Data loading & cleaning (create a curated dataset)
- Prompt engineering with multiple styles (short / marketing / technical)
- Evaluation with lexical + semantic metrics + composite scoring
- Optional RAG pipeline (FAISS retrieval + context injection)
- Fine-tuning with QLoRA to specialize the model on the domain
- Deployment via FastAPI + Streamlit for real-time generation

## 🧠 Project Pipeline (End-to-End View)

`Raw data → Cleaning → Prompt Engineering → Base LLM`

`                              ↓`

`                         Fine-Tuning (QLoRA)`

`                              ↓`

`                 Evaluation (lexical + semantic)`

`                              ↓`

`         (Optional) RAG: retrieval + context injection`

`                              ↓`

`                 FastAPI API → Streamlit Application`

## 📄 Notebook Summary (01 to 06)

### `01_Load_&_Clean.ipynb` — Data Loading & Cleaning

- Loads the Amazon Electronics dataset
- Explores structure, filters and deduplicates
- Produces a clean sample for downstream steps
- Key output: `data/processed/clean_products_800.csv`

### `02_Prompt_Engineering.ipynb` — Prompt Engineering

- Generates product descriptions using prompt templates
- Tests multiple styles:
  - `short`
  - `marketing`
  - `technical`

### `03_Evaluation.ipynb` — Product Description Evaluation

- Evaluates generated descriptions against reference Amazon descriptions
- Metrics observed in the repo:
  - BLEU
  - ROUGE-L
  - semantic similarity (cosine using sentence embeddings)
  - composite score
- Key output: `data/outputs/scores_evaluation.csv`

### `04_RAG.ipynb` — RAG-Enhanced Generation

- Builds a FAISS index from sentence embeddings (retrieval)
- Retrieves top-k similar products
- Injects retrieved context into the RAG prompt before generation
- Key outputs:
  - `data/outputs/rag_results.jsonl`
  - `data/outputs/partial_results.jsonl`

### `05_LoRA.ipynb` — LoRA Fine-Tuning (QLoRA)

- Fine-tunes a Mistral Instruct model using QLoRA/PEFT
- Adapter targets observed in the adapter config:
  - `gate_proj`, `o_proj`, `k_proj`, `v_proj`, `q_proj`, `up_proj`, `down_proj`

### `06_API.ipynb` — Deployment: FastAPI (+ ngrok)

- Exposes the generation pipeline through REST endpoints
- Endpoints observed:
  - `GET /`
  - `GET /health`
  - `POST /generate` (returns `base` and `finetuned`)
- The notebook can also open a public URL via ngrok

## 🛠️ Technologies

Python • Hugging Face Transformers • PEFT (QLoRA) • Mistral 7B Instruct • FastAPI • Streamlit • Pandas • NumPy • FAISS • sentence-transformers

## 🚀 Business Impact

- Scale content creation across large catalogs (minutes/hours → seconds)
- More consistent tone/quality via domain adaptation (fine-tuning)
- Better control of output style (short/marketing/technical)
- Faster iteration thanks to an evaluation loop (metrics + qualitative examples)

## 📊 Evaluation Results

### Model evaluation setup

The repository evaluates generated descriptions using:

- lexical overlap (BLEU, ROUGE-L),
- semantic similarity (cosine similarity over embeddings),
- a composite score aggregating the above.

### Best-performing generation style (observed)

The Streamlit UI notes that the `technical` style reaches the best composite score (approx. `0.435`) in the evaluation notebook.

### Where to find the raw scores & samples

- `data/outputs/scores_evaluation.csv`
- `data/outputs/examples.json`
- `data/outputs/rag_results.jsonl` (for RAG runs)

## 🤖 Streamlit Application

The interactive UI is implemented in `app/app.py`.

Run locally:

```bash
python3 -m streamlit run app/app.py
```

`app/app.py` calls a FastAPI backend through `API_URL` (currently configured for a ngrok URL).

## 📂 Repository Structure

├── `notebooks/` (pipeline: data → prompt → evaluation → RAG → LoRA → API)
├── `app/` (Streamlit UI)
├── `data/` (processed dataset + evaluation/RAG outputs)
├── `models/` (PEFT adapter + templates/configs)
└── `assets/` (project assets and screenshots)

## ✅ How to Reproduce the Workflow

1. Run `notebooks/01_Load_&_Clean.ipynb`
2. Run `notebooks/02_Prompt_Engineering.ipynb`
3. Run `notebooks/03_Evaluation.ipynb`
4. (Optional) Run `notebooks/04_RAG.ipynb`
5. Run `notebooks/05_LoRA.ipynb` and save the adapter to `models/final_adapter/`
6. Run `notebooks/06_API.ipynb` to start FastAPI and obtain the backend URL
7. Update `API_URL` in `app/app.py` and run the Streamlit UI 