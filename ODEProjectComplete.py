import matplotlib.pyplot as plt
import math
import numpy as np

def main(var=[0.3,0.1,0.1,0.05,0.1,0.3,0.5],mode=2,step=[0.1],\
         T=60,num=[10,10,10]):
    '''
    mode: 1 to 3 for respective exercise
    var: growth and decline parameters (4 or 7 parameters needed),
    their use can be found in the function "euler"
    step: step sizes to be plotted
    T: end time
    num: initial population numbers
    '''

    # boilerplate
    if mode not in [1, 2, 3]:
        return None
    
    if len(var) not in [4, 7]:
        return None
    
    if len(step) == 0:
        return None
    
    if len(num) != 3:
        return None
    
    if len(var) == 4 and mode == 3:
        return None
        
    if mode == 1:

        x = np.linspace(0, T, 20*T)
        y = 10*np.exp(-0.1*x)

        plt.figure()
        plt.plot(x, y, label='Analytical solution')

        for i in range(len(step)):

            dt = step[i]
            
            # forward Euler for given time step
            returned_population_numbers = euler([0,0,var[2],0,0,0,0], dt, T, num)
            time_vector = returned_population_numbers[0]
            aphid_numbers = returned_population_numbers[1]

            plt.plot(time_vector, aphid_numbers, '-o', markersize = 0.01, \
                     label=f'Numerical solution: t = {dt}')
            
            # calculate the truncation error
            tr_err = max(aphid_numbers[1] - 10*np.exp(-0.1*dt), -aphid_numbers[1]\
                          + 10*np.exp(-0.1*dt))
            trunc = f'The numerically computed local truncation error \
for a time step of t = {dt} is given by {tr_err}.'
            print(trunc)

        # plot the data
        plt.xlabel('t: Time in days')
        plt.ylabel('y(t): Amount of aphids')
        plt.legend()
        plt.show()

    elif mode == 2:
        
        plt.figure()

        for i in range(len(step)):

            dt = step[i]
            
            # forward Euler for given time step
            returned_population_numbers = euler(var[0:4] + [0, 0, 0], dt, T, num)
            time_vector = returned_population_numbers[0]
            aphid_numbers = returned_population_numbers[1]
            tomato_numbers = returned_population_numbers[2]

            # calculating the success rate of the tomatoes
            S = np.trapz(tomato_numbers, time_vector)
            s_rate = f'The success rate of the tomatoes under the given \
circumstances and with a time step of t = {dt} is S = {S}.'
            print(s_rate)

            plt.plot(time_vector, tomato_numbers, '-o', markersize = 0.01, \
                     label=f'Population of tomatoes: t = {dt}')
            plt.plot(time_vector, aphid_numbers, '-o', markersize = 0.01, \
                     label=f'Population of aphids: t = {dt}')
            
        # plot the data
        plt.xlabel('Time in days')
        plt.ylabel('Population of species')
        plt.legend()
        plt.show()

    else:
        
        plt.figure()

        for i in range(len(step)):

            dt = step[i]
            
            # forward Euler for given time step
            returned_population_numbers = euler(var, dt, T, num)
            time_vector = returned_population_numbers[0]
            aphid_numbers = returned_population_numbers[1]
            tomato_numbers = returned_population_numbers[2]
            ladybug_numbers = returned_population_numbers[3]

            # calculating the success rate of the tomatoes
            S = np.trapz(tomato_numbers, time_vector)
            s_rate = f'The success rate of the tomatoes under the given \
circumstances and with a time step of t = {dt} is S = {S}.'
            print(s_rate)

            plt.plot(time_vector, tomato_numbers, '-o', markersize = 0.01, \
                     label=f'Population of tomatoes: t = {dt}')
            plt.plot(time_vector, aphid_numbers, '-o', markersize = 0.01, \
                     label=f'Population of aphids: t = {dt}')
            plt.plot(time_vector, ladybug_numbers, '-o', markersize = 0.01, \
                     label=f'Population of ladybugs: t = {dt}')
            
        # plot the data
        plt.xlabel('Time in days')
        plt.ylabel('Population of species')
        plt.legend()
        plt.show()

def euler(var,dt,T,num):

    # initial time and end time
    t = 0
    T = 60

    # assigning initial population numbers
    x_0 = num[0]
    y_0 = num[1]
    z_0 = num[2]

    # lists for plotting
    tomato_numbers = []
    tomato_numbers.append(x_0)
    aphid_numbers = []
    aphid_numbers.append(y_0)
    ladybug_numbers = []
    ladybug_numbers.append(z_0)
    time_vector = []
    time_vector.append(t)

    # constants, use of population growth and decline parameters
    tomato_growth = var[0]
    tomato_decline = var[1]
    aphid_decline = var[2]
    aphid_growth = var[3]
    ladybug_growth = var[4]
    aphid_being_eaten = var[5]
    ladybug_decline = var[6]

    # forward Euler for given time step
    while t < T:
        
        x_t = x_0
        y_t = y_0
        z_t = z_0
        x_0 = x_t + dt*(tomato_growth*x_t - tomato_decline*x_t*y_t)
        y_0 = y_t + dt*(aphid_growth*x_t*y_t - aphid_decline*y_t - aphid_being_eaten*y_t*z_t)
        z_0 = z_t + dt*(ladybug_growth*z_t*y_t - ladybug_decline*z_t)
        tomato_numbers.append(x_0)
        aphid_numbers.append(y_0)
        ladybug_numbers.append(z_0)
        t = t + dt
        time_vector.append(t)

    return (time_vector, aphid_numbers, tomato_numbers, ladybug_numbers)
