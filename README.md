🌍 AI-Powered Travel Planner App
An AI-powered travel planning application designed to assist users in finding optimal travel options between a given source and destination. The system leverages LangChain and Google GenAI to process user inputs and generate various travel choices such as cab, train, bus, and flights, along with their estimated costs.

📌 Project Overview
It is an AI-based travel planner that efficiently fetches travel information and recommends the best travel options based on user preferences.

🎯 Objectives
✅ Develop an AI application that efficiently fetches travel information
✅ Utilize LangChain to manage LLM-based interactions for user queries
✅ Integrate Google GenAI for intelligent data processing and response generation
✅ Ensure an intuitive user interface for seamless interaction

🏗️ System Architecture
🔹 Components
User Interface (UI): A web-based application using Streamlit to collect user input
LangChain Framework: For managing LLM-based conversation flow
Google GenAI Model: To generate intelligent travel recommendations
🔹 Workflow
User inputs source and destination in the application
The system processes the input using LangChain and Google GenAI
The model generates a structured response containing different travel modes and their estimated prices
The user receives the response with travel recommendations
🛠️ Tech Stack
Programming Language: Python
User Interface: Streamlit
Framework: LangChain
AI Model: Google GenAI
Notebook: Jupyter Notebook for development and testing
📦 Installation
Install dependencies:
cd travel-planner  
pip install -r requirements.txt  
Start the app:
streamlit run app.py  
💡 How to Use
Enter the source and destination.
View recommendations for different travel options and estimated costs.
Customize and save your travel plan.
📂 Jupyter Notebook
The project includes a Jupyter Notebook (travel_planner.ipynb) for testing and refining the AI model. Open it using:
jupyter notebook travel_planner.ipynb  
🤝 Contributing
Feel free to submit issues and pull requests to improve the app.

📝 License
This project is licensed under the MIT License.

