# Numeric ODE Game

A numerical methods game where players solve Ordinary Differential Equations (ODEs) while managing computational resources and accuracy requirements.

## How to Play

1. You start with $1000 virtual money
2. For each round:
   - You'll be presented with a differential equation to solve
   - You need to choose the method and parameters (currently only Euler method and only the step length h)
   - The system will compute the solution and calculate:
     * Computational cost (based on time and step size)
     * Solution accuracy
   - If you achieve the target accuracy, you'll receive a reward but pay the computational cost
   - If not, you get no reward but still pay the computational cost

TODO
- [ ] More methods to choose from
- [ ] Randomly generated equations
- [ ] Visualize the result
- [ ] Implement the computation in Rust
