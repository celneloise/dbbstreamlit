import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Title 
st.title("How Are You Feeling Today?")

# Text input 
st.header("Welcome to your daily check-in!")
st.text("We'd love to know how you're feeling today.")

# Ask the user how they are feeling
mood = st.text_input("How are you feeling today?", "Type here...")

# Slider to capture mood
mood_slider = st.select_slider(
    "Select your mood today:",
    options=["Not Happy", "Okay", "Happy"],
    help="Choose your mood: Not Happy, Okay, or Happy"
)

# Slider mapping
if mood_slider == 1:
    mood_label = "Not Happy"
elif mood_slider == 2:
    mood_label = "Okay"
else:
    mood_label = "Happy"

# Display the mood chosen
st.write(f"Your mood today: {mood_label}")

# Display the mood input from the user
st.write(f"You said: {mood}")

# Add an interactive plot (Matplotlib)
st.header("Your Mood Visualization")
moods = ['Not Happy', 'Okay', 'Happy']
mood_counts = [0, 0, 0]  # Sample counts for each mood

# Map mood to index and update the count
mood_mapping = {"Not Happy": 0, "Okay": 1, "Happy": 2}
mood_counts[mood_mapping[mood_slider]] += 1  # Update based on selected mood

# Create a bar plot for visualization
fig, ax = plt.subplots()
ax.bar(moods, mood_counts, color=["red", "orange", "green"])
ax.set_title('Mood Distribution')
ax.set_ylabel('Number of Responses')
ax.set_xlabel('Mood')

# Display the plot in Streamlit
st.pyplot(fig)

# Add some additional components to make the app engaging
st.text("Thank you for sharing how you feel!")
st.write("Remember to check in every day!")

