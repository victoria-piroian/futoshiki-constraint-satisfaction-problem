# Futoshiki CSP Solver – Constraint Propagation & Modeling

## Overview  
This project implements a full Constraint Satisfaction Problem (CSP) solution for the Futoshiki logic puzzle, built from the ground up using classic AI constraint propagation techniques. The system includes custom implementations of Forward Checking, Generalized Arc Consistency (GAC), and the Minimum Remaining Values (MRV) heuristic, along with two distinct CSP encodings of the puzzle.

The project emphasizes correctness, careful domain pruning, and clean interaction with a backtracking search engine, and was developed as a personal AI systems project.

---

## Constraint Propagation

### Forward Checking (FC)  
- Implemented in `propagators.py`  
- Checks constraints with exactly one unassigned variable  
- Prunes unsupported values from remaining domains  
- Detects dead-ends early and returns all pruned values for correct backtracking  

### Generalized Arc Consistency (GAC)  
- Queue-based GAC enforcement over constraints  
- Iteratively removes values without supporting tuples  
- Re-adds affected constraints when domains change  
- Terminates early if any domain becomes empty  

---

## Variable Ordering Heuristic

### Minimum Remaining Values (MRV)  
- Selects the unassigned variable with the smallest current domain  
- Breaks ties arbitrarily, as permitted by the CSP interface  
- Designed to reduce branching and improve search efficiency  

### Futoshiki CSP Models
Model 1: Binary Constraint Encoding  
- One variable per grid cell  
- Binary not-equal constraints for all row and column pairs  
- Binary inequality constraints (`<` and `>`) between adjacent cells  
- Constraint tuples generated explicitly for correctness  

Model 2: N-ary Constraint Encoding  
- One variable per grid cell  
- N-ary all-different constraints for each row and each column  
- Binary inequality constraints for directional relationships  
- Uses Cartesian product enumeration to construct satisfying tuples  

Both models correctly enforce:  
- Domain bounds {1, …, n}  
- Row and column uniqueness  
- All inequality constraints specified by the puzzle  
- Pre-filled board values  

Implementation Highlights  
- Uses the provided `Variable`, `Constraint`, and `CSP` abstractions without modification  
- Tracks all pruned (variable, value) pairs to support precise domain restoration  
- Avoids duplicate pruning and respects already-pruned values  
- Compatible with Python 3.12 and standard library imports only  

---

## Evaluation  
- Validated against visible and hidden automated tests  
- Demonstrates performance differences between FC and GAC propagation  
- Highlights modeling tradeoffs between binary and n-ary constraints  

---

## Usage

Clone the repository:
```
git clone <repo-url>
```

Run the provided test script:
```
python3 autograder.py
```

You may add custom CSP or Futoshiki instances to the testing script for experimentation.

---

## Goals  
- Implement core CSP algorithms from first principles  
- Apply constraint propagation to structured logic puzzles  
- Compare CSP modeling strategies and their computational impact  
- Strengthen algorithmic reasoning and backtracking search design  
- Demonstrate foundational AI problem-solving techniques  

---

## Author  
Victoria Piroian  

University of Toronto  

Faculty of Applied Science & Engineering, 2025
