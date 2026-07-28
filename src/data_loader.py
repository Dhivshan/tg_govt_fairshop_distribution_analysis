import pandas as pd
import glob
import os

# Path to your CSV files (adjust folder path as needed)
# Example: "data/shop-wise-trans-details_*_2023.csv"
file_paths = glob.glob("shop-wise-trans-details_*_2023.csv") + \
             glob.glob("shop-wise-trans-details_*_2024.csv") + \
             glob.glob("shop-wise-trans-details_*_2025.csv")

print(f"Found {len(file_paths)} files")

dfs = []
for fp in file_paths:
    # Extract year from filename (assuming format: shop-wise-trans-details_1_2023.csv)
    filename = os.path.basename(fp)
    year = filename.split("_")[-1].replace(".csv", "")

    # Read CSV and add year column
    df = pd.read_csv(fp)
    df['year'] = int(year)

    dfs.append(df)

# Combine all into one master DataFrame
master_df = pd.concat(dfs, ignore_index=True)

# Step 2: Load and combine all Card Status CSVs (year-wise)
card_files = glob.glob("fpshop-card-status_*_2023.csv") + \
             glob.glob("fpshop-card-status_*_2024.csv") + \
             glob.glob("fpshop-card-status_*_2025.csv")

card_dfs = []
for fp in card_files:
    filename = os.path.basename(fp)
    year = filename.split("_")[-1].replace(".csv", "")
    df = pd.read_csv(fp)
    df['year'] = int(year)
    card_dfs.append(df)

card_status_df = pd.concat(card_dfs, ignore_index=True)

# Step 3: Load FPS Locations (static dataset)
fps_locations_df = pd.read_csv("shop-status-details_6_2025.csv")

print(master_df.shape)
print(card_status_df.shape)
print(fps_locations_df.shape)

# Step 4: Triple Join on shopNo, distCode, and year
unified_df = master_df.merge(card_status_df, on=['shopNo','distCode','year'], how='inner') \
                            .merge(fps_locations_df, on=['shopNo','distCode'], how='inner')

# Step 5: Save unified dataset
unified_df.to_csv("unified_master.csv", index=False)

# Quick checks
print(unified_df.shape)
print(unified_df[['shopNo','distCode','year']].head())

# Save master_df to a CSV file
# master_df.to_csv("master_transactions.csv", index=False)
# card_status_df.to_csv("master_card_status.csv", index=False)

