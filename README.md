# Problem Statement: Impact of Vaccination on Disease Dynamics Using the SIR Model

## **Objective**
The goal is to analyze the impact of vaccination on the spread of an infectious disease within a population using the SIR (Susceptible-Infected-Recovered) model.

## **Key Questions**
1. **How does vaccination alter the dynamics of disease transmission?**
   - Investigate the changes in disease spread due to vaccination rates and coverage.

2. **What are the differences in the number of susceptible, infected, and recovered individuals over time with and without vaccination?**
   - Compare time-series data for the SIR model parameters with and without a vaccination program.

3. **Does vaccination help achieve herd immunity, and if so, how quickly?**
   - Evaluate the time required to reach herd immunity under different vaccination scenarios.

---

## **Solution Approach**

### **Model Parameters**
- **Population size:** \( N = 1000 \)
- **Basic reproduction number:** \( R_0 = 3 \)
- **Recovery rate:** \( \gamma = 1/5 \) (assumes an average recovery time of 5 days)
- **Infection rate:** \( \beta = R_0 \cdot \gamma \)
- **Vaccination rate:** 50%

### **Initial Conditions**
- **Without vaccination:** All but one individual are susceptible.
- **With vaccination:** 50% of the population is vaccinated, starting as "recovered."

### **Simulation**
- Iteratively calculate changes in the susceptible (\( S \)), infected (\( I \)), and recovered (\( R \)) populations over 98 days (14 weeks).
- Use the SIR model differential equations to simulate disease spread:
  - \( \frac{dS}{dt} = -\beta \cdot S \cdot I / N \)
  - \( \frac{dI}{dt} = \beta \cdot S \cdot I / N - \gamma \cdot I \)
  - \( \frac{dR}{dt} = \gamma \cdot I \)

### **Comparison**
- Track population dynamics with and without vaccination.
- Highlight differences in infection peaks and recovery rates between the two scenarios.

### **Visualization**
- Plot the time series of susceptible, infected, and recovered populations for both scenarios.
- Display the herd immunity threshold (\( N / R_0 \)) for reference.

---

## **Key Observations**

### **Without Vaccination**
- The disease spreads rapidly due to a fully susceptible population.
- The peak of infections is higher, and the epidemic lasts longer.

### **With Vaccination**
- A significant portion of the population is initially immune (vaccinated).
- The number of infected individuals remains much lower, and the epidemic resolves faster.

### **Herd Immunity Threshold**
- Vaccination reduces the susceptible population below the herd immunity threshold, mitigating disease spread.

---

## **Insights from the Plot**
- **Flattening the Curve:** Vaccination dramatically flattens the infection curve and reduces the epidemic's impact on the population.
- **Indirect Protection:** Recovered individuals (vaccinated) act as a protective barrier, indirectly safeguarding the susceptible population.
- **Herd Immunity Threshold:** The plot highlights the minimum population immunity required to halt disease spread.

This analysis underscores the importance of vaccination in managing epidemics and achieving herd immunity.
---
<br><br>
<img src = "https://github.com/Pedasoft-Consult/-Vaccination/blob/main/output/epidemic.png?raw=true">


## **Expected Outcomes**
- Quantitative insights into how vaccination impacts the progression of an infectious disease.
- Understanding the role of vaccination in achieving herd immunity and reducing the overall burden of the disease.











## References:
[Recommendation systems](https://towardsdatascience.com/introduction-to-recommender-systems-1-971bd274f421)<br>
[Recommender systems tutorial](https://www.kaggle.com/kanncaa1/recommendation-systems-tutorial)



### Feedback

If you have any feedback, please reach out at kepedahel@gmail.com


### 🚀 About Me
#### Hi, I'm Pedahel! 👋
I am an AI Enthusiast and  Data science & ML practitioner




[1]: https://github.com/Pedasoft-Consult/
[2]: https://www.linkedin.com/in/pedahel-emmanuel-mbc-6a7b8441/
[3]: https://public.tableau.com/app/profile/emmanuel.kojo.pedahel#!/




[![git](https://raw.githubusercontent.com/Pedasoft-Consult/-Vaccination/main/icons/icons/git.svg)][1]
[![linkedin](https://raw.githubusercontent.com/Pedasoft-Consult/-Vaccination/main/icons/iconmonstr-linkedin-5.svg)][2]
[![tableau](https://raw.githubusercontent.com/Pedasoft-Consult/-Vaccination/main/icons/icons8-tableau-software-1.svg)][3]



