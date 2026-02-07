import pandas as pd

# Load dataset
df = pd.read_csv("dataset.csv")

def predict_placement(cgpa, skill_count):
    # Filter similar CGPA range
    similar = df[
        (df["cgpa"] >= cgpa - 0.5) &
        (df["cgpa"] <= cgpa + 0.5)
    ]

    if cgpa < 6:
        return {
            "chance": 0,
            "lpa": 0,
            "status": "Not Eligible"
        }

    # Placement probability
    placed_ratio = similar["placed"].mean() if not similar.empty else 0.7
    chance = min(95, int(placed_ratio * 100))

    # Expected LPA
    avg_lpa = similar["package_lpa"].mean() if not similar.empty else 4.0
    lpa = round(avg_lpa + skill_count * 0.4, 2)

    return {
        "chance": chance,
        "lpa": lpa,
        "status": "Eligible"
    }
