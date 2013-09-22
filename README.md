tsec
====

Transparent, secure encryption layer with a distributed trust model

Seeing as most implementations have been screwed over by the National Security Industry. 
With both servers and clients not using the latest security protocols, and bieng the CA model
the de-facto trust model (with all its issues), this is try at a PoC of creating and easy to implement,
transparent comunication layer that will do the following:

* Provide the same interface as a normal OS socket to the client app
* Validate the identity endpoint using other trusted endpoints (similar to Convergence.io aproach to trust valdiation)
* Establish an encrypted comunication between both endpoints using the best crypto available


The idea is to provide any newly written application with the ability to forget about the complexity
of secure communications management, while at the same time making that comunication as secure as possible.
