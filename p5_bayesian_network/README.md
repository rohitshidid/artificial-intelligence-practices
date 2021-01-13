Bayesian Network
=================================
An example [Bayesian Network](https://en.wikipedia.org/wiki/Bayesian_network) in [Samiam](http://reasoning.cs.ucla.edu/samiam/).
## Table of content
* [Domain](#domain)
* [CPT values](#cpt_values)
* [Probabilites](#probabilities)
* [How to run](#how-to-run)
* [License](#license)

## Domain
The domain is a scenario of two friends meeting.

**Rainy:** Denotes if the weather is rainy or not. (rainy = true, not rainy = false)

**Raincoat:** Denotes whether Alex wears his raincoat. (wearing = true, not wearing = false)

**Rush_Hour:** Denotes if it is the rush hour when Alex departure to meet with Sasha. (rush hour = true, not rush hour = false)

**Accident:** Denotes whether there was an accident on the road when Alex departure to meet with Sasha. (accident = true, no accident = false)

**Traffic:** Denotes whether there was traffic when Alex departure to meet with Sasha. (traffic = true, no traffic = false)

**Shortcuts:** Denotes whether Alex used shortcuts while driving. (used shortcuts = true, not used shortcuts = false)

**Timing:** Denotes whether Alex arrived at the meeting on time. (on_time/late)

**Late_Before:** Denotes whether Alex has been late before to a previous meeting with Sasha. (yes = true, no = false)

**Friend_Angry:** Denotes whether Sasha is angry when they meet with Alex. (angry = true, not angry = false)


## CPT values
<p align="center">
<img width="871" alt="Screen Shot 2021-01-13 at 17 03 04" src="https://user-images.githubusercontent.com/37274614/104464121-a4fd9d00-55c3-11eb-9a0d-39683daaae13.png">
</p>

## Probabilities
<p align="center">
<img width="1042" alt="Screen Shot 2021-01-13 at 17 21 53" src="https://user-images.githubusercontent.com/37274614/104464515-12113280-55c4-11eb-9948-f0bc597e54d4.png">
</p>

## How to run
1) Install [Samiam Release](http://reasoning.cs.ucla.edu/samiam/index.php?s=)
2) Run the runsamiam in the samiam folder 
2) Open the [bayesian_network.net](./bayesian_network.net) on the Samiam. (File -> Open)
3) Fix the values of the parameters by selecting Mode -> Query Mode. Then left click on the node of the parameter.

## License
  
[MIT](../LICENSE)
