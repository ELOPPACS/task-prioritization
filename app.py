import os
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def calculate_roi(hours_current, hours_automated):
    """Calculate the ROI score based on time savings."""
    savings = 1 - (hours_automated / hours_current)
    return max(0, savings * 30)  # Scale to 30 points

def calculate_feasibility(tools, experience, human_intervention):
    """Feasibility is calculated based on three user inputs (0-30)."""
    return tools + experience + human_intervention  # Each ranges 0-10, max total 30

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

    tools = int(data["tools"])
    experience = int(data["experience"])
    human_intervention = int(data["human_intervention"])

    impact = float(data["impact"])
    urgency = float(data["urgency"])

    roi_score = calculate_roi(hours_current, hours_automated)
    feasibility_score = calculate_feasibility(tools, experience, human_intervention)
    business_impact_score = calculate_business_impact(impact, urgency)

    total_score = roi_score + feasibility_score + business_impact_score

    return jsonify({
        "roi_score": round(roi_score, 2),
        "feasibility_score": round(feasibility_score, 2),
        "business_impact_score": round(business_impact_score, 2),
        "total_score": round(total_score, 2)
    })

# 🔹 Keep-Alive Route for UptimeRobot
@app.route("/keep-alive")
def keep_alive():
    return "I'm alive!", 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Render assigns a dynamic port
    app.run(debug=True, host="0.0.0.0", port=port)
