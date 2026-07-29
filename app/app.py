import streamlit as st
import pandas as pd
import geopandas as gpd
import folium
from streamlit_folium import st_folium

# --- Load Data ---
df = pd.read_csv("..//data//clustering_results_streaming_2.csv")

st.write("Columns in CSV:", df.columns.tolist())
st.write("Number of rows:", len(df))
st.write("Sample data:", df.head())

# --- Sidebar Filters ---
st.sidebar.header("Filters")
district = st.sidebar.selectbox("Select District", sorted(df["distCode"].unique()))
year = st.sidebar.selectbox("Select Year", sorted(df["year"].unique()))

filtered_df = df[(df["distCode"] == district) & (df["year"] == year)]

# --- Geospatial Map ---
st.header("Shop Clusters Map")
m = folium.Map(location=[17.5, 78.5], zoom_start=7)  # Telangana center approx

for _, row in filtered_df.iterrows():
    folium.CircleMarker(
        location=[row["latitude"], row["longitude"]],
        radius=4,
        color="blue",
        fill=True,
        fill_color=["red", "green", "orange", "purple", "brown"][row["kmeans_cluster"]],
        popup=f"ShopNo: {row['shopNo']} | Cluster: {row['kmeans_cluster']}"
    ).add_to(m)

st_folium(m, width=700, height=500)

# --- Shop Search Tool ---
st.header("Shop Performance Lookup")
shop_id = st.text_input("Enter ShopNo:")

if shop_id:
    shop_data = df[df["shopNo"] == int(shop_id)]
    if not shop_data.empty:
        cluster_id = shop_data["kmeans_cluster"].iloc[0]
        cluster_avg = df[df["kmeans_cluster"] == cluster_id][
            ["utilization_ratio", "rice_wheat_ratio", "trans_volatility"]].mean()

        st.subheader(f"Shop {shop_id} (Cluster {cluster_id})")
        st.write("Shop Performance:")
        st.write(shop_data[["utilization_ratio", "rice_wheat_ratio", "trans_volatility"]])

        st.write("Cluster Average:")
        st.write(cluster_avg)
    else:
        st.warning("ShopNo not found.")
