import streamlit as st
import google.generativeai as genai
import mocktrialapi

genai.configure(api_key=mocktrialapi.api_key) #Enter your API Key from Google AI Studio 

st.title("MockTrial Bot⚖️")
st.caption("An AI Solution to all your Legal Problems")

st.divider()

with st.chat_message("assistant"):
    st.text("Hi I'm MockTrial Bot...")
# User prompt input for the legal question
with st.chat_message("user"):
    user_prompt = st.text_area("Write your Legal issue here....")

# Generate Response Button
if st.button("Generate Response"):
    with st.spinner("Generating response..."):
        try:
            def generate_response(prompt):
                model = genai.GenerativeModel("gemini-pro")


                # Send the user prompt to the model
                response = model.generate_content(
                    "Give me breif legal advice headings FOR PROSECUTION, FOR DEFENDANT, EVIDENCES, IMPORTANT POINTS " + prompt
                )

                # Display the response in markdown format
                with st.container():
                    with st.chat_message("assistant"):
                        st.markdown(response.text)

            generate_response(user_prompt)
        except Exception as e:
            st.error(f"An error occurred: {e}")
