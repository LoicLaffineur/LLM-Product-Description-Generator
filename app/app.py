## python3 -m streamlit run app/app.py

import streamlit as st
import requests

# ── Configuration ──────────────────────────────────────────
API_URL = "https://subproportionally-circinate-alexzander.ngrok-free.dev"

st.set_page_config(
    page_title="Product Description Generator", page_icon="🛍️", layout="wide"
)

# ── Header ─────────────────────────────────────────────────
st.title("🛍️ Product Description Generator")
st.caption("Mistral 7B — Base model vs Fine-tuned (QLoRA) · Amazon Electronics")
st.divider()

# ── Form ───────────────────────────────────────────────────
with st.form("product_form"):
    col1, col2 = st.columns(2)

    with col1:
        title = st.text_input(
            "Product title *",
            placeholder="Samsung Story Station 1TB USB 2.0 Desktop External Hard Drive",
        )
        brand = st.text_input("Brand", placeholder="Samsung")

    with col2:
        category = st.text_input("Category", placeholder="External Hard Drives")
        price = st.text_input("Price", placeholder="89.99")

    style = st.selectbox(
        "Description style",
        ["technical", "marketing", "short"],
        help="Technical style recommended — best composite score (0.435) in evaluation (Notebook 03)",
    )

    submitted = st.form_submit_button("✨ Generate", use_container_width=True)

# ── Generation ─────────────────────────────────────────────
if submitted:
    if not title.strip():
        st.warning("Please enter a product title.")
    else:
        with st.spinner("Generating descriptions..."):
            try:
                response = requests.post(
                    f"{API_URL}/generate",
                    json={
                        "title": title,
                        "brand": brand,
                        "category": category,
                        "price": price,
                        "style": style,
                    },
                    timeout=120,
                )
                response.raise_for_status()
                result = response.json()

                st.divider()

                # ── Results ────────────────────────────────
                col_base, col_ft = st.columns(2)

                with col_base:
                    st.subheader("Base model")
                    st.caption("Mistral 7B · prompt engineering only")
                    st.info(result["base"])
                    st.download_button(
                        label="Download",
                        data=result["base"],
                        file_name="description_base.txt",
                        mime="text/plain",
                    )

                with col_ft:
                    st.subheader("Fine-tuned model")
                    st.caption("Mistral 7B · QLoRA trained on Amazon descriptions")
                    st.success(result["finetuned"])
                    st.download_button(
                        label="Download",
                        data=result["finetuned"],
                        file_name="description_finetuned.txt",
                        mime="text/plain",
                    )

                # ── Metadata ───────────────────────────────
                with st.expander("Request details"):
                    st.json(
                        {
                            "title": title,
                            "brand": brand,
                            "category": category,
                            "price": price,
                            "style": style,
                            "api_url": API_URL,
                        }
                    )

            except requests.exceptions.Timeout:
                st.error(
                    "Request timed out — the model is taking too long to respond. Try again."
                )
            except requests.exceptions.ConnectionError:
                st.error(
                    "Cannot connect to the API. Make sure FastAPI is running and the URL is correct."
                )
            except Exception as e:
                st.error(f"Unexpected error: {e}")

# ── Footer ─────────────────────────────────────────────────
st.divider()
st.caption(
    "Portfolio project · Mistral 7B · HuggingFace Transformers · PEFT QLoRA · FastAPI · Streamlit"
)
