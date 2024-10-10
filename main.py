# main.py

import streamlit as st
from news_fetcher import fetch_news
from summarizer_ai import summarize_and_get_precautions
from email_sender import send_email


def streamlit_application():
    st.title("Precaution Recommendation System")

    st.markdown("---")
    st.subheader("Enter Topic and Email")
    user_input = st.text_input("Enter a topic or event:")
    user_email = st.text_input("Enter your email to receive response via mail:")

    if st.button("Get Recommendations", key="get_recommendations"):
        if not user_input:
            st.warning("Please enter a topic or event.")
        else:
            with st.spinner("Fetching latest news..."):
                placeholder = st.empty()
                placeholder.info("Fetching latest news...")
                news = fetch_news(user_input)
                placeholder.empty()

            if not news:
                st.warning("No relevant news found. Please try a different query.")
            else:
                with st.spinner("Analyzing news and generating precautions..."):
                    placeholder = st.empty()
                    placeholder.info("Analyzing news and generating precautions...")
                    summary_and_precautions = summarize_and_get_precautions(news["body"])
                    placeholder.empty()
                
                st.markdown("---")
                st.subheader("News Summary and Precautions")
                st.write(summary_and_precautions)

                if user_email:
                    with st.spinner("Sending results to your email..."):
                        placeholder = st.empty()
                        placeholder.info("Sending results to your email...")
                        is_email_success = send_email(
                            user_email,
                            f"Precaution Recommendations: {user_input}",
                            summary_and_precautions,
                        )
                        placeholder.empty()
                    
                    if not is_email_success:
                        st.error("Failed to send email. Please check your email address and try again.")
                    else:
                        st.success("Results sent to your email successfully!")

    st.markdown("---")
    st.info("This system provides precaution recommendations based on the latest news about your chosen topic.")


streamlit_application()
