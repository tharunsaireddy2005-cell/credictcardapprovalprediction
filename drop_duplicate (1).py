import pandas as pd

# Create sample dataset with duplicate records
app = pd.DataFrame({
    'Applicant_ID': [101, 102, 103, 101, 104, 105, 102],
    'CODE_GENDER': ['M', 'F', 'M', 'M', 'F', 'M', 'F'],
    'FLAG_OWN_CAR': ['Y', 'N', 'Y', 'Y', 'N', 'Y', 'N'],
    'FLAG_OWN_REALTY': ['Y', 'Y', 'N', 'Y', 'N', 'Y', 'Y'],
    'CNT_CHILDREN': [0, 1, 2, 0, 1, 0, 1],
    'AMT_INCOME_TOTAL': [180000, 120000, 250000, 180000, 150000, 200000, 120000],
    'NAME_INCOME_TYPE': ['Working', 'Pensioner', 'Working', 'Working', 'Student', 'Working', 'Pensioner'],
    'NAME_EDUCATION_TYPE': ['Higher', 'Secondary', 'Higher', 'Higher', 'Secondary', 'Higher', 'Secondary'],
    'NAME_FAMILY_STATUS': ['Married', 'Single', 'Married', 'Married', 'Single', 'Married', 'Single'],
    'NAME_HOUSING_TYPE': ['House', 'Apartment', 'House', 'House', 'Apartment', 'House', 'Apartment'],
    'DAYS_BIRTH': [-12000, -14000, -10000, -12000, -13000, -11000, -14000],
    'DAYS_EMPLOYED': [-3000, -5000, -2500, -3000, -4000, -3500, -5000],
    'FLAG_MOBIL': [1, 1, 1, 1, 1, 1, 1],
    'FLAG_WORK_PHONE': [1, 0, 1, 1, 0, 1, 0],
    'FLAG_PHONE': [1, 1, 0, 1, 1, 0, 1],
    'FLAG_EMAIL': [0, 1, 0, 0, 1, 1, 1],
    'OCCUPATION_TYPE': ['Manager', 'Clerk', 'Engineer', 'Manager', 'Student', 'Doctor', 'Clerk'],
    'CNT_FAM_MEMBERS': [2, 3, 4, 2, 3, 2, 3]
})

print("Before removing duplicates:")
print(app)

# Remove duplicate Applicant_ID records (keep the first occurrence)
app = app.drop_duplicates(subset='Applicant_ID', keep='first')

print("\nAfter removing duplicates:")
print(app)
app = app.drop_duplicates(
    subset=[
        'CODE_GENDER', 'FLAG_OWN_CAR', 'FLAG_OWN_REALTY',
        'CNT_CHILDREN', 'AMT_INCOME_TOTAL',
        'NAME_INCOME_TYPE', 'NAME_EDUCATION_TYPE',
        'NAME_FAMILY_STATUS', 'NAME_HOUSING_TYPE',
        'DAYS_BIRTH', 'DAYS_EMPLOYED',
        'FLAG_MOBIL', 'FLAG_WORK_PHONE',
        'FLAG_PHONE', 'FLAG_EMAIL',
        'OCCUPATION_TYPE', 'CNT_FAM_MEMBERS'
    ],
    keep='first'
)

print(app)

