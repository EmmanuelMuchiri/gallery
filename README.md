# gallery
A personal gallery application that you display your photos for others to see.
### Description
The application allows users to view images according to their categories and location. The admin is the one responsible for uploading, editing and deleting images. The users can search for images according to their categories.

##screenshots


### BDD Specifications Table
|        User Requirements                 |           Input                           |           Output                         |
|------------------------------------------|-------------------------------------------|------------------------------------------|
| View all images                          |  Go to the home page                      |    All images will be displayed          |
| Search for an image                      | Input the category name in the search bar | All images in that category will display |
| View the image details                   | Click on the image                        | All the image details will be displayed  |
| Copy image                               | Click on the copy link button             | The image link is copied                 | 

### Setup/Installation Requirements
<ul>
<li>Ensure you have Python3.6 installed</li>
<li>Clone the Pixels directory</li>
<li>Create your own virtual environment and activate it using these respective commands:python3.6 -m venv --without-pip virtual && source virtual/bin/activate</li>
<li>Install all the necessary dependencies necessarry for running the application using this command: pip install-r requirements.txt</li>
<li>Create a database: psql then create the databse using this command: CREATE DATABASE gallery</li>
<li>Run migrations using these respective commmands: python3.6 manage.py makemigrations images then: python3.6 manage.py migrate</li>
<li>Run the app using this command: python3.6 manage.py runserver on the terminal.You can then open the app on your browser</li>
</ul>

### Technologies Used
<ul>
<li>Python 3.6</li>
<li>Django</li>
<li>Bootstrap</li>
<li>HTML</li>
</ul>

### Support and Contact Details
Email : emmanuel.muchiri@outlook.com

### Licence 
Copyright(c) 2019  Emmanuel Muchiri