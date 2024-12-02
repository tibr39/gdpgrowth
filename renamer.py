import pandas as pd


#this renames the columns of the dataset to a more understandable and simplifed form

column_names = [
    "country_id",
    "country",
    "year",
    "ama_exchange_rate",
    "imf_exchange_rate",
    "population",
    "currency",
    "per_capita_gni",
    "agriculture_fishing_isic_a_b",
    "changes_in_inventories",
    "construction_isic_f",
    "exports_goods_services",
    "final_consumption",
    "govt_consumption",
    "gross_capital_formation",
    "fixed_capital_formation",
    "household_consumption",
    "imports_goods_services",
    "manufacturing_isic_d",
    "mining_manufacturing_utilities_isic_c_e",
    "other_activities_isic_j_p",
    "total_value_added",
    "transport_communication_isic_i",
    "wholesale_retail_isic_g_h",
    "gni_usd",
    "gdp"
]

df = pd.read_csv("countriesecoindexes.csv")

i = 0

for columns in column_names:

    df.rename(columns={df.columns[i]: columns}, inplace=True)
    i+=1
print(df)


df.to_csv('countriesecoindexes.csv', index=False)




