# Instructions to run the project

Visit the site deployed at https://floating-river-86847.herokuapp.com/

Login using user credentials.
Users are of three types:
- Student
- Instructor
- Admin

### Student View:
The home page consists of cards containing links to the pages of all the courses the student has been registered for, a link to view the student's gradesheet and a navbar containing the 'messages' tab and an option to logout.

The coursepage for each course has 4 tabs: 
1. Announcements (displays all the course announcements by the instructor)
2. Documents (displays all the documents uploaded by the instructor)
3. Grades (displays marksheet of the student containing summary of the marks scored by the student in each assessment of the course)
4. Quizzes (displays list of online tests/quizzes conducted in the course- a test can be attempted only once; the test can be attempted by clicking on it. After submitting the test the result page is shown)

'Messages' leads to the personal messenger for the user, where the user can text another user via their student/instructor ID, a 6 digit number unique to every user.
Clicking on 'DevClub Moodle' in the navbar leads to the home page for the user.

### Instructor View:
The instructor home page is almost identical to the student home page, the only difference being that there is no 'gradesheet' section.

The coursepage for each course that the instructor teaches has 4 tabs:
1. Announcements (displays all the course announcements by the instructor and the instructor can make new announcements as well)
2. Documents (displays all the documents uploaded by the instructor, with an option to upload more documents from the instructor's local machine)
3. Upload Student Grades (has options to upload marks for a particular assessment, as well as upload the final grades for the course, for a particular student)
4. Create A Quiz (instructor can create an online MCQ test by first inputting the name and weightage of the test; then keep adding questions. Once all questions have been added, click on the `Finish` button)
###### NOTE:
Marks for online quizzes are automatically uploaded to a student's marksheet.



### Admin View:
This leads to Django's Admin site. 

Upon creating a new User, they have to be registered in either the `Students` or `Instructors` model. New courses can be added in the `Courses` model. 
Register students or instructors for a particular course using the `Student_registration table` or `Instructor_registration table` models.

`Announcements` is for course-related announcements; `Messages` is for personal messages between two users.

`Question Bank` is for creating quizzes; `Quizattempts` is for keeping track of whether students registered for a course have attempted a particular online test or not.

`Grades` is for the final course grades of a student; `Marks` is for the marks scored by a student in a particular assessment of a course.

`Document` is for all the documents uploaded for a course.




# DevClub Assignment 5

You have learnt about backend engineering with Django in our session. Now use it to create a web application by yourself!
## DevClub LMS (Learning Management System)
You must have used **Moodle** in your courses, where both instructors and students login, and for each course, the instructor uses the platform to share resources, send announcements, release grades, conduct quizzes and what not!

Your task is to create your own such a learning management system using Django, where you can add functionalities as per your own creativity!

### We would recommend you to have these apps inside the project: 
- Users (to store auth logic, and models for `Instructor`, `Student`, `Course`, `Admin`)
- Grades (to store logic for sharing grades for any assessment, and models for let's say a class `Grade`)
- Documents (for Instructor to upload `Docs` like lecture notes for the course)
- Quizzes (this can have models for a `QuestionBank` containing `Question`'s which form a `Quiz`)
- Communication (to work on features like Course-wide `Announcements`, `Reply`ing in threads to announcements, sending personal `Messages`)

Try to implement as many features as you can, but make sure to plan the structure of the project and database schemas well!

### Bonus:
- Deploy on Heroku
- Create documentation for any RESTful APIs created with documenter on postman
- Markdown support for Communication
- Email: For registration, password reset, notifications, instructor custom message
- Bulk upload from CSV for grades, quizzes
- Generating PDF: Print digitally signed transcript
- Add security features for the quizzes

## Submission Instructions
- **FORK** this repository, by clicking the "Fork" button on top right
- `clone` the forked repo into your machine, and `cd` into the Repo Folder such that you are in same directory level as `manage.py`
- If on macOS, run `python3 -m venv env`, otherwise `python -m venv env`
- Now activate the virtual environment by `source env/bin/activate`
- See if the environment is correctly set by running `pip list`, it should be mostly empty
- Install dependencies with `pip install -r requirements.txt`
- We have already started a dummy project called `DevClubLMS` for you
- Now, you can use `python manage.py runserver` to start the dev server or `python manage.py startapp <appname>` to create a new app inside this project
- After completing the assignment, append instructions to run your project, along with explanation of features etc in this README
- It would be nice if you can host it on Heroku and also give a documentation of each endpoint through postman
- Finally submit with your details in the [Google Form](https://forms.gle/XSidrfbrsEZuDYfy6)
- You do NOT need to make any pull requests to this repo

# Resources
- [Slides used in the session](https://docs.google.com/presentation/d/e/2PACX-1vQbtDDGQonkIoGu68VrINL2s3sQcfiH5XVnk-iU26nk16DFBGsDabichsqhdtBvowPvpxaIbFLAV2h3/pub?slide=id.p)
- Introduction to Python and Django by [Programming With Mosh](https://youtu.be/_uQrJ0TkZlc)
- Detailed Django Tutorials by [Corey Schafer](https://www.youtube.com/playlist?list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p)
- [Mozilla's Tutorials](https://developer.mozilla.org/en-US/docs/Learn/Server-side) on Server Side Programming with Django
- [Django Official Docs](https://www.djangoproject.com/start/)
- [Talk](https://youtu.be/lx5WQjXLlq8) on how Instagram uses Django at production, and also [*the time when Justin Beiber almost crashed Instagram!*](https://youtu.be/lx5WQjXLlq8?t=715)
- Advice on Backend Engineering by [Hussein Nasser](https://www.youtube.com/c/HusseinNasser-software-engineering)
- Guide for Deploying Python apps on [Heroku](https://devcenter.heroku.com/categories/python-support)
- Guide for [Postman Documenter](https://learning.postman.com/docs/publishing-your-api/documenting-your-api/)
