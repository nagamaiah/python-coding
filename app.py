import streamlit as st

st.title("My Streamlit App. Naggg")
st.write("Welcome to your basic Streamlit app!")

# HTML form for username and email
st.markdown("""
    <style>
        .form-container {
            background-color: #f9f9f9;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.05);
            max-width: 400px;
            margin: 30px auto;
        }
        .form-container input[type=text], .form-container input[type=email] {
            width: 100%;
            padding: 8px;
            margin: 8px 0 16px 0;
            border: 1px solid #ccc;
            border-radius: 4px;
        }
        .form-container input[type=submit] {
            background-color: #4CAF50;
            color: white;
            padding: 10px 20px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
        }
        .form-container input[type=submit]:hover {
            background-color: #45a049;
        }
    </style>
    <form class="form-container" method="POST">
        <label for="username">Username:</label><br>
        <input type="text" id="username" name="username" required><br>
        <label for="email">Email:</label><br>
        <input type="email" id="email" name="email" required><br>
        <input type="submit" value="Submit">
    </form>
""", unsafe_allow_html=True)

