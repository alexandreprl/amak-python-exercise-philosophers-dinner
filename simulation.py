from amak import Scheduler

from system import PhilosophersDinnerMAS, Table
from amak import Scheduler

from system import PhilosophersDinnerMAS, Table

import matplotlib.pyplot as plt

if __name__ == "__main__":
    results = []

    environment = Table(5)
    mas = PhilosophersDinnerMAS(environment, results)


    Scheduler(mas, environment).start()

    # Extract unique keys (agent names)
    agents = list(results[0].keys())

    # Prepare data for plotting
    time_steps = range(len(results))
    agent_values = {agent: [entry[agent] for entry in results] for agent in agents}

    # Plot the lines
    plt.figure(figsize=(8, 5))
    for agent, values in agent_values.items():
        plt.plot(time_steps, values, label=agent, marker="o")

    plt.xlabel("Time Step")
    plt.ylabel("Ate pastas")
    plt.title("Ate pastas per philosopher over time")
    plt.legend()
    plt.grid(True)
    plt.show()

