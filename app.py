import streamlit as st
import re
import time
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser

# Streamlit UI Setup
st.set_page_config(page_title="AI Travel Planner", page_icon="✈️", layout="wide")
st.title("🌍 AI Travel Planner ✈️")
st.write("Plan your trip with cost estimates, summary, travel details, and food recommendations!")

col1, col2 = st.columns(2)
with col1:
    source = st.text_input("📍 Enter Source Location:", help="Start typing and select a location")
with col2:
    destination = st.text_input("📍 Enter Destination:", help="Start typing and select a location")

budget = st.number_input("💰 Budget (in your currency):", min_value=0, step=100)
travel_time = st.selectbox("⏰ Preferred Travel Time:", ["🌅 Morning", "🌞 Afternoon", "🌆 Evening", "🌙 Night", "Anytime"])
num_travelers = st.number_input("👥 Number of Travelers:", min_value=1, step=1)
preferred_mode = st.multiselect("🚗 Preferred Mode of Transport:", ["🏍️ Bike", "🚖 Cab", "🚌 Bus", "🚆 Train", "✈️ Flight", "Any"])

# Helper functions

def clean_markdown(text):
    text = re.sub(r'\*\*(.*?)\*\*', r'\1', text)
    text = re.sub(r'\*(.*?)\*', r'\1', text)
    return text.strip()

def parse_response(response):
    response = clean_markdown(response)
    sections = {}
    for line in response.splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            sections[key.strip()] = value.strip()
    return sections

def render_section(label, key, sections):
    with st.expander(label):
        content = sections.get(key, "").strip()
        st.write(content if content else "Not available.")

# Main app logic

if st.button("🛫 Plan My Trip"):
    if source and destination:
        with st.spinner("🔄 Fetching travel options and food recommendations..."):
            time.sleep(1)

            # Extra-strict system prompt for reliable output fields
            system_prompt = """
You are an AI Travel Planner. ONLY return the following, using these exact labels and nothing else. No introductions, no explanations.

Cost Estimate: (give a currency value and short explanation)
Travel Time: (how long does the trip usually take)
Distance: (distance between source and destination)
Mode of Transport: (suggested best mode)
Departure Info: (suggest good departure time with respect to requested preference)
Food Suggestions: (near or at the destination)
Trip Summary: (one short paragraph summary of the trip plan)
"""

            human_prompt = """
Find travel options from {source} to {destination}.
Budget: {budget}
Travel Time: {travel_time}
Number of Travelers: {num_travelers}
Preferred Modes: {preferred_mode}
"""

            chat_template = ChatPromptTemplate.from_messages([
                ("system", system_prompt),
                ("human", human_prompt)
            ])

            GEMINI_API_KEY = "AIzaSyC0N2YTXsODJpZnjoiGSOhM1VPH40XmQ4U"
            chat_model = ChatGoogleGenerativeAI(api_key=GEMINI_API_KEY, model="gemini-2.0-flash-exp")
            parser = StrOutputParser()
            chain = chat_template | chat_model | parser

            raw_input = {
                "source": source,
                "destination": destination,
                "budget": budget,
                "travel_time": travel_time,
                "num_travelers": num_travelers,
                "preferred_mode": ", ".join(preferred_mode) if preferred_mode else "Any"
            }

            try:
                response = chain.invoke(raw_input)
                st.write("**Raw AI Response:**", response)  # Debug: show the actual response
                sections = parse_response(response)

                st.success("✅ Trip Planned Successfully!")
                st.subheader("🗂️ Travel Plan Summary")

                render_section("💰 Cost Estimate", "Cost Estimate", sections)
                render_section("⏰ Travel Time", "Travel Time", sections)
                render_section("📏 Distance", "Distance", sections)
                render_section("🚗 Mode of Transport", "Mode of Transport", sections)
                render_section("🕓 Departure Info", "Departure Info", sections)
                render_section("🍽️ Food Suggestions", "Food Suggestions", sections)
                render_section("📝 Trip Summary", "Trip Summary", sections)
            except Exception as e:
                st.error(f"❌ Error: {str(e)}")
    else:
        st.warning("⚠️ Please enter both source and destination.")
