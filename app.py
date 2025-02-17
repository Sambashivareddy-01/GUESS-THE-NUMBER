import streamlit as st
import random

# Initialize session state variables before using them
if 'secret_number' not in st.session_state:
    st.session_state.secret_number = random.randint(1, 100)
    st.session_state.attempts = 0
    st.session_state.max_attempts = 10  # Initialize before using

st.title("🎯 Guess the Number Game!")
st.write(f"I'm thinking of a number between 1 and 100. You have {st.session_state.max_attempts} attempts.")

st.image("./img/images.jpeg")

guess = st.number_input("Enter your guess:", min_value=1, max_value=100, step=1)
submit = st.button("Submit Guess")

# Function to reset the game
def reset_game():
    st.session_state.secret_number = random.randint(1, 100)
    st.session_state.attempts = 0

if submit:
    st.session_state.attempts += 1

    if guess == st.session_state.secret_number:
        st.balloons()
        st.success(f"🎉 Congratulations! You guessed the number in {st.session_state.attempts} attempts!")

        # Reset Button
        if st.button(" Play Again"):
            reset_game()
    elif st.session_state.attempts == st.session_state.max_attempts:
        st.error(f"Sorry! You've used all {st.session_state.max_attempts} attempts. The number was {st.session_state.secret_number}.")
        
        # Reset Button after losing
        if st.button("Play Again"):
            reset_game()
    elif guess < st.session_state.secret_number:
        st.warning("Too low! Try again.")
    else:
        st.warning("Too high! Try again.")

    st.write(f"Attempts remaining: {st.session_state.max_attempts - st.session_state.attempts}")
