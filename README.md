# KU-S-S-EM
Network Protocol Reverse Engineering

## Introduction
Network Protocol Inference of aSTEAM Project (Next-Generation Information Computing Development Program through the National Research Foundation of Korea (NRF) funded by the Ministry of Science and ICT). 
This project aims to find out each protocol's syntax and semantics through reverse enginerring. For find out semantics and rules of each protocols, it makes finite state machine(FSM) for given packet datas. Before making FSM, specific keywords must be found to determine the state of protocol flow. Keywords are specified with well-proven algorithms such as Apriori. Through this, protocol syntax and semantics are specified. 

## Requirements and Dependencies
* OS : `Ubuntu 18.04.1 LTS`
* Language : `Python 3.5`, `Python 3.6`
* Library : `PIL`, `Pydot`

## Instructions
* Instructions for Use of `KU-S-S-EM`
  1. Open a terminal
  2. Install dependent libraries through `pip3`
  3. Install `Python 3.5`
  4. Run `main.py`

+(191105)

> Protocol State Visualization through `fsm/*`  
  1. install `python install setup.py` after `KU-S-S-EM`
  2. Run `python fsm/main.py` 


> Packet Capture Boost through Kernel Bypass
  * Kernel bypass environment used
  
  
  ![image](https://user-images.githubusercontent.com/6499345/68916778-d05fde80-07aa-11ea-9af0-b12d358ec00f.png)

> Process of inferencing of protocol state


  ![image](https://user-images.githubusercontent.com/6499345/68916807-f2f1f780-07aa-11ea-9627-fe8922a41793.png)
