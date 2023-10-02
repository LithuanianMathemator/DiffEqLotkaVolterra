# Numerical Project ODE: Modelling Populations using the Lotka-Volterra equations

## All exercises and further explanations about the project can be found in the .pdf file!

The goal of this project was to model populations of tomatoes and aphids using differential equations. In the end, ladybugs were added to see how they affect the numbers of the other two when eating the aphids.
The project was part of the course "Ordinary Differential Equations" at Stockholm University.

One of the first exercises was to plot different step sizes when only having aphids as a species. The provided .py file has the option of doing this with one, two or three species. To use this functionality, one can adjust the parameter `step`.

<p align="center">
  <img src="https://github.com/LithuanianMathemator/DiffEqLotkaVolterra/blob/main/Images/Timesteps.png" alt="drawing" width="600"/>
</p>

Below can be seen the modelling of aphids in combination with tomatoes. To switch between only aphids (`mode = 1`), aphids and tomatoes or aphids (`mode = 2`), tomatoes and ladybugs (`mode = 3`), use the parameter `mode`. 

<p align="center">
  <img src="https://github.com/LithuanianMathemator/DiffEqLotkaVolterra/blob/main/Images/WithTomatoes.png" alt="drawing" width="600"/>
</p>

In the end, ladybugs were added to control/diminish the aphid population.

<p align="center">
  <img src="https://github.com/LithuanianMathemator/DiffEqLotkaVolterra/blob/main/Images/WithLadybugs.png" alt="drawing" width="600"/>
</p>
