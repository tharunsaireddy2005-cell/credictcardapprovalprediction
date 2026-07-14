import pandas as pd
import numpy as np

# =========================
# LOAD DATASETS
# =========================
app = pd.read_csv("application_record.csv")
credit = pd.read_csv("credit_record.csv")

print("\n================ DATA LOADED ================\n")

# =========================
# CLEAN APPLICATION DATA
# =========================
app = app.dropna()

app["DAYS_BIRTH"] = abs(app["DAYS_BIRTH"])
app["DAYS_EMPLOYED"] = abs(app["DAYS_EMPLOYED"])
app["FAMILY_SIZE"] = app["CNT_FAM_MEMBERS"]

categorical_cols = [
    "CODE_GENDER",
    "FLAG_OWN_CAR",
    "FLAG_OWN_REALTY",
    "NAME_INCOME_TYPE",
    "NAME_EDUCATION_TYPE",
    "NAME_FAMILY_STATUS",
    "NAME_HOUSING_TYPE",
    "OCCUPATION_TYPE"
]

app_encoded = pd.get_dummies(app, columns=categorical_cols)

print("Application Data After Cleaning:")
print(app_encoded.head())

print("\nShape:", app_encoded.shape)

# =========================
# CLEAN CREDIT DATA
# =========================
credit["MONTHS_BALANCE"] = abs(credit["MONTHS_BALANCE"])

credit_grouped = credit.groupby("ID").agg({
    "MONTHS_BALANCE": ["min", "max", "count"],
    "STATUS": lambda x: (x == "C").sum()
})

credit_grouped.columns = [
    "OPEN_MONTH",
    "END_MONTH",
    "TOTAL_MONTHS",
    "GOOD_PAYMENTS"
]

credit_grouped = credit_grouped.reset_index()

print("\nCredit Data After Grouping:")
print(credit_grouped.head())

print("\nShape:", credit_grouped.shape)

# =========================
# MERGE DATASETS
# =========================
final_data = pd.merge(app_encoded, credit_grouped, on="ID", how="inner")

print("\nMerged Dataset:")
print(final_data.head())

print("\nFinal Shape:", final_data.shape)

# =========================
# TARGET CREATION
# =========================
final_data["TARGET"] = (
    final_data["GOOD_PAYMENTS"] > final_data["GOOD_PAYMENTS"].median()
).astype(int)

print("\nTarget Column Added Successfully")

print("\nTarget Value Counts:")
print(final_data["TARGET"].value_counts())

# =========================
# FINAL SUMMARY OUTPUT
# =========================
print("\n================ SUMMARY ================")
print("Total Records:", final_data.shape[0])
print("Total Features:", final_data.shape[1])
print("Target Distribution:")
print(final_data["TARGET"].value_counts())

print("\nData Cleaning Completed Successfully!")