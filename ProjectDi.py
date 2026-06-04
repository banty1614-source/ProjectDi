import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
np.random.seed(42)
#Initial Health Indicators of Country A
health_indi=np.array([
      'population',
      'gdp',
      'inflation',
      'happiness',
      'food',
      'energy' 
])


#Corresponding value of health indicator
health_indi_value=np.array([
        1450000000,        # ~1.45 Billion
        4000000000000,     # ~4 Trillion USD nominal
        4.5,               # ~4.5% 
        40,                # Scaled to your 0-100 system
        330000000,         # ~330 Million tonnes (annual grain production)
        1900000           # ~1.9 Million GWh (annual electricity generation)
])


#Initializing the given below indicator
population = 1450000000
gdp=4000000000000
happiness=40
inflation=4.5


#Creating empty lists
years = []
populations = []
gdps = []
inflations = []
happiness_scores = []
events_occurred = []


#Now calculating various stuff for next 20 years
for year in range(1,21):
    #Population growth around (0.2%-0.6%)
    population_growth=np.random.uniform(0.2,0.6)
    population *=(1+population_growth/100)

    #GDP growth around (6%-8%)
    gdp_growth=np.random.uniform(4,9)
    gdp *=(1+gdp_growth/100)

    #Inflation around (3.5%-5.5%)
    inflation +=np.random.uniform(-1,1)
    #Keeping value for higher inflation=10 and lower inflation=2
    inflation=np.clip(inflation,2,10) #Here this function ensure worst and best case for inflation

    #Impact on happiness(affected by inflation and gdp)
    #1.Impact of inflation on happiness
    if inflation>=6:
        happiness -=4
    elif 3.5<inflation<6:
        happiness +=1
    elif 2<=inflation<=3.5:
        happiness +=2

    #Impact of gdp on happiness
    if gdp_growth>7.5:
        happiness +=2
    elif gdp_growth <5.5:
        happiness -=2
    happiness=np.clip(happiness,0,100) #Here this function ensure happiness lies between 0 and 100

    #We have ignored impact of food by assuming that food will be easily available for whole population

    #Creating major events list 
    events=[
        'Economic Boom',
        'Recession',
        'Drought',
        'Breakthrough',
        'Pandemic',
        'Nothing'
    ]
    event = np.random.choice(events)
    if event =='Economic Boom' :
        gdp *=1.08
        happiness +=5
    elif event == 'Recession':
        gdp *=0.98
        happiness -=5
    elif event =='Pandemic':
        population *=0.995
        gdp *=0.95
        happiness -=7
    elif event == 'Breakthrough':
        gdp *=1.09
        happiness +=5  

    #Storing the data in their respective domain
    years.append(year)
    populations.append(population)
    gdps.append(gdp)
    inflations.append(inflation)
    happiness_scores.append(happiness)
    events_occurred.append(event) 


#Creating DataFrame using pandas
df = pd.DataFrame({
    "Year": years,
    "Population": populations,
    "GDP": gdps,
    "Inflation": inflations,
    "Happiness": happiness_scores,
    "Event": events_occurred
}) 


#Visualization
#1. Population
plt.figure(figsize=(8, 4))
plt.plot(df["Year"], df["Population"] / 1e9, color="blue", marker="o", label="Population")
plt.title("India Population Growth Over 20 Years")
plt.xlabel("Year")
plt.ylabel("Population (in Billions)")
plt.grid(True)
plt.show()

#2. GDP 
plt.figure(figsize=(8, 4))
plt.plot(df["Year"], df["GDP"] / 1e12, color="green", marker="s", label="GDP")
plt.title("India GDP Trajectory Over 20 Years")
plt.xlabel("Year")
plt.ylabel("GDP (in Trillions USD)")
plt.grid(True)
plt.show()

#3. Happiness
plt.figure(figsize=(8, 4))
plt.plot(df["Year"], df["Happiness"], color="gold", marker="^", linewidth=2)
plt.title("Civilization Happiness Index")
plt.xlabel("Year")
plt.ylabel("Happiness Score (0-100)")
plt.ylim(0, 100) 
plt.grid(True)
plt.show()

#Statistical summary
print(df.describe())
