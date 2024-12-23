# **TuneCritic Blog**
##  **App Overview**
As a big music fan, I wanted to create a blog that showed reviews of some pivotal albums of the last 20 years.

The TuneCritic blog is designed to allow any user to view reviews that are written by users, and anyone to sign up, create an account, and write their own reviews for albums that can be viewed by any visitors on the site. The app enables users to edit, delete the reviews they have posted. It provides a community-driven space for music enthusiasts to share their opionions and discover new perspectives on albums from the past two decades. 

<hr>

Click [here](https://tunecritic-b151784f4800.herokuapp.com/) for Heroku deployment of app

<hr>

## Table of Contents:

1. [**App Overview**](#app-overview)
1. [**Planning**](#planning)
    * [**Strategy**](#strategy)
      * [**Application Goals**](#app-goals)
      * [**Target Audiences**](#target-audiences)
      * [**Wireframes**](#wireframes)
    * [**Entity Relationship Diagram**](#erd)
    * [**Color Scheme**](#color-scheme)
    * [**Typography**](#typography)
1. [**Agile Development**](#agile-development)
    * [**User Stories**](#user-stories)
1. [**Features**](#features)
    * [**Admin**](#admin)
    * [**Header**](#header)
    * [**Home Page**](#homepage)
    * [**My Reviews**](#my-reviews)
    * [**Review Detail**](#review-detail)
    * [**Add Review**](#add-review)
    * [**Edit Review**](#edit-review)
    * [**Delete Review**](#delete-review)
    * [**Accounts**](#accounts)
      * [***Login***](#login)
      * [***Logout***](#logout)
      * [***Signup***](#signup)
    * [**Messages**](#messages)
    * [**Defensive Design**](#defensive-design)

1. [**Future Features**](#future-features)
1. [**Testing**](#testing)
1. [**Deployment**](#deployment)
1. [**Technology**](#technology)
1. [**Media**](#media)
1. [**Credits**](#credits)
1. [**Acknowledgments**](#acknowledgements)

## **Planning**

### **Strategy**

#### **Application Goals**
- **Create an intuitive platform** where users can share and discover reviews for albums.
- **Provide secure user accounts** enabling individuals to add, edit, and manage their own reviews.
- **Facilitate community interaction** by allowing user to express their thoughts on albums, creating a space for music enthusiasts to connect.
- **Ensure responsive design**, so the blog can be enjoyed across devices of different screen sizes.

#### **Target Audiences**

- **Music Enthusiasts** who enjoy discovering new albums and reading reviews from others.
- **Bloggers and critics** looking to share their reviews and opinions on popular albums
- **Casual Listeners** who want to learn more about albums before deciding to listen to them.


### **Wireframes**

I used Figma to create wiremframes for this project. I wanted to create a very basic design that would meet the criteria as I had outlined in my user stories.

* [Homepage](docs/wireframes/home.png)
* [My Reviews](docs/wireframes/my-reviews.png)
* [Review Detail](docs/wireframes/review-detail.png)
* [Add Review](docs/wireframes/add-review.png)
* [Edit Review](docs/wireframes/edit-review.png)
* [Delete Review](docs/wireframes/delete-review.png)

I wanted to keep my design simple at this early stage of design, however I liked the simple color scheme of black and white, and choose to keep this as the project progressed into the later stages.

### **Entity Relationship Diagram**

The app consisted of one custom model, the Review model, and the user model from Django was imported. You can see a visual representation of the relationship between these to models [here](docs/erd/erd.png).

### **Color Scheme**

I had done some research on music blogs and review sites, the most popular of which being pitchfork. I decided to keep with a very similar color scheme.

- **Header and Footer**: #212529
- **Main section**: #fff
- **Typography**: #000000 and #fff

### **Typography**

For this project I kept it simple and left the default bs-font-sans-serif variable that points to the list of fonts as are available depending on a users system (inlcuding Roboto, Segoe UI, Helvetica Neue, Noto Sans).

## **Agile Development**

### **User Stories**


The agile development phase of this project involved adopting the perspective of the future user. I tried to step into the shoes of a future user and understand what basic features and functionality I would expec, which lead me to developing 8 essential user stories. Each user was created using Githubs issues features, and includes acceptance criteria and that are represent the tasks I was to take on as the developer in this project. When I felt the acceptance criteria of each user story had been met, I moved the user story from 'In Progress' to 'Complete' on the kanban board within the Github project that was created. 

> User Stories

1. [User Story: Admin Login](https://github.com/users/jamiemcstay/projects/4/views/1?pane=issue&itemId=89391178&issue=jamiemcstay%7Cportfolio-4%7C4)
2. [User Story: Displaying Reviews](https://github.com/users/jamiemcstay/projects/4/views/1?pane=issue&itemId=89392864&issue=jamiemcstay%7Cportfolio-4%7C8)
3. [User Story: Review Management](https://github.com/users/jamiemcstay/projects/4/views/1?pane=issue&itemId=89391403&issue=jamiemcstay%7Cportfolio-4%7C5)
4. [User Story: User Registration](https://github.com/users/jamiemcstay/projects/4/views/1?pane=issue&itemId=89389801&issue=jamiemcstay%7Cportfolio-4%7C1)
5. [User Story: User Login](https://github.com/users/jamiemcstay/projects/4/views/1?pane=issue&itemId=89390446&issue=jamiemcstay%7Cportfolio-4%7C2)
6. [User Story: User Logout](https://github.com/users/jamiemcstay/projects/4/views/1?pane=issue&itemId=89390869&issue=jamiemcstay%7Cportfolio-4%7C3)
7. [User Story: Edit Review](https://github.com/users/jamiemcstay/projects/4/views/1?pane=issue&itemId=89392214&issue=jamiemcstay%7Cportfolio-4%7C6)
8. [User Story: Delete Review](https://github.com/users/jamiemcstay/projects/4/views/1?pane=issue&itemId=89392529&issue=jamiemcstay%7Cportfolio-4%7C7)

## **Features**

### **Admin**

Users with superuser credentials can manage the platform's users, manage posts, and edit reviews.

### **Header**

The header features the TuneCritic logo, navigation menu, and user authentication links (login/logout/signup). It remains consistent across pages, offering quick access to the home page, and the 'My Reviews' section to add, edit and remove reviews for authenticated users. 

### **Home Page**

The home page is where users and visitors can browse thumbnails of all reviews that have been posted to the site. When a user or a visitor clicks into a specific review they are redirected to an expanded version of the review.

### **My Reviews**

This page is where users can view all the reviews they have posted to the site. Also, users can add reviews, and edit and delete existing reviews. If an authenticated visitor tries to access this page, they will be redirected to either login, or create an accout. 

### **Add Review**

A form that allows authenticated users to a submit a new review, including the album title, artist name, a rating, and a text field for their opinion on the album.

### **Edit Review**

An form that allows users to edit their existing reviews by updating the text and other details that were previously added.

### **Delete Review**

A simple option for users to delete their reviews from the platform, once a user clicks the delete button they are redirected to a page that asks them to confirm they are sure they want to delete that review.

### **Accounts**

#### **Login**

Allows registered users to securely log in to their account using their credentials (username and password).

#### **Logout**

A button that securely logs the user out of the platform, ensuring their session ends.

#### **Signup**

A registration process for new users to create an account, enabling them to write their reviews.

#### **Messages**

Using messages users are informed of having logged in or out of the system, as well as if they have added, edited or deleted a review on the platform.

### **Defensive Design**

The app includes validation and safeguards against common errors, such as entering invalid ratings, submitting incomplete forms, and ensuring only authenticated users can perform specific actions like posting reviews, editing, and deleting them.

## **Future Features**

- **Comment System**: Allow users to leave comments on individual reviews.
- **Recommendations**: Allow users to receive recommendations based on the rating they give for albums.
- **Social Sharing**: Add features to share reviews on social media platforms.
- **Search Functionality**: A search bar for users to find album reviews based on the artist, album name, genre, or rating.

## **Testing**

### **Account Registration and Authentication Tests**

| Test |Result  |
|--|--|
| User can register a new account | Pass |
| User can log into their own account | Pass |
| User can log out of their account | Pass |
| Error messages displayed for invalid data entry | Pass |
| Users are redirected to signup when trying to access 'My Reviews' tab | Pass |

### **User Navigation Tests**

| Test |Result  |
|--|--|
| User can navigate to home page | Pass |
| Authenticated users can access the My Reviews page | Pass |
| User can click on a review to view the details of that review | Pass |
| Navigation links are functional and easily visible for users | Pass |
| Logged out users can navigate to the signup page | Pass |
| Logged can view their reviews on the My Reviews page | Pass |

### **Review Management Tests**

| Test |Result  |
|--|--|
| Authenticated user can create a new review   | Pass |
| Authenticated users can edit an exisint review they have created | Pass |
| Authenticated users can delete a review | Pass |
| Authenticated users can view their own reviews in the My Reviews page | Pass |
| Users cannot edit or delete other users reviews | Pass |
| Error messages appear for incomplete forms | Pass |

### **Admin Tests**

| Test |Result  |
|--|--|
| Users with superuser credentials can access the admin page  | Pass |
| Users without superuser credentials cannot access the admin page | Pass |
| Admins can manage user accounts from admin page | Pass |
| Admins can view, edit and delete reviews from admin page | Pass |
| Changes made in admin panel reflect on front end | Pass |

### **Defensive Design**

| Test |Result  |
|--|--|
| User cannot access restricted pages without logging in  | Pass |
| Input fields validate data correctly | Pass |
| Error messages display for invalid form submission | Pass |
| Review submission is prevented for authenticated users | Pass |

### **Messages**

| Test |Result  |
|--|--|
| Message display informing user they have logged in  | Pass |
| Messages display when user has successfully adding, edited or deleted a review | Pass |

## **Deployment**

I followed these steps to deploy my app on Heroku.

1. **Log in to Heroku**

2. **Create a New App**

- Navigate to Heroku Dashboard, click the **New App** button in the top right corner and select **Create New App**.

3. **Configure Environment Variables**

-  Go to the **Settings** tab, scroll to the **Config Vars** sections, and click **Reveal Config Vars**

- Add the necessary key value pairs for the app to function correctly.

  - 'CLOUDINARY_URL': cloudinary://...
  - 'DATABASE_URL': postgres://...
  - 'SECRET_KEY': my django secret key

- Update Django 'settings.py' file to include the Heroku hostname in the 'ALLLOWED_HOSTS' list:
  - ALLOWED_HOSTS = ['8000-jamiemcstay-portfolio4-tlooqyh8svk.ws-eu117.gitpod.io',
'.herokuapp.com']

4. **Prepare app for deployment**

- Ensured project has the following files:

  - 'requirements.txt'
  - 'Procfile ('containing 'web:gunicorn project_name.wsgi')

- Set `DEBUG = False' in 'settings.py' file.
- Save changes, add the files to Git, commit, and push to Github. 

5. **Connect Heroku to Github repository**

- In the Heroku app's **Deploy** tab, choose **Github** as the deployment method.
- Search for the repository by name in the search bar, click the main branch and then click **Connect**.

6. **Deploy App**

- Selected **Manual Deploy**
- Click **Deploy Branch** to initiate the deployment.

7. **Launch App**

- Once the build process completes, click **View** to open your deployed app.

## **Technology**

- **Django**: The core framework for the app's backend.
- **PostgreSQL**: The database for storing user data and reivews.
- **HTML/CSSS**: For front-end development.
- **Heroku**: Platform for deployment.
- **Figma**: For building wireframes for the project.
- **Github**: For version control and agile development.
- **Cloudinary API**: For storing images for the app.

## **Media**

All images used for this project were sourced from google images.

## **Credits**

- **Django**
- **Bootstrap**
- **Fontawesome**

## **Acknowledgements**

Thanks to the code institute tutors staff and support team through the development of this project. Special thanks to my mentor Richard Wells for his advice and feedback throughout the duration of this project.



















