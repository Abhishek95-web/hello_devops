
import pandas as pd
from evidently import Report
from evidently.presets import DataDriftPreset

# Reference data: the normal distribution
reference = pd.DataFrame({
    "temperature": [20, 21, 22, 20, 21, 22, 23, 21, 20, 22],
    "humidity": [40, 42, 41, 43, 40, 42, 41, 44, 43, 42],
})

# Current data: values have shifted
current = pd.DataFrame({
    "temperature": [30, 31, 32, 30, 31, 32, 33, 31, 30, 32],
    "humidity": [60, 62, 61, 63, 60, 62, 61, 64, 63, 62],
})

report = Report(metrics=[DataDriftPreset()])
result = report.run(
    reference_data=reference,
    current_data=current,
)

result.save_html("evidently_report.html")
print("Monitoring complete. Report saved to evidently_report.html")
