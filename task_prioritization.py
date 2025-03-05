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

def main():
    print("\n🚀 Task Prioritization Calculator 🚀")
    print("Answer the following questions to calculate the task priority score.")

    # Get user inputs with clear explanations
    hours_current = float(input("\n⏳ How many hours does the task currently take? (e.g., 10, 20, etc.) ➜ "))
    hours_automated = float(input("🤖 If automated, how many hours will it take? (e.g., 2, 5, etc.) ➜ "))

    print("\n✅ Feasibility Score (0-30)")
    print("   0  - Not feasible (impossible to automate)")
    print("   10 - Requires significant effort but possible")
    print("   20 - Moderately difficult but manageable")
    print("   30 - Very easy to automate (low effort)")
    feasibility = float(input("   ➜ Enter a feasibility score (0-30): "))

    print("\n📈 Business Impact Score (1-5)")
    print("   1 - Very low impact (not important)")
    print("   2 - Low impact (useful but not critical)")
    print("   3 - Moderate impact (beneficial to the business)")
    print("   4 - High impact (important for efficiency and success)")
    print("   5 - Critical impact (business cannot function well without it)")
    impact = float(input("   ➜ Enter an impact score (1-5): "))

    print("\n🔥 Urgency Score (1-5)")
    print("   1 - No urgency (can wait indefinitely)")
    print("   2 - Low urgency (not needed soon)")
    print("   3 - Moderate urgency (needed soon but not critical)")
    print("   4 - High urgency (should be implemented quickly)")
    print("   5 - Critical urgency (must be done immediately)")
    urgency = float(input("   ➜ Enter an urgency score (1-5): "))

    # Calculate scores
    roi_score = calculate_roi(hours_current, hours_automated)
    feasibility_score = calculate_feasibility(feasibility)
    business_impact_score = calculate_business_impact(impact, urgency)

    # Final priority score
    total_score = roi_score + feasibility_score + business_impact_score

    # Show the results
    print("\n🎯 Task Prioritization Results:")
    print(f"   - ROI Score: {roi_score:.2f}/30")
    print(f"   - Feasibility Score: {feasibility_score:.2f}/30")
    print(f"   - Business Impact Score: {business_impact_score:.2f}/40")
    print(f"   - 🔥 Total Score: {total_score:.2f}/100")

    # Interpretation
    if total_score >= 80:
        print("\n✅ This task is HIGH PRIORITY! Automate ASAP!")
    elif 50 <= total_score < 80:
        print("\n⚠️ This task is MEDIUM PRIORITY. Consider automating soon.")
    else:
        print("\n❌ This task is LOW PRIORITY. Not urgent for automation.")

if __name__ == "__main__":
    main()
