import numpy as np
from scipy.integrate import solve_ivp
import time

class ODEGame:
    def __init__(self, problems, initial_money=1000):
        self.money = initial_money
        self.current_round = 0
        self.problems = problems

    def euler_method(self, f, t_span, y0, h):
        t = np.arange(t_span[0], t_span[1] + h, h)
        y = np.zeros(len(t))
        y[0] = y0
        
        start_time = time.time()
        for i in range(1, len(t)):
            y[i] = y[i-1] + h * f(t[i-1], y[i-1])
        computation_time = time.time() - start_time
        
        return t, y, computation_time

    def calculate_cost(self, computation_time, h):
        # Cost increases with computation time and smaller step sizes
        # return int(computation_time * 1000 + 10/h)
        return int(1/h)

    def calculate_error(self, numerical_solution, true_solution, t):
        true_values = true_solution(t)
        max_error = np.max(np.abs(numerical_solution - true_values))
        return max_error

    def play_round(self):
        if self.current_round >= len(self.problems):
            print("Game Over! You've completed all problems.")
            return False

        problem = self.problems[self.current_round]
        print(f"\nRound {self.current_round + 1}")
        print(f"Current money: ${self.money}")
        print("Solve the differential equation:")
        print(problem['display'])
        print(f"Initial condition: y({problem['t_span'][0]}) = {problem['y0']}")
        print(f"Time interval: {problem['t_span']}")
        print(f"Target accuracy: {problem['target_accuracy']}")

        # Get user input
        while True:
            try:
                h = float(input("Choose step size h: "))
                if h > 0:
                    break
                print("Step size must be positive.")
            except ValueError:
                print("Please enter a valid number.")

        # Solve using Euler method
        t, y, computation_time = self.euler_method(
            problem['equation'],
            problem['t_span'],
            problem['y0'],
            h
        )

        # Calculate cost and error
        cost = self.calculate_cost(computation_time, h)
        error = self.calculate_error(y, problem['true_solution'], t)

        # Check if user can afford the computation
        if cost > self.money:
            print("You don't have enough money for this computation!")
            return False

        self.money -= cost
        print(f"\nComputation cost: ${cost}")
        print(f"Maximum error: {error}")

        # Check if accuracy target is met
        if error <= problem['target_accuracy']:
            reward = problem['base_reward']
            self.money += reward
            print(f"Target accuracy achieved! Reward: ${reward}")
        else:
            print("Target accuracy not achieved. No reward.")

        self.current_round += 1
        return True

    def start_game(self):
        print("Welcome to the ODE Solver Game!")
        print("Solve differential equations using numerical methods.")
        print("Choose your parameters wisely to maximize profits!")

        while self.money > 0:
            if not self.play_round():
                break
            
            # if input("\nContinue to next round? (y/n): ").lower() != 'y':
                # break

        print(f"\nGame Over! Final money: ${self.money}")



problems = [
    {
        'equation': lambda t, y: y,  # dy/dt = y
        'true_solution': lambda t: np.exp(t),  # y = e^t
        't_span': (0, 1),
        'y0': 1.0,
        'target_accuracy': 1e-1,
        'base_reward': 100,
        'display': 'dy/dt = y'
    },
    {
        'equation': lambda t, y: -2*t*y,  # dy/dt = -2ty
        'true_solution': lambda t: np.exp(-t**2),  # y = e^(-t^2)
        't_span': (0, 2),
        'y0': 1.0,
        'target_accuracy': 1e-1,
        'base_reward': 150,
        'display': 'dy/dt = -2ty'
    },
]


# Run the game
game = ODEGame(problems, initial_money=1000)
game.start_game()