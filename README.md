# Top Rock 

Top Rock is an application helping users discover top rock bands of all time. The users will be prompted with a login/sing up form where they would have to create an account and log in, after the successful log in users will be prompted with a list of artists where they could pick a band of interest that they want to discover more about and have conversations about that particular band.After choosing an artist the users will see an image header with the band, a description about the band and the members of the band then right below the description section there are the bands album images all displayed in a carousel all fetched from MongoDB, the last section is a comment panel where users can discuss interesting thinks about the band.

# UX
### Strategy 
Top Rock is designed for users interested in the greatest bands of all time. The layout of the application includes 
Navigation Bar, Footer, Login/SingUp form, List of bands, Artist Description, Album Image Carousel, Comment Section.

The following link shows the initial mockups for the Wintersun Website using pen and paper https://github.com/ChristianPlesca/Milestone-Project3/tree/master/static/wireframes

### User Stories 
1. As a User, I must be able to log in, Logout and SingUp.
2. As a User, I must be able to see each album released by the band.
3. As a User, I must be able to see a description of the individual band and the bands members.
4. As a User, I must be able to leave comments on the specific band's page.

## Features 
### Existing Features
1. Login/SingUp allows you to to create an account and login to the website.
2. Navbar allows you to navigate through the website. 
3. The home page allows you to pick any band of interest an go to the artist page.
4. Description section gives you an introduction about the selected band.
5. Album section allows you to see every album of the band nicely presented in a carousel.
6. Comment section allows you to Insert, Read, Update, Delete a comment. 


### Features Left To Implement 
* Search Bar where you can search for a specific band. 
* Loading Gif when the images load in the home page.
* User Image where the user can insert a photo of themselves.
* Few small bugs to be fix


# Technologies
1. Html5 
2. Css3 
3. Javascript 
4. Jquery 
5. Bootstrap
6. Font Awesome 
7. Python 
8. Flask 
9. MongoDB
10. Sqlite 
11. Visual Studio Code 
12. Google Fonts 
13. Heroku
14. Git 
15. GitHub 

### Resources
* [Stackoverflow](https://stackoverflow.com/)
* [W3schools](https://www.w3schools.com/)
* [Google](https://www.google.com/)
* [Flask Documentation](https://flask.palletsprojects.com/en/1.1.x/#)
* [MongoDB Documentation](https://docs.mongodb.com/manual/)

## Testing
*  The application was constantly tested during development using Opera GX dev tools. I used this to resize the browser to check the new code was working, breakpoints, and different mobile/tablet screen sizes.
* After deployment, I've tested the website on multiple browsers such as Mozilla(FireFox), Opera, Chrome, Microsoft Edge, Safari.
* Used https://jshint.com for testing Javascript files - No major issues were found
* Used [Google Mobile-Friendly Test](https://search.google.com/test/mobile-friendly?utm_source=support.google.com/webmasters/&utm_medium=referral&utm_campaign=%206352293) - received this page is easy to use on a mobile device
* Used HTML and CSS validator [NuHTMLChecker](https://validator.w3.org/nu/#textarea) and [W3C-CSS](https://jigsaw.w3.org/css-validator/validator) - No major issues found
* The Login Sign Up form was tested by creating new users, by trying to create a user with the same name/email witch has already been created.
* The comment section was tested by creating multiple messages, when inserting, deleting or updating a message it should redirect back to the comment section, the message field should load every 10 seconds so you don't have to refresh the browser each time you want to see replies
* Tested the comments/comments count so they are inserted on the particular artist URL
* The Delete/Edit comment was tested so the user can edit or delete their own messages, the other users must not be albe to delete or edit other users comments
* Tested the comment box so that users can't click Post New Comment if the textarea is empty
* The user should not be able to insert more than 500 characters



### Issues encountered
* Flask - Fetching the comments into artist page so the same comments don't display for all the artists 
* Flask - Redirect after CRUD back to artist_page
* Heroku - Deployment
### Steps taken to resolve issues
* Searched for solutions on Goole and StackOverflow
* Read Flask , Heroku documentation

## Deployment
The deployment of the website was done using Heroku, a link to the website can be found [Here](https://top-rock.herokuapp.com/).
To deploy to project to Heroku I used the following steps:
* Created a virtual environment using pipenv 
* Installed all the dependencies using pipenv install package name
* Created an app on the Heroku Platform
* Installed the package Gunicorn 
* Used echo web: gunicorn app:app > Procfile to create the Procfile
* Set the IP 0.0.0.0 and PORT 5000
* Created the requirements.txt file using pip3 freeze --local > requirements.txt
* Used the commands Heroku git:remote -a (app name) , git add . , git push -u Heroku master

## Credits
The login form was taken from [https://colorlib.com/wp/html5-and-css3-login-forms/] and has been overwritten by me to fit my needs.

### Media 
* Images were taken from [Google](https://www.google.com/)

Website for educational purposes only.