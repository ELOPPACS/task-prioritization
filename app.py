from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def calculate_roi(hours_current, hours_automated):
    """Calculate the ROI score based on time savings."""
    savings = 1 - (hours_automated / hours_current)
    return max(0, savings * 30)  # Scale to 30 points

def calculate_business_impact(impact, urgency):
    """Calculate Business Impact score (scaled to 40 points)."""
    return ((impact + urgency) / 2) * 8

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/calculate", methods=["POST"])
def calculate():
    data = request.json
    hours_current = float(data["hours_current"])
    hours_automated = float(data["hours_automated"])
    feasibility = float(data["feasibility"])
    impact = float(data["impact"])
    urgency = float(data["urgency"])

    roi_score = calculate_roi(hours_current, hours_automated)
    business_impact_score = calculate_business_impact(impact, urgency)

    total_score = roi_score + feasibility + business_impact_score

    return jsonify({"total_score": round(total_score, 2)})

if __name__ == "__main__":
    app.run(debug=True)
