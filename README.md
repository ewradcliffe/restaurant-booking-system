The objective of this project was to create a reservation system for the Blue Boar Inn, a fictional restaurant. At it's core, the project needed a user to have full CRUD (Create, Read, Update, Delete)control over data in a database, i.e. be able to make, edit, delete a reservation as well as view their database.

### Strategy
The overall approach was to build a full stack application using the Django framework linked to a PostgreSQL database. PostgresSQL is a popular and adaptable relational database management system and Django is a flexible framework which easily integrates API's, allowing for a streamlined development cycle. Both are open source and well supported allowing for easy maintainance, future development and customisation. Bootstrap 5 was to be used at the front end to speed up the design process.

The site was disigned using an Agile approach: User stories were collected, added to a [kanban board](https://github.com/users/ewradcliffe/projects/5/views/1) in the project [Githib repository](https://github.com/ewradcliffe/restaurant-booking-system) and prioritised according to the MOSCOW system. These were then used to decide on the scope of the initial iteration of the project.


### Scope

##### Must have
Must have features are features without which the project will not work.
- [Staff can make reservations on behalf of customers](https://github.com/users/ewradcliffe/projects/5/views/1?pane=issue&itemId=73488282)
- [Staff can edit reservations on behalf of customers](https://github.com/users/ewradcliffe/projects/5/views/1?pane=issue&itemId=74915945)
- [Staff can delete reservations on behalf of customers](https://github.com/users/ewradcliffe/projects/5/views/1?pane=issue&itemId=74916026)
- [Staff should have accounts with enhanced access so they have CRUD access to reservation, user and menu duatabases. These accounts should be password protected for reasons of data security and to prevent malicious use.](https://github.com/users/ewradcliffe/projects/5/views/1?pane=issue&itemId=73488956)
- [Customers should be able to create an account so their data is protected with a password](https://github.com/users/ewradcliffe/projects/5/views/1?pane=issue&itemId=73488956)
- [Customers can make reservations online.](https://github.com/users/ewradcliffe/projects/5/views/1?pane=issue&itemId=73488791)
- [Customers can edit reservations online.](https://github.com/users/ewradcliffe/projects/5/views/1?pane=issue&itemId=74915566)
- [Customers can delete reservations online.](https://github.com/users/ewradcliffe/projects/5/views/1?pane=issue&itemId=74915437)
- [Automated tests should be created to ensure users have full CRUD control over reservations once logged in.](https://github.com/users/ewradcliffe/projects/5/views/1?pane=issue&itemId=74916186)
- [Automated tests should be created to ensure the reservation database works correctly.](https://github.com/users/ewradcliffe/projects/5/views/1?pane=issue&itemId=78005401)
- [Automated tests should be created to ensure the menu database works correctly.](https://github.com/users/ewradcliffe/projects/5/views/1?pane=issue&itemId=78005720)

- []()
##### Should have
Features not essential to the functioning of the project, but will add significant value to the project.
- [The site should tell users if they are logged in. The message advising them they are not should link to the log in page.](https://github.com/users/ewradcliffe/projects/5/views/1?pane=issue&itemId=77004143)
- [The site should be able to display the restaurant menu.](https://github.com/users/ewradcliffe/projects/5/views/1?pane=issue&itemId=73489183)
- [The site should prevent users making reservations in the past.](https://github.com/users/ewradcliffe/projects/5/views/1?pane=issue&itemId=74917161)
- [The front end of the programme should be designed to allow for intuative use.](https://github.com/users/ewradcliffe/projects/5/views/1?pane=issue&itemId=74917009)
- [Menu should be visble to customers without a login.](https://github.com/users/ewradcliffe/projects/5/views/1?pane=issue&itemId=73489292)
- [The website should support the marketing objectives of the business.](https://github.com/users/ewradcliffe/projects/5/views/1?pane=issue&itemId=73489644)

##### Could have
Features which may be useful, but will not add as much value to the site.
- [Customers can submit special queries via the website.](https://github.com/users/ewradcliffe/projects/5/views/1?pane=issue&itemId=73489518) (This was changed to won't have during this cycle of the development process.)
- [Website displays additional information to the customer.](https://github.com/ewradcliffe/restaurant-booking-system/issues/8) (This was changed to won't have during this cycle of the development process.)


##### Won't have
Features which will not be part of the iteration of development. May be considered in future cycles.

- A system for matching reservations with tables.
- A system for capping reservation numbers at any given point in time. 

A Django project consists of one or more linked apps. Based on the above prioritisation the core of the project was to be an app to manage the reservations. A second app to display the restaurant menu could be added later.

### Structure

Once the scope of the project for the initial cycle of Agile development had been decided it was clear how the project could be structured.  Using Djangos Model View Template (MVT) paradigm the below structure was planned.

##### Authentication 
The standard framework of authentication was installed and a superuser created with access to the admin page. Summernote and init methods were used to add functionality and improve user experience in the admin page.

Some styling was added to the authenticaton pages to make them fit the themes of the project, however they are otherwise unchanged.

###### base.HTML
Not linked to a veiw, the base.html template consists of the header and footer with the content of other templates rendered in the main section depending on user selection.

#### Reservations app
##### Model
Django has a built in User Model so it was only necessary to plan a model for the Reservations table. The below Entity Relationship Diagram (ERD) showing the table fields was prepared prior to development.

![Reservation model ERD](static/images/reservationerd.png "Reservation model ERD")

The reservation_time and number_of_guests fields are set to choices (providing users with a fixed number of input choices) rather than TimeField or NumField inputs. This was the most straightforward way of presenting the user with limited inputs preventing them booking outside opening hours or booking for too many guests.

Please note that the user wasn't set to ondelete (i.e. any entries by the user being deleted if their user profile is deleted). I wanted staff to be able to set reservations for customers and add to the menu. Staff turnover can be high in the hospitality sector and I wanted restaurant managers to be able to delete staff profiles without deleting data entries they had made.

The Reservation Model is converted to a form in forms.py. The fileds reservation_name, reservation_date, reservation_time and number_of_guests are extracted to be displayed to the user as input feilds. Django's DateInput widget is added to the reservation_date field to display a datepicker.

##### Veiw
The below views were created to filter data.

###### index
As the only role of the index was to render the front page content no complex programming was required.
class index(generic.ListView):

##### ReservationList
This renders a list of reservations already created. Note that reservations not made by the user are filtered out by the template not the view. This has no impact on the performance of a small app, but could impact performance of a larger app. It is a point for consideration for future phases of agile development.

##### check_time.
This function compares the time and date of a reservation against the datetime modue to check if a reservation is in the past. 

#### add_reservation
This view renders the reservation form derived from the model to the screen. If the data entered is valid (as per the parameters of the model) it checks the entry is not in the past using the check_time function. If this is valid it saves the data in the database and provides a validation message to the user. If not it advises the user of the error. 

#### delete_reservation
This view is triggered when a user clicks on the 'delete' button of a reservation. It displays the reservation to the user and asks if they are sure they want to delete the reservation. If not they are returned to the reservations page. 
       
##### confirm_delete_reservation
If the user confirms they want to delete the reservation this function is triggered. It deletes the reservation from the database, returns the user to the reservation page and displays a message confirming the reservation has been deleted.

##### edit_reservation(request, id):
This view is triggered if the user selects the edit reservation button on an existing reservation. It uses the same template as the add reservation function but adds the details of the existing reservation as context. It performs the same validation checks as the add_reservation view. Users are presented with appropriate feedback if they enter invalid data, and a success message once the update has been a success.

##### Templates

###### index.html
Displays as the front page to a user who lands on the page for the first time. The user sees some photographs and text which convey the ambience of the restaurant. There is a button linking to the page where they can make a reservation as a call to action.

###### reservation.html
If a user is logged in they are presented with a message advising them as such and linked to the page where they can sign in. Once they are logged in they can see a list of reservations they have made displayed as cards. They can edit or delete these reservations by clicking the appropriatley titled buttons. They can also make a new reservations clicking the 'make reservations' button.

##### delete_reservation.html
This template renders the detail of a reservation to the page if the user selects the 'delete' button on a reservation. It asks the user if they are sure they want to delete the reservation.

###### make_reservation.html
This is used by both the add_reservation and edit_reservation views to render the reservation form using crispy forms.


#### Model app
As displaying a menu was a 'should have' rather than 'must have' feature this was planned and added after development of the Reservations app.

#####  Menu model
The Entity Relationship Diagram (ERD) below was prepared prior to development.

![Menu model ERD](static/images/menuerd.png "Menu model ERD")

menu_entry_type provides the user with a choice between Starter, Main, Dessert or Drinks for their entry, corresponding with a section on the menu page on the site.

##### View
The menu app only needs a single view. This extracts data from the database and adds it as context to the menu template. It also sets out the catagories in a tuple so they can be added as context to the menu template

##### Template
The menu.html template displays the catagories for menu items to the screen. It then uses a for loop to iterate through the database entries and display the selected fields under the appropriate catagory heading.


### Skeleton
The site was designed to have intuitve navigation and use, and follow the principles of mobile first design. The below wireframes were drafted as a guideline for the development of the site.

- Wireframes

A consistant header and footer appears on all pages. The header consists of a navigation bar with the restaurant logo in the top left hand corner and if clicked returns the user to the home page. A three bar 'burger' button opens a drop down menu when clicked, allowing the user quick navigation to the home page, the reservation page, the menu page, the register and log in page (if not logged in) or the sign out page (if logged in). On  screens of 980px and above the burger button is replaced with individual tabs for the above pages. The navigaton bar also gives the user login status. This can also be used to navigate to the log in or register pages if they are not logged in. The footer displays links to social media sites and on screens of 768px and above the footer expands to give the opening hours and address of the restaurant.

Mobile and large screen vesions of the header and footer.
![header and footer (mobile)](static/images/mobileheaderandfooter.png "header and footer (mobile)")
![header and footer (large screen)](static/images/largeheaderandfooter.png "header and footer (large screen)")

The most prominant buttons change colour when the mouse is hovered over it.

The landing page sets the brand of the restarant, with a hero image of a log fire, pictures of food, and text describing the history of the restaurant. At the bottom there is a call to action to click the 'Make a reservation' button.

Mobile and large screen vesions of the reservation page.
![Index page (mobile)](static/images/mobileindex.png "Index page (mobile)")
![Index page (large screen)](static/images/largeheaderandfooter.png "Index page (large screen)")

If logged in, the make a reservation page displays existing reservations as 'cards' using the bootstrap feature. The cards have buttons to edit or delete the reservations. A large button invites the user to 'Make a reservation'. If not logged in the user is advised as such with text linking them to the corresponding log in and register pages.

Mobile and large screen vesions of the reservation page.
![Reservation page (mobile)](static/images/mobilereservation.png "Reservation page (mobile)")
![Reservation page (large screen)](static/images/largereservation.png "Reservation page (large screen)")

On clicking the 'Make a reservation button' the user is directed to a form with input fields for name, date (with a datepicker), time and number of guests drop down menu, and a submit button. Past dates on the datepicker ae greyed out. If the user tries to submit empty or invalid data they are advised of the error in red text. The page remains displayed so they can easily correct the error. Once the reservation has been successfully made they are returned to the reservation page where they can see their reservaton and a pop up message confirms their success.

Image of page with successful reservation and pop up message.
![Success Message](static/images/mobilesuccessmessage.png "success Message")

Example of an error message. The name field has been left blank.
![Error Message](static/images/mobileerrormessage.png "Error Message")

Mobile and large screen vesions of the add reservation page.
![Make reservation page (mobile)](static/images/mobilemakereservation.png "Make reservation page (mobile)")
![Make reservation page (large screen)](static/images/largemakeareservation.png "Make reservation page (large screen)")

Clicking on the 'edit' button on a reservation card takes the user to a the same page as they used to make a reservation, excepting the form is prepopulated with the details of the existing reservation. The details can be amended here and the submission process is identical with the above.

Mobile and large screen vesions of the edit reservation page.
![Edit reservation page (mobile)](static/images/mobileeditreservation.png "Edit reservation page (mobile)")
![Edit reservation page (large screen)](static/images/largeeditreservation.png "Edit reservation page (large screen)")

Clicking on the 'delete' button on a reservation card takes the user to a new page displaying the reservation details. The user has the option to delete the reservation or return to the reservation page. In either case they are returned to the reservation page. If they choose to delete the reservation a pop up messages advises them of the success of the action.

Mobile and large screen vesions of the delete reservation page.
![delete reservation page (mobile)](static/images/mobiledeletereservation.png "delete reservation page (mobile)")
![delete reservation page (large screen)](static/images/largedeletereservation.png "delete reservation page (large screen)")

Clicking on the menu tab takes the user to the restaurant menu. Items are grouped under 'Starter', 'Main', 'Dessert' or 'Drink' depending on type. Items are logically displayed in boxes, with the name in bold, a short description and price.

Mobile and large screen vesions of the menu page.
![Menu page (mobile)](static/images/mobilemenu.png "Menu page (mobile)")
![Menu page (large screen)](static/images/largemenu.png "Menu page (large screen)")


Clicking on either the 'register' or 'log in' buttons takes the user to pages where the user can perform these corresponding actions. The user also has the option to reset password vi email. If the user clicks the 'sign out' button they are taken to a page asking them to confirm the decision.

Mobile and large screen vesions of the sign up page.
![Authentication (mobile)](static/images/mobilesignin.png "Authentication (mobile)")
![Authentication (large screen)](static/images/largesignin.png "Authentication (large screen)")

### Surface
The surface of the page was designed in line with the marketing objectives of the site. The Blue Boar Inn presents itself as a relaxing and cosy restaurant which leans heavily into it's historical links. The below stylings were selected as supportive of this.

###### Fonts.
IM Fell English SC was selected for the majority of the text. Bokor was selected for the logo. Both are medieval looking fonts which link the restaurant to it's medieval origins. Bokor distinguishes the restaurant logo from the majority of the text.

###### Colours
The below colour pallete was selected to support the site branding. A warm pallette supports the cosy, cumfortable image. The use of natural colours supports the historical image. In practical terms different colours help the user distinguish site elements.

- black - all text.
- rgb(253, 248, 216) - main background
-  rgb(173, 155, 52) - header and footer
- rgb(250, 230, 120) - reservation cards
- rgb(145, 123, 4) - where an item changes colour when hovered over and a lighter colour provides a greater contrast
-  rgb(37, 32, 1) - where an item changes colour when hovered over and a darker colour provides a greater contrast
- rgb(150, 148, 148) - borders of menu items.

###### Images
Images were selected from [Pexels](https://www.pexels.com/). Some images were resized and cropped to fit the styling of the site and reduce load time. A log fireplace was used as a hero image, helping users imagine what the inside of the restaurant may be like. Images of tasty meals were added to the index page to give users an idea of what food is served.

###### Interactivity.
The main buttons have been increased in size. They change colour when hovered over to make it clear to users they can be clicked.

designers finalize the product's features such as color, typography, and visual elements that the user will interact with


### Testing
Both manual and automated tests were used in the testing of the programme.

#### Manual tests

| Function | Test | Pass |
| :------: | ----: |  ----: |
| General | Index page fully renders with all content visible | ✓ |
| General | All links routed to correct pages | ✓ |
| General | Menu page fully renders with all content visible | ✓ |
| General | Header collapses to dropdown on small screens | ✓ |
| General | Footer minimised on small screens | ✓ |
| General | latest version deployed to Heroku | ✓ |
| Access | Users able to login with username and email | ✓ |
| Access | User given feedback as to if they are logged in or not | ✓ |
| Access | Log in feedback links to register and log in pages | ✓ |
| Access | Users unable to access admin page without proper permissions | ✓ |
| Reservations | Reservations only visible when logged in | ✓ |
| Reservations | User can only view reservations they have made | ✓ |
| Reservations | Logged in user can make a reservation | ✓ |
| Reservations | Logged in user can edit a reservation | ✓ |
| Reservations | Logged in user can delete a reservation | ✓ |
| Reservations | Logged in staff/superuser can make a reservation | ✓ |
| Reservations | Logged in staff/superuser can edit a reservation | ✓ |
| Reservations | Logged in staff/superuser can delete a reservation | ✓ |
| Reservations | Datepicker prevents user booking date prior to current date| ✓ |
| Reservations | Reservation form cannot be submitted without all fields being completed | ✓ |
| Menu | Menu page fully renders all content to correct sections | ✓ |
| Menu | Logged in staff/superuser can add menu items | ✓ |
| Menu | Logged in staff/superuser can edit menu items | ✓ |
| Menu | Logged in staff/superuser can delete menu items | ✓ |
| Menu | Menu items can only be created, edited and deleted through admin panel | ✓ |


NB - at present the time checker is one hour behind current time.

#### Automated tests
The below automated tests were set up and pass. Please enter python3 manage.py test in the command line to repeat them

|  Programme         | Test | Pass |
| :---------------- | :------: | ----: |
| Menu Views | Confirm menu item can be seen without logging in. | ✓ |
| Menu Views | Confirm menu item can be seen after logging in | ✓ |
| Reservation Form | Tests form is valid. | ✓ |
| Reservation Form | Tests name field. | ✓ |
| Reservation Form | Tests date field. | ✓ |
| Reservation Form | Tests time field. | ✓ |
| Reservation Form | Tests number of guests field. | ✓ |
| Reservation Views | Tests to see if the index page renders. | ✓ |
| Reservation Views | Tests to see if the reservation page renders. | ✓ |
| Reservation Views | Test to see if the add reservation page is rendered. | ✓ |
| Reservation Views | Test to see if the edit reservation page works. | ✓ |
| Reservation Views | Test to see if the delete reservation page renders. | ✓ |
| Reservation Views | Test for making a reservation | ✓ |
| Reservation Views | Test for editing a reservation | ✓ |
| Reservation Views | Test for deleting a reservation | ✓ |

All tests pass as per below:

![Automated tests](static/images/automatedtest.png "Automated tests")



### Validation
Accessibility
All pages give identical scores when run through lighthouse in devtools.

![Lighthouse report](static/images/lighthouse.png "Lighthouse report")


###### HTML
The below pages were put through the [W3C validator](https://validator.w3.org/) and returned no errors. As the validator doesn't understand django template syntax, the URL of each page was entered into the validator

|  Page  | Pass | 
| :----- | :--: | 
| base.html (logged out) | ✓   |
| index.html (logged in) | ✓   |
| reservations.html (logged out) | ✓   |
| reservations.html (logged in) | ✓   |
| make_reservations.html | ✓   |
| delete_reservations.html | ✓   |
| menu.html | ✓   |
| logout.html | ✓   |
| login.html | ✓   |
| password_reset.html | ✓   |
| signup.html | x |

Signup HTML returns four errors. Unfortunately, these are all in the rendering of the form in the lines below and are inaccessable for editing.

![Signup error](static/images/signuperrorone.png "signup error")
![Signup error](static/images/signuperror.png "signup error")

##### CSS
The below pages were put through the [W3C validator](https://jigsaw.w3.org/css-validator/#validate_by_input)
|  Page  | Pass | Message |
| :----- | :--: | :--: | 
| static/css/style.css | ✓   | Imported style sheets are not checked in direct input and file upload modes |

The single CSS style sheet passes without error, and with the message listed above. This simply means the check is limited only to this page.

##### PEP8
The below pages were put through the [W3C validator](https://pep8ci.herokuapp.com/#) and returned no errors
|  Page  | Pass | 
| :----- | :--: | 
| menu/admin.py | ✓   |
| menu/apps.py | ✓   |
| menu/models.py | ✓   |
| menu/test_views.py | ✓   |
| menu/urls.py | ✓   |
| menu/views.py | ✓   |
| reservations/admin.py | ✓   |
| reservations/apps.py | ✓   |
| reservations/models.py | ✓   |
| reservations/test_forms.py | ✓   |
| reservations/test_views.py | ✓   |
| reservations/urls.py | ✓   |
| reservations/views.py | ✓   |
| restuarant/asgi.py | ✓   |
| restuarant/urls.py | ✓   |
| restuarant/settings.py | x   |
| restuarant/wsgi.py | ✓   |

Settings.py has five E501 line too long errors. These are the secret key and the 4 allauth password validators. These can't be fixed by adding a '\' without causing an error so I have left them unaltered. 

## Deployment
The application was created on Gitpod using The Code Institute template (https://github.com/Code-Institute-Org/ci-full-template) and VS Code Plugin and deployed to Github with the following steps:

Login to Github, otherwise create an account.

Navigate to the repository ('Explore -> 'ewradcliffe/restaurant-booking-system') or follow the link (https://github.com/ewradcliffe/restaurant-booking-system).

Please note that to save any changes:

Save as usual

To commit changes, enter 'git add .' in the terminal and then enter 'git commit -m "summarise changes."
Once all changes are made use the command 'git push' to push changes to github.

##### To fork:

Click fork in the top right hand corner, and create new fork.

Confirm the owner of the fork, the repository name and description.

Click "Create fork".

##### To clone:

To clone, you must first fork the repository as per above.

Click on the "Code" button and copy the URL.

In Git Bash, navigate to the location you would like to create the cloned directory.

Enter git clone, paste the URL, and press enter.

##### Prior to deployment
If any changes have been made to the static files, please enter the command python3 manage.py collectstatic. You will be asked if you would like to overwrite existing files. Enter 'yes' to make sure all static files are collected for deployment.

In setting.py set DEBUG to FALSE to allow for debugging outside of the local environment.

Add, commit and push your changes to github.

##### Heroku

The programme is deployed on Heroku ('https://theboarshead-a33405e8a5e0.herokuapp.com/')

To update deployments, navigate to ('https://heroku.com') and either login, or follow the steps to create an account. Navigate to the deployment tab, scroll to the bottom and click deploy branch.

To create a new app navigate to the dashboard, click on the 'New' button and click 'Create new app' from the dropdown. Give the app a name, select your region and click create app. Please note that app names need to be unique to the platform as a whole. Heroku will not accept spaces as characters. You will need to use hyphens.

To link the database to Heroku navigate to the 'Settings' tab and click 'Reveal Config Vars' You will need to add a key of DATABASE_URL and a value of either the PostgreSQL database linked in settings (if linking to this project), or your own database. You will also need to add SECRET_KEY as a key and the value of the secret key found in env.py

Navigate to the 'Deployment' tab. You will have the option to set up automatic deployment so the app is automatically updated with any changes pushed to github.

Then connect your GitHub repository and click 'deploy branch'

## Future development.

It is reccomended that The Django documentation ('https://www.djangoproject.com/') is studied before any changes are made.

## Technologies used.
Python 3.12.2
Django 4.2.14
Heroku
PostgreSQL
Summernote
Cloudinary is installed, but not used in the final version
Crispy Forms
Bootstrap 5.

### Credits.

- Favicon generated by https://www.favicon-generator.org/
- All pictures are free images from https://www.pexels.com/
- Tests taken from 'I think therefore I blog Django Tutorial from https://learn.codeinstitute.net/
- Sign in status and message pop up adapted from 'I think therefore I blog Django Tutorial from https://learn.codeinstitute.net/
- Function to delete reservation adapted from https://www.w3schools.com/django/django_delete_members.php
reservation_time, number_of_guests and menu_type code from Models inspired by https://blog.devgenius.io/django-tutorial-on-how-to-create-a-booking-system-for-a-health-clinic-9b1920fc2b78
- Navbar adapted from https://www.w3schools.com/bootstrap/bootstrap_navbar.asp.
- Footer based on https://mdbootstrap.com/snippets/standard/mdbootstrap/2885092?view=side
