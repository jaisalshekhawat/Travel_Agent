# 🧳 Travel Agent (AI-powered)

An AI-powered **Travel Agent Assistant** built using **Azure OpenAI**.  
It helps users plan trips by suggesting must-see attractions, landmarks, and experiences for any destination.  

---

## ✨ Features
- 🌍 Get travel recommendations for any destination  
- 🤖 Uses **Azure OpenAI Chat Completions API**  
- 🔑 Secure environment configuration with `.env`  
- 🐍 Built with **Python 3.11+**  
- 🛠 Easy to extend for more travel-related features (itineraries, costs, bookings, etc.)  

---

## 📂 Project Structure
Travel_Agent/
│
├── chat_completion.py # Main script to query AI assistant
├── chat_summary.py # (Optional) LangGraph testing for summaries
├── .env # Environment variables (not tracked in GitHub)
├── requirements.txt # Python dependencies
└── README.md # Project documentation


---

## ⚙️ Setup & Installation

Follow these steps to set up and run the project:

### 1. Clone the repository
```bash
git clone https://github.com/jaisalshekhawat/Travel_Agent.git
cd Travel_Agent

# On Windows
python -m venv venv
venv\Scripts\activate

# On Linux/Mac
python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt

If you don’t have a requirements.txt, create one with:
pip install openai python-dotenv
pip freeze > requirements.txt

Create a .env file in the project root and add your Azure OpenAI credentials:
AZURE_OPENAI_ENDPOINT=your_azure_openai_endpoint
AZURE_API_VERSION=2023-07-01-preview
AZURE_OPENAI_API_KEY=your_api_key
AZURE_OPENAI_CHAT_DEPLOYMENT=your_deployment_name

Run the project
python chat_completion.py
