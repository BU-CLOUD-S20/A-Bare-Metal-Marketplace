## A-Bare-Metal-Marketplace Project Description

### Context: 
* Many hosts do not use cloud servers due to multiple constraints including security, privacy, or a need for specific hardware. Hosts often rent space in a data center for their servers.

### Bare-Metal Marketplace: 
* In order to allow for scalability or temporarily increased resources and the opposite- productive use of unnecessary resources, a marketplace to buy and sell time on bare-metal nodes where a renter can use nodes for any purpose. 

### Project Goal: 
* Implementing an auction system in order to facilitate the fair economics of the bare-metal marketplace system.

### Reach Goals:
* Adding a system for filtering based on resource 
* Autobuy systems for HPC and temporary scaling purposes based on various criteria including cost per resource
* An enhanced UI

** **

## 1.   Vision and Goals Of The Project:

The vision of this project is an OpenStack service for data centers to implement an auction system for already written Bare Metal Marketplace technology in order to facilitate the rapid and secure trade of computing resources among DC tenants without physical interference. This tool has applications primarily in industry and in research contexts.

* Bare Metal Marketplace (BMM) will be a microservice in OpenStack which functions as a service auction for bare metal nodes.

High-Level goals of BMM include:
* Providing a simple straightforward user experience for non-expert users.
* Providing a command line interface (CLI) for streamlined access and implementation
* Enabling a direct P2P marketplace hosted by data centers.



## 2. Users/Personas Of The Project:

BMM will be used by clients who sell resources, and clients who buy nodes on our marketplace. 

* Shared Data Center Managers: OpenStack users that are interested in hosting marketplace services to tenants that do not create security issues.

* Tenants with extra resources: Desire this application to reduce the cost of ownership for resources not always needed- may have different reasons or times/amounts etc. of resources to rent.
    * Type A- Wants to maximize money overall for a period of resource being rented
    * Type B- Wants to maximize money per amount of time that resource is being rented

* Tenants that desire extra resources:
    * Desire this application to quickly scale (industry)
    * Desire to run applications when cost-effective (HPC)

Note that it is important to keep in mind DC tenants have some rationale for choosing a DC over cloud solutions, including security or specific resource needs.

** **

## 3.   Scope and Features Of The Project:

The scope of this project is to design an auction system and related features- it is not to implement the core principles of the bare metal trading system. Included in this scope are UI elements related to the auction system, delivering information about nodes, selecting relevant resources based on cost, etc. Not included in this scope are cybersecurity aspects of bare metal access, delivery of the bare metal resource, etc.

* Hosting Tenants
    * Addition/Management of nodes
    * Authorization of who can sell
    * Flexible contested node policy
    * Multiple auction options
        * True auction
        * Buy now price set
    * Analytics portal
* Renting Tenants
    * Marketplace Filtering
    * Data management / Hard drive connection
* All Users
    * Messaging System
    * Profile Pages
    * Money Transfer / Credit System


** **

## 4. Solution Concept

Global Architectural Structure Of the Project:



`![alt text](https://github.com/BU-CLOUD-S20/A-Bare-Metal-Marketplace/images/InitialOverview.png "BMM Hierarchy")`


`![alt text](https://github.com/BU-CLOUD-S20/A-Bare-Metal-Marketplace/images/InitialBlowupView.png "BMM Internal Blowup")`

Overall, this project aims to be implemented in OpenStack with the use of Ironic for bare-metal provisioning.


### Design Implications and Discussion:

* Tenant & Renter UI
    * React/Bootstrap for reusable components and pre-written CSS
* MongoDB- JSON like, popular and versatile
* Credential System- Reusing credentials in OpenStack and Ironic
* Nodes- Requiring BareMetal Hypervisor to be rented
* OpenStack-The desired service to make use of Ironic
* Ironic Plugins-Any necessary plugins such as the python agent
* Paypal- An easy external system to implement for payment transfer

The microservice itself needs to be light to run as to not consume unnecessary resources.

## 5. Acceptance criteria

Minimum Criteria would be a simple auction system that could serve as the BMM. Stretch Goals Include:
* An autobuy system for renters
* Analytics pages
* Content Filtering

## 6.  Release Planning:
Week 3 goals:
* Basic UI

Week 5 goals:
* Start of Auction system

Week 7 goals:
* Finishing Auction System

Week 9 Goals:
* OpenStack Implementation

Week 11 Goals:
* Autobuy and Content Filtering

Week 13 Goals:
* Analytics


** **

## General comments

#TODO all

** **
