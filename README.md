# CoT-Driven AI Warfare & Resource Management

## 📌 Project Overview
**CoT-Driven AI Warfare & Resource Management** is a simulation where AI agents use **Chain of Thought (CoT) reasoning** for **military strategy, diplomacy, espionage, and resource management**. The AI evolves over time using **Deepseek R1 1.5B via Ollama**, making adaptive decisions in a dynamic war-driven world.

## 🚀 Features
- **Multi-Step Battle Planning:** AI generals simulate potential outcomes before attacking.
- **AI-Driven Diplomacy:** Entities form alliances, betray each other, or engage in peace talks.
- **Espionage & Deception:** Spies use misinformation and sabotage against enemies.
- **Resource & Economy Management:** AI controls logistics, war funding, and supply chains.
- **Reinforcement Learning:** AI learns from past wars to optimize strategies over time.
- **Persistent Memory:** Agent data is stored in **JSON files**, ensuring the simulation resumes from the last saved state on every run.


## 🛠️ Setup & Installation
### **1️⃣ Install Dependencies**
Ensure you have **Python 3.9+** installed. Then, install required packages:
```bash
pip install -r requirements.txt
```
### **2️⃣ Set Up Ollama & Deepseek R1**
Follow the Ollama documentation to set up Deepseek R1:
```bash
ollama pull deepseek-r1-1.5b
```
### **3️⃣ Run the Simulation**
Execute the main simulation:
```bash
python main.py
```

## 🔄 Persistent Data Storage
- **All agent memory and game state** are stored in **JSON files** under `data/`.
- The simulation **resumes from the last saved state** when restarted.
- Changes are automatically **saved after every turn**.

## 📚 Future Enhancements
- **AI-Self Learning:** Improve reinforcement learning for **adaptive tactics**.
- **GUI/Visualization:** Integrate **map-based war simulations**.
- **More Complex AI Strategies:** Evolve political systems within factions.


