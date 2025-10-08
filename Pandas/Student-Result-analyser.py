# ----------------------------
# 🧮 Student Result Analyzer
# ----------------------------

import pandas as pd
import matplotlib.pyplot as plt
# Step 1: Load CSV file
df = pd.read_csv('students.csv')
print("🎓 Original Data:")
print(df, "\n")

# Step 2: Calculate Total and Percentage
df['Total'] = df[['Math', 'Science', 'English', 'Computer']].sum(axis=1)
df['Percentage'] = df['Total'] / 4

# Step 3: Determine Overall Rank
df['Overall Rank'] = df['Total'].rank(ascending=False, method='min').astype(int)

# Step 4: Add Subject-wise Ranks
for subject in ['Math', 'Science', 'English', 'Computer']:
    df[f'{subject} Rank'] = df[subject].rank(ascending=False, method='min').astype(int)

# Step 5: Identify Failed Students (Pass mark = 40)
pass_mark = 40
df['Status'] = df.apply(lambda row: 'Fail' if any(row[sub] < pass_mark for sub in ['Math', 'Science', 'English', 'Computer']) else 'Pass', axis=1)

# Step 6: Class Summary
print("📊 Class Average Marks:")
print(df[['Math', 'Science', 'English', 'Computer']].mean(), "\n")

print("🏆 Overall Topper:")
topper = df.loc[df['Total'].idxmax()]
print(f"{topper['Name']} with {topper['Total']} marks ({topper['Percentage']:.2f}%)\n")

print("📈 Subject-wise Toppers:")
for subject in ['Math', 'Science', 'English', 'Computer']:
    top_student = df.loc[df[subject].idxmax(), 'Name']
    print(f"{subject}: {top_student}")

# Step 7: Show Failed Students
failed_students = df[df['Status'] == 'Fail']
if not failed_students.empty:
    print("\n❌ Failed Students:")
    print(failed_students[['Name', 'Math', 'Science', 'English', 'Computer', 'Status']])
else:
    print("\n✅ No failed students!")

# Step 8: Display Processed Data
print("\n📋 Final Processed Data:")
print(df)

# Step 9: Plot Marks Distribution
print("\n📈 Showing Marks Distribution Chart...")
df[['Math', 'Science', 'English', 'Computer']].plot(kind='bar', title='Marks Distribution')
plt.show()
# Step 10: Save Processed Results
df.to_csv('processed_results.csv', index=False)
print("\n💾 Processed results saved successfully as 'processed_results.csv'")