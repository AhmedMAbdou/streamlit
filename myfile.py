import streamlit as st

def main():
    st.title("Button Demo")

    # Add a button to the app
    button_clicked = st.button("Click me")

    # Check if the button is clicked
    if button_clicked:
        st.write("Hello")


if __name__ == "__main__":
    main()
