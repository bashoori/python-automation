import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Automation Dashboard", page_icon="🤖", layout="wide")

st.title("🤖 Python Automation Dashboard")
st.markdown("Visualize data scraped and automated with Selenium.")

data_path = "data/scraped_data.csv"

if os.path.exists(data_path):
    df = pd.read_csv(data_path)
    st.success("✅ Data loaded successfully!")

    # Show dataset preview
    st.subheader("📄 Scraped Data Preview")
    st.dataframe(df, use_container_width=True)

    # Basic metrics
    st.subheader("📊 Summary")
    st.write(f"Total Records: {len(df)}")
    if "Links" in df.columns:
        unique_links = df['Links'].nunique()
        st.write(f"Unique Links: {unique_links}")

    # Search/filter box
    search_term = st.text_input("🔍 Search term:")
    if search_term:
        filtered = df[df.apply(lambda row: row.astype(str).str.contains(search_term, case=False).any(), axis=1)]
        st.dataframe(filtered)
        st.write(f"🔎 Found {len(filtered)} matching rows.")
    else:
        st.info("Type a keyword above to filter the data.")

    # Download CSV
    st.download_button(
        label="💾 Download CSV",
        data=df.to_csv(index=False).encode('utf-8'),
        file_name="scraped_data.csv",
        mime="text/csv",
    )
else:
    st.error("❌ No data found. Please run the scraper first.")
