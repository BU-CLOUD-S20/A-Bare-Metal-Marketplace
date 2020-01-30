## A-Bare-Metal-Marketplace Project Description

### Context: 
- Many hosts do not use cloud servers due to multiple constraints including security, privacy, or a need for specific hardware. Hosts often rent space in a data center for their servers.

### Bare-Metal Marketplace: 
- In order to allow for scalability or temporarily increased resources and the opposite- productive use of unnecessary resources, a marketplace to buy and sell time on bare-metal nodes where a renter can use nodes for any purpose. 

### Project Goal: 
- Implementing an auction system in order to facilitate the fair economics of the bare-metal marketplace system.

### Reach Goals:
- Adding a system for filtering based on resource 
- Autobuy systems for HPC and temporary scaling purposes based on various criteria including cost per resource
- An enhanced UI

** **

## 1.   Vision and Goals Of The Project:

The vision of this project is an OpenStack service for data centers to implement an auction system for already written Bare Metal Marketplace technology in order to facilitate the rapid and secure trade of computing resources among DC tenants without physical interference. This tool has applications primarially in industry and in research contexts.

## 2. Users/Personas Of The Project:

- Data Center Managers: OpenStack users that are interested in hosting marketplace services to tenants that do not create security issues.

- Tenants with extra resources: Desire this application to reduce the cost of ownership for resources not always needed- may have different reasons or times/amounts etc. of resource to rent.

- Tenants that desire extra resources: Desire this application to quickly scale (industry), or run applications when cost-effective (HPC).

Note that it is important to keep in mind DC tenants have some rationale for choosing a DC over cloud solutions, including security or specific resource needs.

** **

## 3.   Scope and Features Of The Project:

The scope of this project is to design an auction system and related features- it is not to implement the core principles of the bare metal trading system. Included in this scope are UI elements related to the auction system, delivering information about nodes, selecting relevant resources based on cost, etc. Not included in this scope are cybersecurity aspects of bare metal access, delivery of the bare metal resource, etc. 

** **

## 4. Solution Concept

Global Architectural Structure Of the Project:

Overall, this project aims to be implemented in OpenStack with the use of Ironic for bare-metal provisioning.


Design Implications and Discussion:

The microservice itself neets to be light to run as to not consume unnecessary resources.

## 5. Acceptance criteria

TBD after discussion with mentors

## 6.  Release Planning:

TBD after discussion with mentors
1st sprint: knowledge spike

** **

## General comments

#TODO all

** **
