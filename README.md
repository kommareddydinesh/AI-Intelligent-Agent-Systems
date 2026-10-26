# 🤖 AI Models — Intelligent Agent Systems

A Python-based collection of four Artificial Intelligence agent models demonstrating different decision-making strategies through practical, real-world scenarios.

This repository explores how intelligent agents perceive their environment, apply rules or search strategies, make decisions, and produce appropriate actions.

## 📌 Project Overview

The project implements four fundamental AI agent architectures:

1. **Simple Reflex Agent** — Makes decisions using condition-action rules.
2. **Model-Based Reflex Agent** — Uses internal memory to track previous states.
3. **Goal-Based Agent** — Searches for a path to achieve a defined goal.
4. **Utility-Based Agent** — Evaluates conditions using utility scores to recommend suitable decisions.

Each agent is implemented as an independent Python program.

## 🚀 Implemented AI Agents

### 1. Smart Library Silence Monitor

**Agent Type:** Simple Reflex Agent

A library noise monitoring system that evaluates the current noise level and determines whether a warning is required.

**Features**
- Accepts the current noise level in decibels (dB).
- Applies condition-action rules using a threshold of 60 dB.
- Displays a warning when the noise level exceeds the threshold.
- Reports whether the library environment is noisy or quiet.

**Decision Rule**
- If noise > 60 dB → Display a silence warning.
- Otherwise → Report a quiet environment.

**AI Concept:** Decisions are based on the current percept without maintaining internal state.

### 2. Smart Museum Artifact Protection System

**Agent Type:** Model-Based Reflex Agent

A museum security simulation that monitors the distance between visitors and protected artifacts. The agent uses internal memory to determine an appropriate response.

**Features**
- Accepts visitor distance in centimeters.
- Classifies the distance into safe, caution, and restricted zones.
- Stores the warning state in internal memory.
- Escalates a repeated restricted-zone violation to a simulated security alarm when prior warning state is available.
- Displays a security report with the selected action and system status.

**Decision Rules**
- Distance below 50 cm → Issue a warning on the first violation or activate an alarm after a previous warning.
- Distance from 50 cm to below 100 cm → Display a caution message.
- Distance of 100 cm or more → Report a safe distance.

**AI Concept:** Uses percepts and internal state to make decisions.

> Note: The current single-input version starts with fresh memory each time it runs. Therefore, it issues the first warning for a restricted-zone reading rather than detecting a violation from a previous execution.

### 3. Flood Escape Agent

**Agent Type:** Goal-Based Agent

A flood evacuation simulation that searches for a safe route from a citizen's current location to a relief camp while avoiding flooded roads.

**Features**
- Represents the city as a graph of connected locations.
- Accepts the citizen's current location.
- Uses Breadth-First Search (BFS) to find a route.
- Avoids roads identified as flooded.
- Displays the planned route and reports whether the goal is achieved.

**Goal:** Reach the Relief Camp through a route that avoids flooded roads.

**Algorithm:** Breadth-First Search (BFS)

**AI Concept:** Selects actions according to whether they help achieve a predefined goal.

### 4. Wildlife Safari Guide Agent

**Agent Type:** Utility-Based Agent

A safari route recommendation system that evaluates route conditions and calculates a utility score to support decision-making.

**Features**
- Accepts route name and animal sighting probability.
- Evaluates weather conditions.
- Considers road quality and crowd levels.
- Includes fuel cost in the utility calculation.
- Generates a utility score and recommendation.

**Decision Factors**
- Animal sighting chance
- Weather conditions
- Road conditions
- Crowd levels
- Fuel cost

**AI Concept:** Evaluates alternatives using a utility function and selects recommendations according to the resulting score.

## 🛠️ Technologies Used

- **Programming Language:** Python 3
- **AI Concepts:** Simple Reflex, Model-Based Reflex, Goal-Based, and Utility-Based Agents
- **Search Algorithm:** Breadth-First Search (BFS)
- **Python Libraries:** Standard library modules, including `collections.deque` and `datetime` where required
- **Development Environment:** Visual Studio Code
- **Version Control:** Git and GitHub

No external Python packages are required for the provided implementations.

## 📂 Repository Structure

```text
AI-MODELS/
│
├── README.md
├── 01_Simple_Reflex_Agent.py
├── 02_Model_Based_Agent.py
├── 03_Goal_Based_Agent.py
└── 04_Utility_Based_Agent.py
```

## ⚙️ Installation and Setup

### Prerequisites

- Python 3 installed on your system.
- Visual Studio Code or another Python-compatible editor.
- Git, if you want to clone the repository.

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/AI-MODELS.git
```

Replace `YOUR-USERNAME` with your GitHub username.

### 2. Navigate to the Project Folder

```bash
cd AI-MODELS
```

### 3. Run the Agents

Run each program separately:

**Simple Reflex Agent**
```bash
python 01_Simple_Reflex_Agent.py
```

**Model-Based Reflex Agent**
```bash
python 02_Model_Based_Agent.py
```

**Goal-Based Agent**
```bash
python 03_Goal_Based_Agent.py
```

**Utility-Based Agent**
```bash
python 04_Utility_Based_Agent.py
```

On Windows, you can use `py` instead of `python` if required.

## 🧪 Example Use Cases

| Agent | Input | Expected Decision |
|---|---|---|
| Library Silence Monitor | Noise level: 75 dB | Display a silence warning |
| Museum Artifact Protection | Visitor distance: 35 cm | Issue a warning |
| Flood Escape Agent | Current location: Home | Search for a safe route to the Relief Camp |
| Wildlife Safari Guide | Route conditions and costs | Calculate utility and recommend a route |

*These examples illustrate the intended behavior; actual output depends on the program's input and configured rules.*

## 🎯 Learning Objectives

- Understand the architecture of different intelligent agents.
- Implement condition-action rules in Python.
- Explore internal state and memory in model-based agents.
- Apply graph search to goal-oriented problem solving.
- Understand utility functions and decision evaluation.
- Practice Python programming, input validation, and modular design.
- Connect fundamental AI concepts with practical scenarios.

## 🔮 Future Enhancements

- Develop a unified dashboard to access all four agents.
- Add graphical user interfaces for improved usability.
- Integrate real sensors for noise and distance monitoring.
- Add dynamic flood information and more advanced route planning.
- Compare multiple safari routes automatically.
- Improve input validation, logging, and automated testing.

## 👨‍💻 Author

**Dinesh Reddy**

AI and Machine Learning | Python | Intelligent Systems

## 📄 License

This project is intended for educational and learning purposes. A license can be added to specify the terms under which others may use, modify, and distribute the code.

---

⭐ If you find this project useful for learning Artificial Intelligence concepts, consider starring the repository.

**Built with Python to explore the fundamentals of intelligent agents and AI-based decision-making.**
