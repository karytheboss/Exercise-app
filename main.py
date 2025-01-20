#! C:\Users\Karan Bhapse\Desktop\PFE Course Project\myenv\Scripts\python.exe

import streamlit as st

def calculate_bmr(weight, height, age, gender):
    """Calculate Basal Metabolic Rate (BMR) based on gender."""
    if gender.lower() == "male":
        return 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
    else:
        return 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)

def calculate_daily_calories(bmr, goal, timeframe_days):
    """Calculate daily calorie requirements based on goal."""
    weight_change = abs(goal - bmr)  # Total weight to change in kg
    daily_calorie_deficit = (weight_change * 7700) / timeframe_days  # 1 kg = 7700 kcal
    return bmr - daily_calorie_deficit if goal < bmr else bmr + daily_calorie_deficit

def recommend_workout(intensity, goal):
    """Recommend workouts based on intensity and goal."""
    if intensity == "low":
        return [
            "30-minute brisk walk, 5 times a week",
            "Light yoga/stretching 3 times a week",
            "Push-ups: 2 sets of 10-15 reps",
            "Planks: 2 sets of 30 seconds"
        ]
    elif intensity == "moderate":
        return [
            "45-minute jog or cycling, 4-5 times a week",
            "Bodyweight strength training 3 times a week",
            "Bench press: 3 sets of 8-12 reps",
            "Burpees: 2 sets of 10-15 reps",
            "Playing a sport like basketball or soccer 2-3 times a week"
        ]
    else:  # high intensity
        return [
            "60-minute HIIT workout or running, 5-6 times a week",
            "Strength training 4 times a week",
            "Sprint intervals: 10 x 30-second sprints with 1-minute rest",
            "Burpees: 3 sets of 15-20 reps",
            "Planks: 3 sets of 1 minute",
            "Playing a sport like tennis or squash for high-intensity cardio"
        ]

def recommend_diet(calories, goal):
    """Recommend a diet plan based on calorie needs and goal."""
    if goal == "lose":
        return {
            "Calories": calories,
            "Protein": "40%",
            "Carbs": "35%",
            "Fats": "25%",
            "Suggestions": [
                "Lean meats (chicken, fish)",
                "Leafy greens and vegetables",
                "Whole grains (quinoa, brown rice)",
                "Healthy fats (avocado, nuts)",
                "Low-calorie snacks (carrot sticks, cucumbers)"
            ]
        }
    else:  # gain weight
        return {
            "Calories": calories,
            "Protein": "30%",
            "Carbs": "50%",
            "Fats": "20%",
            "Suggestions": [
                "High-calorie foods (nuts, peanut butter, whole milk)",
                "Starchy vegetables (potatoes, sweet potatoes)",
                "Lean proteins",
                "Healthy oils (olive oil, coconut oil)",
                "Smoothies with protein powder, fruits, and nut butter"
            ]
        }

def main():
    st.title("Fitness Plan App")
    st.markdown("Welcome to your personalized fitness and diet planning app! Fill in your details below and get a tailored plan to achieve your goals.")

    # Get user inputs through Streamlit widgets
    current_weight = st.number_input("Enter your current weight (kg):", min_value=0.0, step=0.1)
    target_weight = st.number_input("Enter your target weight (kg):", min_value=0.0, step=0.1)
    timeframe_days = st.number_input("Enter your timeframe (days):", min_value=1, step=1)
    height = st.number_input("Enter your height (cm):", min_value=0.0, step=0.1)
    age = st.number_input("Enter your age:", min_value=1, step=1)
    gender = st.selectbox("Enter your gender:", ["Male", "Female"])

    if st.button("Generate Plan"):
        # Determine goal (lose or gain weight)
        goal = "lose" if current_weight > target_weight else "gain"

        # Calculate BMR and daily calorie needs
        bmr = calculate_bmr(current_weight, height, age, gender)
        daily_calories = calculate_daily_calories(bmr, target_weight, timeframe_days)

        # Determine workout intensity
        weekly_weight_change = abs(target_weight - current_weight) / (timeframe_days / 7)
        if weekly_weight_change < 0.5:
            intensity = "low"
        elif 0.5 <= weekly_weight_change <= 1:
            intensity = "moderate"
        else:
            intensity = "high"

        # Generate recommendations
        workouts = recommend_workout(intensity, goal)
        diet = recommend_diet(daily_calories, goal)

        # Display recommendations
        st.subheader("Personalized Fitness Plan")
        st.markdown(f"**Daily Caloric Needs:** {daily_calories:.2f} kcal")
        st.markdown(f"**Workout Intensity:** {intensity.capitalize()}")

        st.subheader("Recommended Workouts:")
        for workout in workouts:
            st.write(f"- {workout}")

        st.subheader("Recommended Diet:")
        st.markdown(f"- **Calories:** {diet['Calories']:.2f} kcal")
        st.markdown(f"- **Protein:** {diet['Protein']}")
        st.markdown(f"- **Carbs:** {diet['Carbs']}")
        st.markdown(f"- **Fats:** {diet['Fats']}")
        st.markdown("- **Food Suggestions:**")
        for suggestion in diet['Suggestions']:
            st.write(f"  - {suggestion}")

if __name__ == "__main__":
    main()
