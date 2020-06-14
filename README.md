Service for travel agency
Brief description of the system As part of the project, 
create the system, that allows you to search for tripsby given criteria and their purchase.

Main system functions
Main page
Configuring the trip offer (administrator)
Searching for trips by given criteria"Purchase" of the trip 
calculation of the final amount to pay according tothe number of people
(optional) Additional services: car rental,
optional trips
(optional) Configuration of passport and visa restrictions
Technologies
Django
(optional) Frontend in Angular and Django REST Framework Basic entities
(proposal)Continent name Countrynamebelonging to the continent (foreign key)City
name belonging to the country (foreign key)
Hotel name standard (stars) description belonging to the city 
(foreign key)Airport name belonging to the city 
(foreign key)Tripfrom where (City, Airport)to where (City, Hotel, Airport)d
ate of departuredate of return number of daystype: (BB  - bed & breakfast, HB – half board, FB – full board, AI – all inclusive )
price for an adult price for a child promoted number of places for adultsnumber of places for children Purchase of a triptrip
participant details amount Functionalities 
Main page- presentation of promoted trips- presentation of upcoming trips (globally)- presentation of upcoming trips (by continents)- 
presentation of upcoming trips (by country)- presentation of recently purchased trips- 
(optional) presentation of trips with a reduced price (mechanism should beadded)- 
(optional) presentation of trips with only 1 or 2 places left- each of the following lists should present, for example, 3 entries + link see moredirecting to search results according to a given criterion, 
e.g. by clicking theTenerife link should redirect us to the page with results of searching trips toTenerife- continent, country, city, hotel should be clickable and lead to search results- after clicking on a specific tour, detailed data are presented- 
(optional) below the trip we present trips to the same place, but with a later date- 
(optional) below the trip we present trips to other hotels from this city- 
(optional) under the trip we present trips to other cities from this countrySetting up a tour offer- the administrator (on a separate page) has the ability to add and edit tours- the form should make it possible to enter all the parameters of the trip- you must pre-configure the database of continents, countries, cities, airports andhotels
(optional) separate sites for managing continents, countries, cities, airports and hotels
Searching for trips by given criteria- all clickable elements (continents, countries, cities, hotels direct to search resultspage)- 
in addition, the page has a form for filtering and sorting results- 
You can search for trips by:city 
(airport) of departurecity 
(Hotel) of staydeparture date 
(optional range)return date 
(optional range)type (BB, HB, FB, AI)hotel standardnumber of days- you can sort by:price departure date- 
(optional) as the amount of data increases, you can enter paging search resultsPurchase of a trip- after choosing a specific trip, you can buy it- 
specify the number of adults and children- 
if there are enough places available, 
the trip will be "purchased"- the number of free places will be reduced- the price for the trip will be calculated (based on the number of people)- purchased trips are presented on the administrative page / pages- 
(optional), you can group these trips accordingly and add a simple search engine
Additional requirements- it is necessary to ensure an aesthetic and functional way of presenting data- data collected from users should be pre-validated
