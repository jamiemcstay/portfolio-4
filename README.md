# **TuneCritic Blog**
##  **App Overview**
As a big music fan, I wanted to create a blog that showed reviews of some pivotal albums of the last 20 years.

The TuneCritic blog is designed to allow any user to view reviews that are written by users, and anyone to sign up, create an account, and write their own reviews for albums that can be viewed by any visitors on the site. The app enables users to edit, delete the reviews they have posted. It provides a community-driven space for music enthusiasts to share their opionions and discover new perspectives on albums from the past two decades. 

<hr>

![I am Responsive Screenshot]()

Click here for Heroku deployment of app

<hr>

## Table of Contents:

1. [**App Overview**](#app-overview)
1. [**Planning**](#planning)
    * [**Strategy**](#strategy)
      * [**Application Goals**](#app-goals)
      * [**Target Audiences**](#target-audiences)
      * [**User Stories**](#user-stories)
    * [**Wireframes**](#wireframes)
    * [**Entity Relationship Diagram**](#erd)
    * [**Color Scheme**](#color-scheme)
    * [**Typography**](#typography)
1. [**Agile Development**](#agile-development)
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

#### **User Stories**

The beginning phase of the project involved adopting the perspective of the future user. I tried to step into the shoes of a future user and understand what basic features and functionality I would expec, which lead me to developing 8 essential user stories. Each user was created using Githubs issues features, and includes acceptance criteria and that are represent the tasks I was to take on as the developer in this project. When I felt the acceptance criteria of each user story had been met, I moved the user story from 'In Progress' to 'Complete' on the kanban board within the Github project that was created. 

> User Stories

1. [User Story: Admin Login](https://github.com/users/jamiemcstay/projects/4/views/1?pane=issue&itemId=89391178&issue=jamiemcstay%7Cportfolio-4%7C4)
2. [User Story: Displaying Reviews](https://github.com/users/jamiemcstay/projects/4/views/1?pane=issue&itemId=89392864&issue=jamiemcstay%7Cportfolio-4%7C8)
3. [User Story: Review Management](https://github.com/users/jamiemcstay/projects/4/views/1?pane=issue&itemId=89391403&issue=jamiemcstay%7Cportfolio-4%7C5)
4. [User Story: User Registration](https://github.com/users/jamiemcstay/projects/4/views/1?pane=issue&itemId=89389801&issue=jamiemcstay%7Cportfolio-4%7C1)
5. [User Story: User Login](https://github.com/users/jamiemcstay/projects/4/views/1?pane=issue&itemId=89390446&issue=jamiemcstay%7Cportfolio-4%7C2)
6. [User Story: User Logout](https://github.com/users/jamiemcstay/projects/4/views/1?pane=issue&itemId=89390869&issue=jamiemcstay%7Cportfolio-4%7C3)
7. [User Story: Edit Review](https://github.com/users/jamiemcstay/projects/4/views/1?pane=issue&itemId=89392214&issue=jamiemcstay%7Cportfolio-4%7C6)
8. [User Story: Delete Review](https://github.com/users/jamiemcstay/projects/4/views/1?pane=issue&itemId=89392529&issue=jamiemcstay%7Cportfolio-4%7C7)


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

For this project I kept it simple and left the default bs-font-sans-serif variable that points to the list of fonts as are available depending on a users system (inlcuding Roboto, Segoe UI, Helvetica Neue, Noto Sans)












