# supernatural_webdev

## What it is?

This is a project made for Web Development class. Basically, it is a blog made entierly in Django (Python framework) as the backend. Project / blog theme is popular TV Show [Supernatural](https://www.imdb.com/title/tt0460681/).
![](http://www.thecinemalaser.com/wp-content/uploads/2019/02/Movie-Review-Supernatural.jpg "Crowley, Dean, Sam, Castiel")

## What can I do on it?

- user managment
  - admin has **_full CRUD_** over users (except password)
  - registration
  - login
  - personal account page
- blogging
  - CRUD blog posts
  - vote (like) on blogs
- personal account / blog
  - user can see his own blogposts
    - published
    - unpublished
  - user can see other people's **_published_** blogs
- administration
  - publishing posts that follow rules
  - moderating blog posts
  - moderating comments

## Technologies used

1. Django for backend
   - taking care of database, sessions and cookies
   - handling requests and queries through views
2. HTML5, CSS3, Bootstrap 5 and Javascript for frontend
   - multiple HTML documents for navigation
   - mobile first design - fully responsive
   - Javascript and CSS animations for niche
3. AJAX handles most of post requests
