from os import rename
import pandas as pd


# Load Excel file into DataFrame
df = pd.read_excel(r"/content/sample_data/Customer_Call_List.xlsx")
df

# Remove duplicate rows
df = df.drop_duplicates()
df

# Drop irrelevant column
df = df.drop(columns = "Not_Useful_Column")
df

-

# Strip specified characters from start/end of 'Last_Name'
df["Last_Name"]= df["Last_Name"].str.strip("123._/")
df

# Convert phone numbers to strings and remove non-digit characters
df["Phone_Number"] = df["Phone_Number"].apply(lambda x: str(x))


# Convert phone numbers to strings and remove non-digit characters
df["Phone_Number"] = df["Phone_Number"].astype(str).str.replace(r'\D', '', regex=True)
# Format phone numbers as xxx-xxx-xxx

df["Phone_Number"] = df["Phone_Number"].apply(lambda x: '-'.join([x[:3], x[3:6], x[6:]]))
df

-

# Split 'Address' into 'Street_Address', 'State', and 'Zip_Code' columns
df[["Street_Address", "State", "Zip_Code"]] = df["Address"].str.split(pat=',', n=2, expand=True)
df

# Drop original 'Address' column
df.drop(columns=["Address"], inplace=True)
df

-

# Simplify 'Paying Customer' and 'Do_Not_Contact' flags to 'Y'/'N'
df["Paying Customer"] = df["Paying Customer"].str.replace('Yes','Y')
df

df["Paying Customer"] = df["Paying Customer"].str.replace('No','N')
df

df["Do_Not_Contact"] = df["Do_Not_Contact"].str.replace('Yes','Y')
df

df["Do_Not_Contact"] = df["Do_Not_Contact"].str.replace('No','N')
df

-

# Replace NaN with empty strings
df = df.fillna('')
df

# Remove rows where contact is not allowed or missing
for x in df.index:
  if df.loc[x, "Do_Not_Contact"] == 'Y' or df.loc[x, "Do_Not_Contact"] == '':
      df.drop (x, inplace=True)
df

-

# Remove rows with invalid phone numbers
for x in df.index:
  if df.loc[x, "Phone_Number"] == '--':
    df.drop (x, inplace=True)
df

# Reset index to 0,1,2...
df = df.reset_index(drop=True)
df

# Name the index column
df.index.name = 'Index'
df
