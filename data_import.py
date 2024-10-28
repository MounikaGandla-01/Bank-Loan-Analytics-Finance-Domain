from sqlalchemy import create_engine
import pandas as pd

# Step 1: Define database connection string
db_url = "mysql+pymysql://root:Root@127.0.0.1:3306/bank_loan"
engine = create_engine(db_url)

# Step 2: Read CSV into a Pandas DataFrame
df = pd.read_csv(r"C:\Users\mouni\Downloads\LOAN.csv")

# Step 3: Import data into the database table
df.to_sql('loan_data', con=engine, if_exists='append', index=False)

print("Data imported successfully!")
