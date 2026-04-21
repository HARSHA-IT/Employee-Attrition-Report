import pandas as pd
import numpy as np

np.random.seed(42)

n = 1000

data = pd.DataFrame({
    "Employee_ID": range(1, n+1),
    "Age": np.random.randint(22, 60, n),
    "Department": np.random.choice(["Sales", "R&D", "HR", "Finance", "IT"], n),
    "Job_Role": np.random.choice(["Executive", "Manager", "Associate", "Analyst"], n),
    "Attrition": np.random.choice(["Yes", "No"], n, p=[0.2, 0.8]),
    "Monthly_Income": np.random.randint(3000, 20000, n),
    "Performance_Rating": np.random.randint(1, 6, n),
    "Years_at_Company": np.random.randint(0, 20, n)
})

# Save CSV
data.to_csv("employee_dataset.csv", index=False)

print("Dataset created successfully!")