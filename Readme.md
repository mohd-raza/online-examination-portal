# Online-Examination Portal
This project is entitled Online Examination Portal System. This is a web-based application developed in Python and Django Framework. This project provides an automated and online Examination platform for certain Colleges or Universities. The application can be accessed by the school management, faculties, and students. It has a simple and pleasant user interface with the help of Boostrap Framework. This Online Exam System Project consists of user-friendly features and functionalities.

# Developed using:
* Python
* Django
* SQLite3
* HTML
* CSS
* JavaScript
* jQuery
* Ajax
* Pillow Library
* asgiref Library
* Django-widget-tweaks
* pytz Library
* Fontawesome
* Bootstrap

This Online Exam System Project has 3 types of user roles as I mentioned above. It gives access to the school management, faculties, and students. Each user role contains different permission or restriction to the project features and functionalities. The Student and Faculties are required to register or signup first on the site. The Faculty Accounts requires an admin validation before they can gain access to features and functionalities of its role.

In this system, the Admin Users have the privilege to access and manage most of the features and functionalities. They are the ones who validate the new teachers/faculties system account. They can also update the information of both Students and Faculty details and credentials.

The Faculties/Teachers have the privilege to manage the list of courses and questions. He/She can add a new course, delete a course, add questions to the course, and delete questions.

The Students can list all available examinations to take. In order for them to take the exam, they will simply click the 'Attend Exam Button' beside the exam name and the page will be redirected to the instruction page. Students can only select 1 answer to the options per question. Then, after the student finished answering and reviewing their answers, they can simply click the Submit Answer Button below the questionnaire. After the student answer sheet is submitted, the system will automatically check and computes the total score of the student.

Sample Snapshots:

![image](https://user-images.githubusercontent.com/91888013/206496982-6f13bc4a-75e5-493e-aaa7-41fca340a3a3.png)
![image](https://user-images.githubusercontent.com/91888013/206497097-1ac3870e-f0a0-43ef-b810-0f416c5ed4ac.png)
![image](https://user-images.githubusercontent.com/91888013/206497250-df7a3346-a33a-498c-aba6-65cbd8baddef.png)

![image](https://user-images.githubusercontent.com/91888013/206496847-562b3b9c-2c00-495d-9ac1-8845f7bd871b.png)
![image](https://user-images.githubusercontent.com/91888013/206497182-0cd845e8-d7de-44b3-85a2-3c8975f93df3.png)


## To run locally in your device:
1. pip install -r requirements.txt
2. python manage.py migrate.
3. Create a Superuser by executing the following command:
    * python manage.py createsuperuser.
4. Run the project by executing the following command:
    * python manage.py runserver
5. Open a web browser and browse *http://127.0.0.1:8000/*
