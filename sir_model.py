import matplotlib.pyplot as plt

# Parameters
total_days = 14 * 7  # 14 weeks = 98 days
N = 1000  # Total population
R0 = 3  # Basic reproduction number
gamma = 1 / 5  # Recovery rate (5 days to recover)
beta = gamma * R0  # Infection rate
vaccination_rate = 0.5  # 50% of the population is vaccinated

# Initial conditions
S_no_vaccine = N - 1  # Susceptible without vaccination
I_no_vaccine = 1  # Infected without vaccination
R_no_vaccine = 0  # Recovered without vaccination

S_with_vaccine = (1 - vaccination_rate) * N - 1  # Susceptible with vaccination
I_with_vaccine = 1  # Infected with vaccination
R_with_vaccine = vaccination_rate * N  # Recovered with vaccination

# Track results
S_no_vac, I_no_vac, R_no_vac = [S_no_vaccine], [I_no_vaccine], [R_no_vaccine]
S_with_vac, I_with_vac, R_with_vac = [S_with_vaccine], [I_with_vaccine], [R_with_vaccine]

# Simulation
for day in range(total_days):
    # No vaccination
    new_infections_no_vac = beta * S_no_vaccine * I_no_vaccine / N
    new_recoveries_no_vac = gamma * I_no_vaccine
    S_no_vaccine = max(S_no_vaccine - new_infections_no_vac, 0)
    I_no_vaccine = max(I_no_vaccine + new_infections_no_vac - new_recoveries_no_vac, 0)
    R_no_vaccine = min(R_no_vaccine + new_recoveries_no_vac, N)
    S_no_vac.append(S_no_vaccine)
    I_no_vac.append(I_no_vaccine)
    R_no_vac.append(R_no_vaccine)

    # With vaccination
    new_infections_with_vac = beta * S_with_vaccine * I_with_vaccine / N
    new_recoveries_with_vac = gamma * I_with_vaccine
    S_with_vaccine = max(S_with_vaccine - new_infections_with_vac, 0)
    I_with_vaccine = max(I_with_vaccine + new_infections_with_vac - new_recoveries_with_vac, 0)
    R_with_vaccine = min(R_with_vaccine + new_recoveries_with_vac, N)
    S_with_vac.append(S_with_vaccine)
    I_with_vac.append(I_with_vaccine)
    R_with_vac.append(R_with_vaccine)

# Plot results
plt.figure(figsize=(12, 8))

# Without vaccination
plt.plot(S_no_vac, label="Susceptible (No Vaccine)", linestyle="--")
plt.plot(I_no_vac, label="Infected (No Vaccine)", linestyle="--")
plt.plot(R_no_vac, label="Recovered (No Vaccine)", linestyle="--")

# With vaccination
plt.plot(S_with_vac, label="Susceptible (With Vaccine)")
plt.plot(I_with_vac, label="Infected (With Vaccine)")
plt.plot(R_with_vac, label="Recovered (With Vaccine)")

# Herd immunity threshold
herd_immunity_threshold = N / R0
plt.axhline(herd_immunity_threshold, color="red", linestyle="--", label="Herd Immunity Threshold")

# Add labels and legend
plt.title("Impact of Vaccination on Epidemic Dynamics")
plt.xlabel("Days")
plt.ylabel("Population")
plt.legend()
plt.grid(True)
plt.show()
