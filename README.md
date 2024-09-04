


### Database Schema

The Entity Relationship Diagrams (ERD) below were prepared prior to development.

#### Reservation model ERD

![Reservation model ERD](static/images/reservationerd.png "Reservation model ERD")

The reservation_time and number_of_guests fields are set to choices (providing users witha fixed number of input choices) rather than TimeField or NumField inputs. This was the most straightforward way of presenting the user with limited inputs preventing them booking outside opening hours or booking for too many guests.

#### Menu model ERD

![Menu model ERD](static/images/menuerd.png "Menu model ERD")

menu_entry_type provides the user with a choice between Starter, Main, Dessert or Drinks for their entry, corresponding with a section on the menu page on the site.

Please note that in both cases the user wasn't set to ondelete (i.e. any entries by the user being deleted if their user profile is deleted) as I wanted staff to be able to set reservations for customers and add to the menu. Staff turnover can be high in the hospitality sector and I wanted restaurant managers to be able to delete staff profiles without deleting data entries they had made.



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
| Access | Log in feedback links to sign up and log in pages | ✓ |
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


### Credits.

- Favicon generated by https://www.favicon-generator.org/
- All pictures are free images from https://www.pexels.com/
- Tests taken from 'I think therefore I blog Django Tutorial from https://learn.codeinstitute.net/
- Sign in status and message pop up adapted from 'I think therefore I blog Django Tutorial from https://learn.codeinstitute.net/
- Function to delete reservation adapted from https://www.w3schools.com/django/django_delete_members.php
reservation_time, number_of_guests and menu_type code from Models inspired by https://blog.devgenius.io/django-tutorial-on-how-to-create-a-booking-system-for-a-health-clinic-9b1920fc2b78
