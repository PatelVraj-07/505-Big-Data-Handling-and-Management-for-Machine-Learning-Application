
import pandas as pd

# Large CSV file path
file_path = "Transaction.csv"

# Initialize variables
total_records = 0
running_sum = 0

# Read CSV file in small batches
for chunk in pd.read_csv(file_path, chunksize=10000):

    # Count records in the current chunk
    total_records += len(chunk)

    # Calculate sum of transaction amounts
    running_sum += chunk["Amount"].sum()

# Calculate overall average
if total_records > 0:
    average_transaction = running_sum / total_records
else:
    average_transaction = 0

# Display results
print("Total Records:", total_records)
print("Total Transaction Amount:", running_sum)
print("Average Transaction Value:", average_transaction)