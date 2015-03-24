import matplotlib.pylab as plt

class population:
   
   def __init__(self, init_population):
      self.population  = init_population
      self.pop_history = [[init_population],[0]]
   
   def evolve(self, pop_inflow, pop_outflow, dt = 1.):
      pop_change = (pop_inflow - pop_outflow)*dt
      self.population += pop_change
      if self.population < 0:
         self.population = 0
      
      self.pop_history[0].append(self.population)
      self.pop_history[1].append(self.pop_history[1][-1] + dt)



rabits = population(100)
wolves = population(10)
alpha, beta, gamma, delta = 4, .05, 10, .01
dt = .001

for t in range (0,10000):
   rabits.evolve(alpha * rabits.population,  beta * rabits.population * wolves.population,dt)
   wolves.evolve(delta * wolves.population * rabits.population, gamma * wolves.population,dt)

plt.subplot(211)
plt.plot(rabits.pop_history[1],rabits.pop_history[0],color = 'blue')
plt.plot(wolves.pop_history[1],wolves.pop_history[0],color = 'red')
plt.xlabel('time')
plt.subplot(223)
plt.plot(rabits.pop_history[0],wolves.pop_history[0],'-')
plt.xlabel('Rabbit population')
plt.ylabel('Wolf population')
plt.show()
      