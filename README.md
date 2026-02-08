# Futoshiki CSP Solver – Constraint Satisfaction System

## Overview  
This project implements a complete Constraint Satisfaction Problem (CSP) solving framework to model and solve Futoshiki logic puzzles. The system combines classic constraint propagation techniques with intelligent variable ordering to efficiently solve structured combinatorial problems. The project was designed as a personal implementation of core AI reasoning algorithms with a focus on correctness, performance, and clean abstraction.

The solver supports multiple propagation strategies and CSP encodings, enabling direct comparison between binary and n-ary constraint modeling approaches.

---

## Core Components

### Constraint Propagation  
Forward Checking (FC)  
- Prunes variable domains when a constraint has exactly one unassigned variable  
- Detects dead-ends early to reduce search space  
- Tracks pruned values for correct backtracking  

Generalized Arc Consistency (GAC)  
- Enforces arc consistency across all constraints  
- Iteratively removes unsupported values from variable domains  
- Efficient queue-based propagation for scalability  

Variable Ordering Heuristic  
Minimum Remaining Values (MRV)  
- Selects the most constrained variable first  
- Reduces branching factor and improves search efficiency  

---

## Futoshiki CSP Models

### Model 1: Binary Constraint Model  
- Binary not-equal constraints for all row and column relationships  
- Binary inequality constraints for directional comparisons  
- Simple, explicit constraint representation  

### Model 2: N-ary Constraint Model  
- N-ary all-different constraints for rows and columns  
- Binary inequality constraints for puzzle relations  
- More compact modeling with higher constraint expressiveness  

Both models correctly enforce:  
- Unique values per row and column  
- Directional inequality constraints  
- Valid assignments within the puzzle domain  

---

## System Design Highlights  
- Modular CSP architecture using reusable Variable and Constraint objects  
- Clean separation between propagation logic and problem modeling  
- Efficient domain pruning with full backtracking support  
- Designed to pass both visible and hidden automated tests  

---

## Evaluation  
- Correctness validated through extensive automated testing  
- Performance compared across FC and GAC propagation strategies  
- Demonstrates tradeoffs between constraint granularity and runtime  

---

## Usage  
Clone the repository:
```
git clone <repo-url>
```

Run the solver using Python 3.12:
```
python3 autograder.py
```

You may modify the test script to add custom CSP or Futoshiki instances for experimentation.

---

## Goals  
- Build a fully functional CSP solver from first principles  
- Apply theoretical AI constraint propagation algorithms in practice  
- Compare binary vs. n-ary CSP modeling approaches  
- Strengthen algorithmic reasoning and search optimization skills  
- Demonstrate foundational AI problem-solving techniques  

---

## Author  
Victoria Piroian  

University of Toronto

Faculty of Applied Science & Engineering, 2025
