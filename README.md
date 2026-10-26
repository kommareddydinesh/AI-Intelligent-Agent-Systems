# AI Intelligent Agent Systems

### Four AI Agent Architectures. Four Real-World Problems. One Python Repository.

A collection of Python implementations exploring how intelligent agents perceive their environment, reason about conditions, plan actions, and make decisions. Each implementation demonstrates a fundamental AI agent architecture through a practical scenario.

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Artificial_Intelligence-Intelligent_Agents-7C3AED?style=for-the-badge" alt="Artificial Intelligence">
  <img src="https://img.shields.io/badge/Dependencies-Standard_Library-16A34A?style=for-the-badge" alt="Standard Library">
</p>

<p align="center">
  <a href="https://github.com/kommareddydinesh/AI-Intelligent-Agent-Systems">
    <strong>Explore the Repository</strong>
  </a>
  &nbsp; · &nbsp;
  <a href="#getting-started">Getting Started</a>
  &nbsp; · &nbsp;
  <a href="#the-four-agents">Explore the Agents</a>
</p>

---

## Overview

Intelligent agents are systems that select actions based on their perceptions, internal state, goals, or evaluation of possible outcomes.

This project demonstrates four foundational agent architectures through small, independently executable Python programs.

| Agent | Application | Decision-Making Approach |
|---|---|---|
| Simple Reflex | Library Silence Monitor | Condition-action rules |
| Model-Based Reflex | Museum Artifact Protection | Percepts and internal state |
| Goal-Based | Flood Escape | Goal-directed search using BFS |
| Utility-Based | Wildlife Safari Guide | Utility-based evaluation |

The goal is to understand the differences between these architectures through readable code and practical examples rather than treating AI as a purely theoretical subject.

## The Four Agents

### 01 — Smart Library Silence Monitor

**Architecture:** Simple Reflex Agent

A rule-based monitoring simulation that checks the current library noise level and determines whether a warning is required.

**How it works**

1. Receives a noise reading in decibels.
2. Compares the reading against a predefined threshold of 60 dB.
3. Displays a warning if the threshold is exceeded.
4. Reports whether the environment is noisy or quiet.

| Condition | Selected Action |
|---|---|
| Noise > 60 dB | Display a silence warning |
| Noise ≤ 60 dB | Report a quiet environment |

**Core concept:** The agent chooses an action from the current percept without maintaining internal state.

**Run**

```bash
python 01_Simple_reflex_agent.py
```

### 02 — Smart Museum Artifact Protection System

**Architecture:** Model-Based Reflex Agent

A museum security simulation that classifies visitor distance into security zones and uses internal state to select an appropriate response.

**How it works**

1. Receives the visitor's distance from an artifact.
2. Identifies the safe, caution, or restricted zone.
3. Checks the stored warning state.
4. Selects a warning, caution message, or simulated alarm.
5. Displays a security report.

| Distance | Security Zone | Response |
|---|---|---|
| Below 50 cm | Restricted | Warning or alarm, depending on memory |
| 50–99.99 cm | Caution | Display caution message |
| 100 cm or more | Safe | Continue monitoring |

**Core concept:** The agent combines current observations with internal state.

**Implementation note:** The current program accepts one reading per execution. Its memory resets at startup, so repeated violations across separate executions are not remembered.

**Run**

```bash
python 02_Model_based_agent.py
```

### 03 — Flood Escape Agent

**Architecture:** Goal-Based Agent

A flood evacuation simulation that searches a city map for a route to a relief camp while excluding roads marked as flooded.

**How it works**

1. Receives the citizen's current location.
2. Represents locations and connections as a graph.
3. Searches for a route using Breadth-First Search.
4. Rejects transitions through flooded roads.
5. Displays the route if the goal is reachable.

**Goal:** Reach the Relief Camp using an available route that avoids flooded roads.

**Algorithm:** Breadth-First Search (BFS)

BFS explores the graph level by level and finds a path with the fewest edges in an unweighted graph when a valid path exists.

**Run**

```bash
python 03_Goal_based_agent.py
```

### 04 — Wildlife Safari Guide Agent

**Architecture:** Utility-Based Agent

A safari route evaluation simulation that calculates a utility score from animal sighting opportunities, weather, road quality, crowd levels, and fuel cost.

**Evaluation factors**

- Animal sighting probability
- Weather conditions
- Road conditions
- Crowd levels
- Fuel cost

The current implementation uses a weighted utility formula:

```text
Utility =
    (Animal Sightings × 0.4)
  + (Weather Score × 0.2)
  + (Road Score × 0.2)
  - (Crowd Score × 0.1)
  - (Fuel Cost × 0.1)
```

The resulting score determines the recommendation:

| Utility Score | Recommendation |
|---|---|
| 70 or above | Excellent Route |
| 50 to below 70 | Good Route |
| Below 50 | Choose Another Route |

**Core concept:** Utility functions quantify preferences to support decisions.

**Run**

```bash
python 04_Utility_based_agent.py
```

> The current implementation evaluates one supplied route at a time. Automatic ranking requires extending it to accept and compare multiple routes.

---

## Architecture at a Glance

```text
                 ENVIRONMENT
                      |
                      v
                Current Percepts
                      |
          +-----------+-----------+
          |           |           |
          v           v           v
     Simple Reflex  Model-Based  Goal-Based
        Agent         Agent       Agent
          |           |           |
     Apply Rules   Use Memory   Search for Goal
          |           |           |
          +-----------+-----------+
                      |
               Utility-Based Agent
                      |
              Evaluate Utility Score
                      |
                      v
                 Select Action
                      |
                      v
                  Show Result
```

*Conceptual overview of the four independently implemented agents; this diagram does not represent a shared runtime pipeline.*

## Repository Structure

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

Each agent can be executed independently. No shared application server or external database is required.

## Getting Started

### Prerequisites

- Python 3
- Git (for cloning the repository)
- Visual Studio Code or another Python-compatible editor

### 1. Clone the repository

```bash
git clone https://github.com/kommareddydinesh/AI-Intelligent-Agent-Systems.git
```

### 2. Open the project directory

```bash
cd AI-Intelligent-Agent-Systems
```

### 3. Run an agent

Choose the program you want to explore:

```bash
python 01_Simple_reflex_agent.py
```

Replace the filename with any of the other three agent filenames to run a different implementation.

**Windows alternative:** If `python` is not recognized, try `py` instead.

### Dependencies

The current implementations use Python's standard library, including `collections.deque` and `datetime` where applicable. No third-party packages are required.

## Example Scenarios

| Scenario | Example Input | Expected Behavior |
|---|---|---|
| Library monitoring | `75` dB | Displays a silence warning |
| Museum protection | `35` cm | Issues a first restricted-zone warning |
| Flood evacuation | `Home` | Searches for a route to the Relief Camp |
| Safari recommendation | Route conditions and fuel cost | Calculates a utility score |

These examples illustrate the intended behavior. Actual results depend on the program's configured rules and inputs.

## Learning Objectives

- Understand the characteristics of different intelligent agent architectures.
- Implement condition-action rules and threshold-based decisions.
- Explore internal state and memory in model-based agents.
- Apply graph representations and BFS to goal-oriented search.
- Design utility functions for decision evaluation.
- Develop readable, modular Python programs.
- Relate foundational AI concepts to practical scenarios.

## Roadmap

Potential improvements for future versions:

- [ ] Integrate the four agents into a unified application.
- [ ] Add an interactive dashboard for selecting and running agents.
- [ ] Add automated tests for rules, edge cases, and invalid input.
- [ ] Persist museum security events across program executions.
- [ ] Add dynamic flood conditions and weighted route planning.
- [ ] Compare multiple safari routes and rank them by utility.
- [ ] Add example screenshots and demonstration videos.

## Technical Scope

This repository is an educational demonstration of agent architectures. Sensor readings are supplied as program inputs, flooded roads are predefined, and security alarms are simulated through console output. The project does not currently connect to physical sensors or operate real-world safety equipment.

## Author

**Dinesh Reddy**

Artificial Intelligence · Machine Learning · Python

GitHub: [@kommareddydinesh](https://github.com/kommareddydinesh)

## License

No license has been specified for this repository. Unless a license is added, others should not assume they have permission to redistribute or modify the project.

---

If you find this project useful for learning Artificial Intelligence, consider starring the repository.

**Built with Python to explore intelligent agents, search strategies, and decision-making.**
