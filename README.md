# rideshare-matchmaker

Service to find and notify potential carpool partners among travelers to a given place

Event organizers should submit their attendees' contact info
and zip/postal codes to the service, along with the zip/postal
code of the event.  rideshare-matchmaker will determine which
attendees live close to each other (relative to the destination)
and contact them, suggesting that they arrange to share rides.

Should also be useful for employers to suggest carpools to their
employees.

Vaporware so far.  PLEASE help brainstorm on the 
challenges listed in the [issue tracker](https://github.com/catherinedevlin/rideshare-matchmaker/issues).  Better yet, steal the
idea and implement it.  Planet earth needs you.

Implement with PostGIS and pgRouting.  Run as a web app
and webservice with API.  Also let event organizers run
on their own hardware, but only tech-savvy organizers will
be able to do that, so webservice is key.

