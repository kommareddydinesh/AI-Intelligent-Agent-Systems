# AI Intelligent Agent Systems

**Four intelligent agent architectures implemented in Python, demonstrated through four real-world problem scenarios.**

A hands-on Artificial Intelligence project exploring how agents make decisions using immediate perceptions, internal state, goal-directed search, and utility-based evaluation.

\<p align="center">
&#x20; \<a href="[https://github.com/kommareddydinesh/AI-Intelligent-Agent-Systems](https://github.com/kommareddydinesh/AI-Intelligent-Agent-Systems)">
&#x20;   \<img src="[https://img.shields.io/badge/Project-AI%20Agent%20Systems-161B22?style=flat-square](https://img.shields.io/badge/Project-AI%20Agent%20Systems-161B22?style=flat-square)" alt="AI Agent Systems">
&#x20; \</a>
&#x20; \<img src="[https://img.shields.io/badge/Language-Python-3776AB?style=flat-square&logo=python&logoColor=white](https://img.shields.io/badge/Language-Python-3776AB?style=flat-square\&logo=python\&logoColor=white)" alt="Python">
&#x20; \<img src="[https://img.shields.io/badge/Domain-Artificial%20Intelligence-7C3AED?style=flat-square](https://img.shields.io/badge/Domain-Artificial%20Intelligence-7C3AED?style=flat-square)" alt="Artificial Intelligence">
&#x20; \<img src="[https://img.shields.io/badge/Dependencies-Standard%20Library-238636?style=flat-square](https://img.shields.io/badge/Dependencies-Standard%20Library-238636?style=flat-square)" alt="Standard Library">
\</p>

\<p align="center">
&#x20; \<a href="#the-four-agents">Explore Agents\</a> ·
&#x20; \<a href="#getting-started">Get Started\</a> ·
&#x20; \<a href="#learning-outcomes">Learning Outcomes\</a>
\</p>

---

## Project Overview

Intelligent agents perceive their environment and select actions according to their design, available information, and objectives.

This repository demonstrates four foundational agent architectures through independently executable Python programs. Each implementation addresses a different problem and illustrates a distinct approach to decision-making.

| Agent Architecture | Application                | Primary Technique           |
| ------------------ | -------------------------- | --------------------------- |
| Simple Reflex      | Library Silence Monitor    | Condition–action rules      |
| Model-Based Reflex | Museum Artifact Protection | Internal state and memory   |
| Goal-Based         | Flood Escape               | Breadth-First Search        |
| Utility-Based      | Wildlife Safari Guide      | Weighted utility evaluation |

## The Four Agents

### 01 — Smart Library Silence Monitor

**Simple Reflex Agent**

A rule-based system that evaluates a library noise reading and determines whether a warning should be displayed.

**Decision logic**

- Noise above 60 dB → Display a silence warning.
- Noise at or below 60 dB → Report a quiet environment.
- Reject negative noise readings.

**Agent principle:** The action depends on the current percept, without requiring memory of previous readings.

**Run the program**

```bash
python 01_Simple_reflex_agent.py
```

### 02 — Smart Museum Artifact Protection System

**Model-Based Reflex Agent**

A museum security simulation that classifies visitor distance and uses internal state to select an appropriate response.

**Decision logic**

| Distance              | Zone       | Response                   |
| --------------------- | ---------- | -------------------------- |
| Below 50 cm           | Restricted | Warning or simulated alarm |
| 50 cm to below 100 cm | Caution    | Display caution message    |
| 100 cm or more        | Safe       | Continue monitoring        |

**Agent principle:** The decision uses the current percept and a stored warning state.

**Implementation detail:** The current program accepts one reading per execution. Because memory starts fresh each time, repeated violations across separate runs are not detected.

**Run the program**

```bash
python 02_Model_based_agent.py
```

### 03 — Flood Escape Agent

**Goal-Based Agent**

A route-planning simulation that searches a predefined city graph for a route from the citizen's current location to a relief camp while avoiding flooded roads.

**How it works**

1. Accept the starting location.
2. Represent locations as graph nodes and roads as edges.
3. Exclude roads identified as flooded.
4. Apply Breadth-First Search (BFS).
5. Display the route if the goal is reachable.

**Goal:** Reach the Relief Camp through a route that avoids flooded roads.

**Agent principle:** Select a sequence of actions that achieves a defined objective.

**Run the program**

```bash
python 03_Goal_based_agent.py
```

### 04 — Wildlife Safari Guide Agent

**Utility-Based Agent**

A route-evaluation simulation that calculates a utility score using animal sighting probability, weather, road quality, crowd levels, and fuel cost.

**Evaluation factors**

- Animal sighting chance
- Weather quality
- Road condition
- Crowd level
- Fuel cost

**Decision thresholds**

| Utility score  | Recommendation       |
| -------------- | -------------------- |
| 70 or above    | Excellent Route      |
| 50 to below 70 | Good Route           |
| Below 50       | Choose Another Route |

The implementation uses a weighted utility function that rewards favorable sighting, weather, and road scores while penalizing crowd levels and fuel cost.

**Agent principle:** Use a numerical utility measure to evaluate a situation and produce a recommendation.

**Run the program**

```bash
python 04_Utility_based_agent.py
```

---

## How the Project Is Organized

```text
AI-Intelligent-Agent-Systems/
│
├── README.md
│
├── 01_Simple_reflex_agent.py
├── 02_Model_based_agent.py
├── 03_Goal_based_agent.py
└── 04_Utility_based_agent.py
```

Each agent is a standalone Python program. The repository does not currently contain a shared dashboard or an integrated multi-agent runtime.

## Getting Started

### Requirements

- Python 3
- Git (optional, for cloning)
- Visual Studio Code or another Python-compatible editor

No third-party Python packages are required for the current implementations.

### 1. Clone the repository

```bash
git clone https://github.com/kommareddydinesh/AI-Intelligent-Agent-Systems.git
```

### 2. Enter the project directory

```bash
cd AI-Intelligent-Agent-Systems
```

### 3. Run an agent

For example, to launch the Library Silence Monitor:

```bash
python 01_Simple_reflex_agent.py
```

To run another agent, use its filename from the repository structure above.

**Windows tip:** If `python` is not recognized, try `py` instead.

## Example Scenarios

| Application                | Example input    | Expected result                       |
| -------------------------- | ---------------- | ------------------------------------- |
| Library Silence Monitor    | `75` dB          | Silence warning                       |
| Museum Artifact Protection | `35` cm          | First restricted-zone warning         |
| Flood Escape               | `Home`           | Search for a route to the Relief Camp |
| Wildlife Safari Guide      | Route conditions | Utility score and recommendation      |

These examples describe expected behavior for the configured rules and sample environment.

## Learning Outcomes

This project provides practical experience with:

- Condition–action rules and reactive behavior.
- Internal state and memory in intelligent agents.
- Graph modeling and goal-directed search.
- Breadth-First Search for unweighted pathfinding.
- Utility functions and weighted decision evaluation.
- Python input handling and modular program structure.
- Comparing different AI decision-making architectures.

## Future Improvements

- [ ] Integrate the four agents into a unified application.
- [ ] Develop a professional interactive web dashboard.
- [ ] Add automated tests and stronger input validation.
- [ ] Persist museum warning state across executions.
- [ ] Support dynamic flood conditions and alternative route costs.
- [ ] Compare multiple safari routes automatically.
- [ ] Add genuine screenshots and demonstration examples.

## Technical Scope

This is an educational simulation project. Inputs are entered manually, flood conditions are predefined, and security alarms are represented through console messages. The programs are not connected to physical sensors or real-world emergency systems.

## Author

**Dinesh Reddy**

Artificial Intelligence · Machine Learning · Python

[GitHub Profile](https://github.com/kommareddydinesh)

## License

No license has been specified. Add a `LICENSE` file if you intend to grant others explicit permission to use, modify, or redistribute this project.

---

If you find this repository useful for learning intelligent agent architectures, consider giving it a star.

**Built to explore the fundamentals of AI decision-making through practical Python implementations.**
