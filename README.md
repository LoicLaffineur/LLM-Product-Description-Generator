# Automated Product Description Generation (LLM Pipeline)

Transform product metadata into consistent, high‑quality descriptions at scale.

## The Problem

E‑commerce and retail companies manage large catalogs but struggle to:

- Produce high‑quality product descriptions fast enough  
- Maintain consistent tone and style across products  
- Scale content creation without exploding costs  

Manual writing is slow, expensive, and hard to maintain as the catalog grows.

## The Approach

This project builds an end‑to‑end pipeline to generate product descriptions from structured metadata (`title`, `brand`, `category`, `price`).

Three approaches are compared:

- Base LLM with prompt engineering  
- RAG‑enhanced LLM (FAISS retrieval + context injection)  
- QLoRA‑fine‑tuned LLM on Mistral‑7B  

The goal: automate descriptions while keeping control over style and quality.

## Results

- Base LLM: good baseline quality  
- RAG‑enhanced: +3.2% in quality (context‑based accuracy)  
- Fine‑tuned model: +1.4% in quality and more stable style  

Best style: **technical** (~0.435 composite score)  
→ mixes BLEU, ROUGE‑L, and semantic similarity.

## How This Can Be Used in a Company

This pipeline can be used to:

- Generate product descriptions from catalog data automatically  
- Maintain consistent tone (e.g., `marketing`, `technical`, `short`)  
- Reduce manual writing time from hours to seconds  
- Scale content creation for large or growing catalogs  

Example:  
An e‑commerce store can plug its product feed into this pipeline and automatically generate SEO‑friendly descriptions for thousands of SKUs.

## Business Impact

- Cut time and cost of content creation  
- Improve description quality and consistency  
- Adapt tone to different audiences (B2B vs. B2C, technical vs. marketing)  
- Build a reusable, reproducible pipeline for future catalogs  

## Tech Stack

- Python
- Hugging Face Transformers
- PEFT (QLoRA)
- Mistral‑7B
- FAISS
- FastAPI
- Streamlit

## Evaluation Plots

- ![Barplot comparison](assets/Eval.png)
- ![Boxplot comparison](assets/Eval_2.png)
- ![Composite score by style](assets/Composite.png)
- ![RAG results](assets/RAG.png)
- ![LoRA results](assets/Lora.png)

## Demo Application

Interactive Streamlit UI to test the model and compare outputs.

![Home page](assets/Home_page.png)  
![Example 1](assets/Example_1.png)

<p align="left">
  <img src="assets/Example_3_video2.gif" width="600">
</p>

Run locally:

```bash
python3 -m streamlit run app/app.py
```

> The Streamlit app calls a FastAPI backend via `API_URL` (configured for a ngrok URL in `app/app.py`).

## How to Reproduce

1. `01_Load_&_Clean.ipynb`
2. `02_Prompt_Engineering.ipynb`
3. `03_Evaluation.ipynb`
4. *(Optional)* `04_RAG.ipynb`
5. `05_LoRA.ipynb` — save adapter to `models/final_adapter/`
6. `06_API.ipynb` — start FastAPI, get backend URL
7. Update `API_URL` in `app/app.py` and run Streamlit

## Work With Me

I help companies automate content generation with LLMs.

I can help you:
- Fine‑tune or adapt LLMs for your product catalog  
- Build pipelines from metadata to product descriptions  
- Integrate LLMs into your existing workflows (API, batch export)  

Available for freelance projects.
