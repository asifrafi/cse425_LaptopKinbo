
# Laptop Kinbo
"Laptop Kinbo" is a web app that aims to provide accurate and up-to-date information on laptop prices and features in Bangladesh. With a focus on helping users make informed decisions about their purchases, the app will scrape data from major retailers like StarTech, Ryans, and Techland, and store it in a MongoDB database. Using Express and Node.js, the app will process this data to suggest laptops based on users' budgets and use cases. Additionally, "Laptop Kinbo" will expose its backend as an API, making it a valuable resource for other websites looking to provide laptop recommendations in Bangladesh. The app will have a simple, user-friendly interface and will not collect any user data. By providing accurate and timely information, "Laptop Kinbo" aims to help users avoid dishonest shop owners and make confident purchases.
### API
* api_list - This API endpoint supports GET and POST methods.
  GET: It retrieves a list of all laptops available in the Bangladeshi market. It uses the LaptopSerializer to serialize the data and returns a response containing the serialized data of all laptops.
  POST: This method is not implemented in the provided code snippet. You can customize it to handle the creation of new laptop entries.

* api_game - This API endpoint supports GET method with two parameters l and h.
  GET: It retrieves a list of gaming laptops within the specified price range. The API filters laptops based on their price using price__gt (greater than) and price__lt (less than) filters. It further filters the laptops by checking if their name contains "RTX" or "GTX" (case-insensitive) to identify gaming laptops. The filtered laptops are serialized using LaptopSerializer and returned as a response.

* laptops_list - This API endpoint supports GET and POST methods with two parameters l and h.
  GET: It retrieves a list of laptops within the specified price range. Similar to api_game, it filters laptops based on their price using price__gt and price__lt filters. The filtered laptops are serialized using LaptopSerializer and returned as a response.
  POST: This method is not implemented in the provided code snippet. You can customize it to handle the creation of new laptop entries within the specified price range.

* mac_list - This API endpoint supports GET method with two parameters l and h.
  GET: It retrieves a list of MacBook laptops within the specified price range. The API filters laptops based on their price using price__gt and price__lt filters and further filters them by checking if their name contains "MacBook" (case-insensitive). The filtered laptops are serialized using LaptopSerializer and returned as a response.

* api_detail - This API endpoint supports GET, PUT, and DELETE methods with a parameter pk.
 GET: It retrieves the details of a specific laptop identified by the pk (primary key). The laptop object is serialized using LaptopSerializer and returned as a response.
 PUT: It updates the details of a specific laptop identified by the pk. The updated data is provided in the request body, and the API saves the changes if the data is valid. The updated laptop object is serialized using LaptopSerializer and returned as a response.
 DELETE: It deletes a specific laptop identified by the pk. The API deletes the laptop object and returns a response with status HTTP 204 No Content.

## Please Read This MarkDown File before running Laptop Kinbo
#### Tech Stack
* Frontend: React (Next.js)
* Backend: Express.js, Node.js
* Database: MongoDB 
* Script: Python,PyMongo,BeautifulSoup4
#### Tech Stack V2
* Frontend: React (Next.js)
* Backend: django,djangorestframework
* Database: MongoDB 
* Script: Python,PyMongo,BeautifulSoup4

#### Operating Environments
<p style="text-align: left;font-family:arial;">
<ul type="disc"> 
  <li><strong>Platform:</strong> Web </li>
  <li><strong>Web Server:</strong> Any OS with NodeJS and NPM and python 3.10 installed***</li>
  <li><strong>Client System:</strong> Any system with a modern web browser and for android with android version 5.0+</li>
  <li><strong>Database Configuration:</strong> MongoDB . We have included all the secrets in config.ENV file so it will automatically connect with our atlas database cluster.</li>
</ul>
</p>

[Install Node JS](https://nodejs.org/en/)

[Install NPM](https://www.npmjs.com/)



#### Contributor
Simanta Mostafa <br>
Asif Haider Rafi <br>

#### Academic Disclosure 
Note: This Is a University Project from North South University <br>
Course: CSE425 <br> 
Department: ECE Department <br>
Faculty Member: MMK1 <br>
Semester: Spring 2023 <br> 
Licensing: MIT Licensing
#### Contact 
If you have any questions or feedback about Laptop Kinbo, please contact us at <br>
Asif Haider Rafi <br>
Education Email: asif.rafi1@northsouth.edu <br>
Personal Email: asifhaiderrafi@protonmail.com

### This is still a work in progress project. Will finalize it before June,2023

