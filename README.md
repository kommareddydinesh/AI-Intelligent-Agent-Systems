# 🤖 AI Intelligent Agent Systems

### Exploring Four Types of Intelligent Agents Through Real-World Applications

A Python-based Artificial Intelligence project demonstrating four fundamental intelligent agent architectures through practical scenarios involving library noise monitoring, museum artifact protection, flood evacuation, and wildlife safari route recommendation.

Each agent demonstrates a different approach to perceiving an environment, evaluating conditions, and selecting appropriate actions.

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![AI](https://img.shields.io/badge/Artificial%20Intelligence-Intelligent%20Agents-8A2BE2?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Educational%20Project-2E8B57?style=for-the-badge)
![License](https://img.shields.io/badge/License-Not%20Specified-lightgrey?style=for-the-badge)

---

## 📌 Overview

Intelligent agents are systems that perceive their environment and choose actions to achieve specific objectives. Different agent architectures use different mechanisms to make decisions.

This repository implements four fundamental AI agent types:

| No. | Agent Architecture | Project | Core Technique |
|---:|---|---|---|
| 01 | Simple Reflex Agent | Smart Library Silence Monitor | Condition-action rules |
| 02 | Model-Based Reflex Agent | Smart Museum Artifact Protection System | Internal state and memory |
| 03 | Goal-Based Agent | Flood Escape Agent | Breadth-First Search (BFS) |
| 04 | Utility-Based Agent | Wildlife Safari Guide Agent | Utility score calculation |

## 🚀 Implemented AI Agents

### 01. 🔇 Smart Library Silence Monitor

**Agent Type:** Simple Reflex Agent

A library monitoring simulation that evaluates the current noise level and determines whether a warning should be displayed.

**Key Features**
- Accepts a noise level in decibels (dB).
- Applies a predefined threshold of 60 dB.
- Displays a silence warning when the noise exceeds the threshold.
- Reports whether the environment is noisy or quiet.

**Decision Logic**

| Condition | Action |
|---|---|
| Noise level > 60 dB | Display a silence warning |
| Noise level ≤ 60 dB | Report a quiet environment |

**AI Principle:** Makes decisions using the current percept without maintaining internal state.

---

### 02. 🏛️ Smart Museum Artifact Protection System

**Agent Type:** Model-Based Reflex Agent

A museum security simulation that evaluates visitor distance from a protected artifact and uses internal state to determine an appropriate response.

**Key Features**
- Accepts visitor distance in centimeters.
- Defines safe, caution, and restricted zones.
- Stores warning status in internal memory.
- Simulates a security alarm for repeated violations when a previous warning is recorded.
- Displays a security report with the selected action and system status.

**Security Rules**

| Distance | Zone | Action |
|---|---|---|
| Below 50 cm | Restricted | Warning or alarm, depending on memory |
| 50 cm to below 100 cm | Caution | Display caution message |
| 100 cm or more | Safe | Continue monitoring |

**AI Principle:** Uses the current percept and internal state to make decisions.

> **Implementation note:** The current program accepts one distance reading per execution. Its memory resets when the program starts, so a repeated violation across separate executions is not detected.

---

### 03. 🌊 Flood Escape Agent

**Agent Type:** Goal-Based Agent

A flood evacuation simulation that searches for a route from the citizen's current location to a relief camp while avoiding flooded roads.

**Key Features**
- Represents the city as a graph of connected locations.
- Accepts the current location as input.
- Uses Breadth-First Search (BFS) to find a route.
- Avoids roads identified as flooded.
- Displays the planned route and reports whether the destination is reachable.

**Goal:** Reach the Relief Camp through a route that avoids flooded roads.

**Algorithm:** Breadth-First Search (BFS)

**AI Principle:** Selects a sequence of actions that achieves a predefined goal.

---

### 04. 🦁 Wildlife Safari Guide Agent

**Agent Type:** Utility-Based Agent

A safari route recommendation simulation that evaluates environmental and travel conditions to calculate a utility score.

**Key Features**
- Accepts a route name and animal sighting probability.
- Evaluates weather conditions.
- Considers road quality and crowd levels.
- Includes fuel cost in the utility calculation.
- Produces a utility score and recommendation.

**Decision Factors**
- Animal sighting chance
- Weather conditions
- Road conditions
- Crowd levels
- Fuel cost

**AI Principle:** Uses a utility function to evaluate conditions and classify a route according to its calculated score.

---

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python 3 | Core programming language |
| AI Agent Architectures | Decision-making models |
| Breadth-First Search | Route planning |
| Python Standard Library | Data structures and timestamps |
| Visual Studio Code | Development environment |
| Git and GitHub | Version control and project hosting |

**Dependencies:** The current implementations use Python's standard library and do not require additional third-party packages.

## 📂 Project Structure

```text
AI-Intelligent-Agent-Systems/
│
├── README.md
├── 01_Simple_reflex_agent.py
├── 02_Model_based_agent.py
├── 03_Goal_based_agent.py
└── 04_Utility_based_agent.py
```

*Ensure that the filenames in your repository match this structure. If your actual filenames differ, update the commands below accordingly.*

## ⚙️ Getting Started

### Prerequisites

- Python 3 installed
- Visual Studio Code or another Python editor
- Git (optional, for cloning the repository)

### 1. Clone the Repository

```bash
git clone https://github.com/kommareddydinesh/AI-Intelligent-Agent-Systems.git
```

### 2. Open the Project Folder

```bash
cd AI-Intelligent-Agent-Systems
```

### 3. Run an Agent

Execute each agent independently.

**Simple Reflex Agent**
```bash
python 01_Simple_reflex_agent.py
```

**Model-Based Reflex Agent**
```bash
python 02_Model_based_agent.py
```

**Goal-Based Agent**
```bash
python 03_Goal_based_agent.py
```

**Utility-Based Agent**
```bash
python 04_Utility_based_agent.py
```

**Windows tip:** If `python` is not recognized, try using `py` instead.

## 🧪 Example Scenarios

| Agent | Example Input | Expected Behavior |
|---|---|---|
| Library Silence Monitor | `75 dB` | Displays a silence warning |
| Museum Artifact Protection | `35 cm` | Issues the first restricted-zone warning |
| Flood Escape Agent | `Home` | Searches for a route to the Relief Camp |
| Wildlife Safari Guide | Route conditions and fuel cost | Calculates a utility score and recommendation |

*These are illustrative examples. Actual results depend on the configured rules, environment, and input values.*

## 🎯 Learning Outcomes

Through this project, you can explore:

- The architecture and behavior of intelligent agents.
- Condition-action rules and simple reflex behavior.
- Internal state and memory in model-based agents.
- Graph traversal and goal-oriented search.
- Utility functions and decision evaluation.
- Python programming and modular code organization.
- The relationship between fundamental AI concepts and real-world applications.

## 🔮 Future Enhancements

- [ ] Integrate all four agents into a unified application.
- [ ] Develop a graphical dashboard for monitoring and interaction.
- [ ] Connect real sensors for noise and visitor-distance monitoring.
- [ ] Introduce dynamic flood information and advanced route planning.
- [ ] Compare multiple safari routes and rank them by utility.
- [ ] Add automated tests and comprehensive input validation.
- [ ] Add screenshots and demonstration videos.

## 👨‍💻 Author

**Dinesh Reddy**

*Artificial Intelligence • Machine Learning • Python Development*

## 📄 License

No license has been specified for this repository yet. Add a `LICENSE` file if you intend to grant others permission to use, modify, and distribute the project.

---

⭐ **If this project helps you learn intelligent agent architectures, consider giving the repository a star!**

*Built with Python to explore fundamental AI agent models and decision-making strategies.*
