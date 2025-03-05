from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def calculate_roi(hours_current, hours_automated):
    """Calculate the ROI score based on time savings."""
    savings = 1 - (hours_automated / hours_current)
    return max(0, savings * 30)  # Scale to 30 points

def calculate_feasibility(feasibility_score):
    """Feasibility score is directly given by the user (0-30)."""
    return feasibility_score  # Max 30 points

def calculate_business_impact(impact, urgency):
    """Calculate the Business Impact score based on importance and urgency."""
    return ((impact + urgency) / 2) * 8  # Scale to 40 points

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
    feasibility_score = calculate_feasibility(feasibility)
    business_impact_score = calculate_business_impact(impact, urgency)

    total_score = roi_score + feasibility_score + business_impact_score

    return jsonify({
        "roi_score": round(roi_score, 2),
        "feasibility_score": round(feasibility_score, 2),
        "business_impact_score": round(business_impact_score, 2),
        "total_score": round(total_score, 2)
    })

if __name__ == "__main__":
    app.run(debug=True)
