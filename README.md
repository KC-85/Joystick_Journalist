# [Joystick_Journalist](https://joystick-journalist-3eda94de87b5.herokuapp.com)

[![GitHub commit activity](https://img.shields.io/github/commit-activity/t/KC-85/Joystick_Journalist)](https://www.github.com/KC-85/Joystick_Journalist/commits/main)
[![GitHub last commit](https://img.shields.io/github/last-commit/KC-85/Joystick_Journalist)](https://www.github.com/KC-85/Joystick_Journalist/commits/main)
[![GitHub repo size](https://img.shields.io/github/repo-size/KC-85/Joystick_Journalist)](https://www.github.com/KC-85/Joystick_Journalist)

# Overview
Joystick Journalist is an interactive gaming review platform dedicated to 90s retro video games. It allows users to browse, review, and rate classic games, creating a community-driven archive of gaming nostalgia. 

The project aims to bring together retro gaming enthusiasts who want to share their experiences, rate games, and discuss their favorites from a golden era of gaming. By providing a structured platform for reviews, Joystick Journalist serves as a valuable resource for both long-time fans and newcomers eager to explore the classics.

# Target Audience
This platform is designed for retro gaming fans, gaming historians, and new players alike. Enthusiasts who grew up playing classic titles can relive their favorite moments and contribute by sharing their insights and reviews.

Gaming historians can use the platform to document and evaluate the impact of these legendary titles, while new players can discover highly rated classics based on community recommendations. By fostering an interactive and engaging environment, Joystick Journalist ensures that the legacy of these games continues to be celebrated.

# Purpose & Benefits
The primary goal of Joystick Journalist is to preserve gaming history through user-generated content. By allowing players to leave reviews and rate games, the platform builds a database of insights and opinions on some of the most iconic titles ever created.

Users benefit from community-driven ratings, which help highlight the best games from the 90s based on collective experiences. The platform also features an intuitive and easy-to-use review system, ensuring that players of all skill levels can contribute.

Designed with a responsive layout, it offers a seamless experience across both desktop and mobile devices. Additionally, user authentication and secure access ensure a safe and personalized experience for every member of the community.


**Site Mockups**
*([amiresponsive](https://ui.dev/amiresponsive?url=https://joystick-journalist-3eda94de87b5.herokuapp.com), [techsini](https://techsini.com/multi-mockup), etc.)*

![screenshot](documentation/mockup.png)

source: [Joystick_Journalist amiresponsive](https://ui.dev/amiresponsive?url=https://joystick-journalist-3eda94de87b5.herokuapp.com)

> [!IMPORTANT]
> The examples in these templates are strongly influenced by the Code Institute walkthrough project called "I Think Therefore I Blog".

## UX

### The 5 Planes of UX

#### 1. Strategy Plane
##### Purpose
- Provide site owners with tools to create, manage, and moderate engaging site content and user interactions.
- Offer users and guests an intuitive platform to explore, engage, and contribute to site discussions.

##### Primary User Needs
- Site owners need seamless tools for publishing and managing reviews.
- Registered users need the ability to engage with site content through reviews and account features.

##### Business Goals
- Foster a dynamic site platform with active user participation.
- Build a sense of community through user engagement.
- Ensure easy blog content management for owners.

#### 2. Scope Plane
##### Features
- A full list of [Features](#features) can be viewed in detail below.

##### Content Requirements
- Game and review management (create, read, update and delete).
- Review approval management tools.
- User account features (register, log in, edit/delete their own game and review additions).
- Notification system for comment approval status.
- 404 error page for lost users.

#### 3. Structure Plane
##### Information Architecture
- **Navigation Menu**:
  - Links to Home, Add review, View reviews, Login/Register, and Dashboard (for site owners).
- **Hierarchy**:
  - Site content displayed prominently for easy browsing.
  - Clear Hero Section and call-to-action buttons for account creation.
  

##### User Flow
1. Guest users see hero section with a call-to-action button, encouraging them to register for an account.
2. Guest users register for an account → log in to add games and/or reviews.
3. Registered users leave reviews → receive a pending approval notification.
4. Site owners manage review approval.
5. Site owners approve or reject reviews.

#### 4. Skeleton Plane
##### Wireframe Suggestions
- A full list of [Wireframes](#wireframes) can be viewed in detail below.

#### 5. Surface Plane
##### Visual Design Elements
- **[Colours](#colour-scheme)**: see below.
- **[Typography](#typography)**: see below.

### Colour Scheme

The Joystick Journalist platform embraces a retro-futuristic neon aesthetic, inspired by classic arcade gaming and cyberpunk themes.

The dark background enhances readability while allowing neon colors to pop, evoking the nostalgic feel of old CRT monitors and neon-lit arcades.

I used [coolors.co](https://coolors.co/000000-00ff00-ffcc00-ff00ff) to generate my color palette.
- `#000000` (Black) - Primary Background (Dark theme for retro aesthetic).
- `#00FF00` (Neon Green) - Primary Text & Borders (Glowing retro text effect).
- `#FFCC00` (Golden Yellow) - Hover Highlights (Interactive elements glow on hover).
- `#FF00FF` (Neon Purple) - Secondary Highlights (Accents and animated elements).

![screenshot](documentation/coolors.png)

### Typography

The primary font used in this project is VT323, a monospace font that gives the site a retro gaming aesthetic. It was imported from Google Fonts and applied site-wide to maintain a consistent theme.

- [VT323](https://fonts.google.com/specimen/VT323) was used for all text within the site in keeping with the 90s retro theme.

Instead of Font Awesome, the project utilizes Unicode symbols and emojis to represent interactive elements such as:
- Buttons and Navbar links.

- [ChatGPT] all icons within the site was generated via ChatGPT to represent interactive elements.

- [Montserrat](https://fonts.google.com/specimen/Montserrat) was used for the primary headers and titles.
- [Lato](https://fonts.google.com/specimen/Lato) was used for all other secondary text.
- [Font Awesome](https://fontawesome.com) icons were used throughout the site, such as the social media icons in the footer.

## User Stories

| Target | Expectation | Outcome |
| --- | --- | --- |
| As a site visitor/guest | I would like to see an introduction to the site (Hero Section) | so that I understand what the site is about before registering. |
| As a site visitor/guest | I would like to be able to register for a user account | so that I can access the game library and become a part of the game community. |
| As a registered user | I would like to login to the site | so that I can access my account and review the game library. |
| As a registered user | I would like to add a game | so that I can add a review in future. |
| As a registered user | I would like to see details for each game, such as genre and release year | so that I can get relevant information before reviewing. |
| As a registered user | I would like to add a game review | so that other users can determine whether to play a certain game or not. |
| As a registered user | I would like to update a game review i made | so that other site users can see the updated review in case of game updates. |
| As a registered user  | I would like to delete a game review that i made | so that I can clear irrelevant text content. |
| As a registered user | I would like to delete a game that i added | so that I can delete games that are no longer popular within the community. |
| As a site owner | I would like to edit or delete a user review | so that I can clean up or remove inappropriate responses after they've been posted. |
| As a registered user | I would like my comment to show my name and the timestamp | so that others can see who I am and when I left the review. |
| As a registered user | I would like to receive a notification or message saying my review is pending approval | so that I understand it hasn't been posted immediately. |
| As a registered user | I would like to edit or delete my own reviews | so that I can fix mistakes or retract my statement. |

| As a registered user | I would like to see a 404 error page if I get lost | so that it's obvious that I've stumbled upon a page that doesn't exist. |
| As a site owner | I would like to see a login error page | so that after a certain number of login attempts with the wrong credentials, i can be sure that the site is safe from brute-force login attempts |

## Wireframes

To follow best practice, wireframes were developed for mobile, tablet, and desktop sizes.
I've used [Visily](https://app.visily.ai/projects) to manually design my site wireframes.

| Page | Mobile | Tablet | Desktop |
| --- | --- | --- | --- |
| Hero Section | ![screenshot](documentation/wireframes/mobile_hero_section.png) | ![screenshot](documentation/wireframes/tablet_hero_section.png) | ![screenshot](documentation/wireframes/desktop_hero_section.png) |
| Register | ![screenshot](documentation/wireframes/mobile_register.png) | ![screenshot](documentation/wireframes/tablet_register.png) | ![screenshot](documentation/wireframes/desktop_register.png) |
| Login | ![screenshot](documentation/wireframes/mobile_login.png) | ![screenshot](documentation/wireframes/tablet_login.png) | ![screenshot](documentation/wireframes/desktop_login.png) |
| Landing Page | ![screenshot](documentation/wireframes/mobile_landing_page.png) | ![screenshot](documentation/wireframes/tablet_landing_page.png) | ![screenshot](documentation/wireframes/desktop_landing_page.png) |
| Add Game | ![screenshot](documentation/wireframes/mobile_add_game.png) | ![screenshot](documentation/wireframes/tablet_add_game.png) | ![screenshot](documentation/wireframes/desktop_add_game.png) |
| Add Review | ![screenshot](documentation/wireframes/mobile_add_review.png) | ![screenshot](documentation/wireframes/tablet_add_review.png) | ![screenshot](documentation/wireframes/desktop_add_review.png) |
| Edit Review | ![screenshot](documentation/wireframes/mobile_edit_review.png) | ![screenshot](documentation/wireframes/tablet_edit_review.png) | ![screenshot](documentation/wireframes/desktop_edit_review.png) |
| All Reviews | ![screenshot](documentation/wireframes/mobile_all_reviews.png) | ![screenshot](documentation/wireframes/tablet_all_reviews.png) | ![screenshot](documentation/wireframes/desktop_all_reviews.png) |
| Lockout Page | ![screenshot](documentation/wireframes/mobile_lockout_page.png) | ![screenshot](documentation/wireframes/tablet_lockout_page.png) | ![screenshot](documentation/wireframes/desktop_lockout_page.png) |
| 404 | ![screenshot](documentation/wireframes/mobile_404.png) | ![screenshot](documentation/wireframes/tablet_404.png) | ![screenshot](documentation/wireframes/desktop_404.png) |

## Features

### Existing Features

| Feature | Notes | Screenshot |
| --- | --- | --- |
| Register | Authentication is handled by Django-auth, allowing users to register accounts. | ![screenshot](documentation/features/register.png) |
| Login | Authentication is handled by Django-auth and Django-axes, allowing users to log in to their existing accounts with the correct credentials. | ![screenshot](documentation/features/login.png) |
| Logout | Authentication is handled by Django-auth, allowing users to log out of their accounts. | ![screenshot](documentation/features/logout.png) |
| Game List | The landing page displays basic information about games, including title and genre. | ![screenshot](documentation/features/landing_page_game_list.png) |
| Add Game | Superusers can add any 90s game of their choosing | ![screenshot](documentation/features/add_game.png) |
| Delete Game | Superusers can delete games, users can delete their own added games. | ![screenshot](documentation/features/delete_game.png) |
| Add Review | Authenticated users can review games. | ![screenshot](documentation/features/add_review.png) |
| Edit Review | Authenticated users can edit their own reviews. | ![screenshot](documentation/features/edit_review.png) |
| Delete Review | Authenticated users can delete their own reviews. | ![screenshot](documentation/features/delete_review.png) |
| Create Game | Site owners can create 90s games, all from the Django admin dashboard. | ![screenshot](documentation/features/create_game_admin.png) |
| Update Game | Site owners can update/manage blog posts from the Django admin dashboard. | ![screenshot](documentation/features/update_game_admin.png) |
| Delete Game | Site owners can delete games from the Django admin dashboard. | ![screenshot](documentation/features/delete_game_admin.png) |
| Create Review | Site owners can create reviews from the Django admin dashboard. | ![screenshot](documentation/features/create_review_admin.png) |
| Update Review | Site owners can update reviews from the Django admin dashboard. | ![screenshot](documentation/features/update_review_admin.png) |
| Delete Review | Site owners can delete reviews from the Django admin dashboard. | ![screenshot](documentation/features/delete_review_admin.png) |
| Create Genre | Site owners can create genres from the Django admin dashboard. | ![screenshot](documentation/features/create_genre_admin.png) |
| Update Genre | Site owners can update genres from the Django admin dashboard. | ![screenshot](documentation/features/update_genre_admin.png) |
| Delete Genre | Site owners can delete genres from the Django admin dashboard. | ![screenshot](documentation/features/delete_genre_admin.png) |
| User Feedback | Clear and obvious Django messages are used to provide feedback to user actions. | ![screenshot](documentation/features/messages.png) |
| Heroku Deployment | The site is fully deployed to Heroku, making it accessible online and easy to manage. | ![screenshot](documentation/features/heroku.png) |
| 404 | The 404 error page will indicate when a user has navigated to a page that doesn't exist, replacing the default Heroku 404 page with one that ties into the site's look and feel. | ![screenshot](documentation/features/404.png) |
| Site Lockout | The lockout page will indicate when a user has tried to log in with the wrong credentials three times in a row and to try again later. | ![screenshot](documentation/features/lockout_page.png) |

### Future Features

- **Two-Factor Authentication**: Allows users to login securely with either a one-time passcode or a QR Code.
- **Post Categories/Tags**: Allow users to categorize and tag games and reviews.
- **Post Search Functionality**: Add a search bar for users to quickly find posts by keywords or phrases.
- **Site Chat Function**: Implement the site chat function so that users are able to engage fully with one another.
- **Chat Room**: Create chat rooms for each game so that users can discuss certain aspects of a game.
- **Spam and Profanity Filter**: Makes sure that inappropriate conversations are deleted
- **Post Likes/Dislikes or Upvotes**: Implement a "like" or "upvote" system for blog posts to encourage user engagement and give feedback to the author.
- **User Profiles**: Create personalized user profiles where authenticated users can view their comments, liked posts, and basic account information.
- **Comment Replies & Threads**: Enable users to reply to comments, creating nested comment threads for better discussions.
- **Post Sharing**: Add social media sharing buttons (e.g., Twitter, Facebook, LinkedIn) for users to share blog posts.
- **Notifications**: Implement a notification system that alerts users when their comments are approved, when new comments are made on a post they've commented on, or when new posts are published.
- **Email Subscriptions**: Allow users to subscribe to receive email notifications for new posts, updates, or newsletters.
- **Post Analytics**: Provide post authors with analytics such as views, time spent reading, and engagement rates.
- **Multilingual Support**: Add the ability to write and view blog posts in multiple languages, broadening the audience.
- **Translator**: Users have the ability to translate posts that are not in their native language.
- **Related Posts Recommendations**: Show related posts at the bottom of a blog post to encourage further reading and keep users engaged.
- **Content Flagging/Reporting**: Allow users to flag or report inappropriate content (comments or posts) for moderation.
- **Add Regular Users as Chat Moderators**: Adds a larger sense of community being.
- **Add an AI Chatbot as a Moderator Bot**: To help with chat moderation once audience becomes large enough.
- **SEO Optimization**: Implement features for SEO, such as custom URLs for better search engine ranking.
- **User Dashboard**: Provide users with a dashboard to track their activity, such as comments made, likes received, and blog posts they’ve interacted with.
- **Admin Dashboard Analytics**: Provide site admins with an analytics dashboard showing user activity, popular posts, most commented articles, etc.
- **Custom Themes for Users**: Allow users to customize the visual theme of the site (colors, fonts, etc.) to suit their preferences.
- **Site Monitoring**: Allow site owner to monitor activity by way of using Prometheus/Grafana.
- **Bot Checker/Blocker**: Allow site owner to check for potential bots by way of standalone single site crawler/bot blocking software.
- **VPN Detection**: Allow site owner to use software to check/block IP addressess from known VPN providers.

## Tools & Technologies

| Tool / Tech | Use |
| --- | --- |
| [![badge](https://img.shields.io/badge/Markdown_Builder-grey?logo=markdown&logoColor=000000)](https://markdown.2bn.dev) | Generate README and TESTING templates. |
| [![badge](https://img.shields.io/badge/Git-grey?logo=git&logoColor=F05032)](https://git-scm.com) | Version control. (`git add`, `git commit`, `git push`) |
| [![badge](https://img.shields.io/badge/GitHub-grey?logo=github&logoColor=181717)](https://github.com) | Secure online code storage. |
| [![badge](https://img.shields.io/badge/Gitpod-grey?logo=gitpod&logoColor=FFAE33)](https://gitpod.io) | Cloud-based IDE for development. |
| [![badge](https://img.shields.io/badge/VSCode-grey?logo=htmx&logoColor=007ACC)](https://code.visualstudio.com) | Local IDE for development. |
| [![badge](https://img.shields.io/badge/HTML-grey?logo=html5&logoColor=E34F26)](https://en.wikipedia.org/wiki/HTML) | Main site content and layout. |
| [![badge](https://img.shields.io/badge/CSS-grey?logo=css3&logoColor=1572B6)](https://en.wikipedia.org/wiki/CSS) | Design and layout. |
| [![badge](https://img.shields.io/badge/JavaScript-grey?logo=javascript&logoColor=F7DF1E)](https://www.javascript.com) | User interaction on the site. |
| [![badge](https://img.shields.io/badge/Python-grey?logo=python&logoColor=3776AB)](https://www.python.org) | Back-end programming language. |
| [![badge](https://img.shields.io/badge/Heroku-grey?logo=heroku&logoColor=430098)](https://www.heroku.com) | Hosting the deployed back-end site. |
| [![badge](https://img.shields.io/badge/Bootstrap-grey?logo=bootstrap&logoColor=7952B3)](https://getbootstrap.com) | Front-end CSS framework for modern responsiveness and pre-built components. |
| [![badge](https://img.shields.io/badge/Django-grey?logo=django&logoColor=092E20)](https://www.djangoproject.com) | Python framework for the site. |
| [![badge](https://img.shields.io/badge/PostgreSQL-grey?logo=postgresql&logoColor=4169E1)](https://www.postgresql.org) | Relational database management. |
| [![badge](https://img.shields.io/badge/WhiteNoise-grey?logo=python&logoColor=FFFFFF)](https://whitenoise.readthedocs.io) | Serving static files with Heroku. |
| [![badge](https://img.shields.io/badge/Font_Awesome-grey?logo=fontawesome&logoColor=528DD7)](https://fontawesome.com) | Icons. |
| [![badge](https://img.shields.io/badge/ChatGPT-grey?logo=openai&logoColor=75A99C)](https://chat.openai.com) | Help debug, troubleshoot, and explain things. |

## Database Design

### Data Model

Entity Relationship Diagrams (ERD) help to visualize database architecture before creating models. Understanding the relationships between different tables can save time later in the project.

![screenshot](documentation/erd/erd_diagram.png)

I have used `Mermaid` to generate an interactive ERD of my project.

```mermaid
erDiagram
    USER ||--o{ REVIEW : writes
    GENRE ||--o{ GAME : includes
    GAME ||--o{ REVIEW : has

    USER {
        int id
        string username
    }

    GENRE {
        int id
        string name
    }

    GAME {
        int id
        string title
        int release_year
        int genre_id
    }

    REVIEW {
        int id
        int game_id
        int reviewer_name_id
        int rating
        text comment
        datetime review_date
    }
```

source: [Mermaid](https://mermaid.live/edit#pako:eNqFUltvgjAU_ivkPKNRwAJ9WzZi9rA9aLYlCwlp4AybQTGlTB3y31duOhcz-9Tz3c7HpYa4SBAooHzgLJUsD4Whz8s6WBnH42RS1MYqeH0M3gxq7CRXWPaCZfC8CkbF8u4p0DwXcVYlJ0UL_o3YMM3-WlH39_ZwoQyenOdSSS5SoypRCpZjTzSju99_237N2ha77VRcZXipkpghKzE6IJOXTIpCYjSmnFYNz_3Pss6sO0Z_QYlfHHcoI3GVZUp3PGMK98qIizxHoc5owhQqnuMQFrXzqSGYkKPMGU_05-8ahqA2qF8XUH1NmPwMIRSN1rFKFeuDiIEqWaEJ1bZNGn6YEdwyAbSGPVDfmdo2sRYLmxDHmbueCQeghEw94hFiuxZx_PnMb0z4Lgrtn029hUt8x7Zcz55bxLO7tPeO7MNlUaUboB8sK_WUyrb0wKBIUN4XlVB6c_MDrhDUhA)


I have used `pygraphviz` and `django-extensions` to auto-generate an ERD.

The steps taken were as follows:
- In the terminal: `sudo apt update`
- then: `sudo apt-get install python3-dev graphviz libgraphviz-dev pkg-config`
- then type `Y` to proceed
- then: `pip3 install django-extensions pygraphviz`
- in my `settings.py` file, I added the following to my `INSTALLED_APPS`:
```python
INSTALLED_APPS = [
    ...
    'django_extensions',
    ...
]
```
- back in the terminal: `python3 manage.py graph_models -a -o erd.png`
- drag the new `erd.png` file into my `documentation/` folder
- removed `'django_extensions',` from my `INSTALLED_APPS`
- finally, in the terminal: `pip3 uninstall django-extensions pygraphviz -y`

![screenshot](documentation/advanced-erd.png)

source: [medium.com](https://medium.com/@yathomasi1/1-using-django-extensions-to-visualize-the-database-diagram-in-django-application-c5fa7e710e16)

## Agile Development Process

### GitHub Projects

[GitHub Projects](https://www.github.com/KC-85/Joystick_Journalist/projects) served as an Agile tool for this project. Through it, EPICs, User Stories, issues/bugs, and Milestone tasks were planned, then subsequently tracked on a regular basis using the Kanban project board.

![screenshot](documentation/github/gh_projects.png)

### GitHub Issues

[GitHub Issues](https://www.github.com/KC-85/Joystick_Journalist/issues) served as an another Agile tool. There, I managed my User Stories and Milestone tasks, and tracked any issues/bugs.

| Link | Screenshot |
| --- | --- |
| [![GitHub issues](https://img.shields.io/github/issues/KC-85/Joystick_Journalist)](https://www.github.com/KC-85/Joystick_Journalist/issues) | ![screenshot](documentation/github/gh_issues_open_png) |
| [![GitHub closed issues](https://img.shields.io/github/issues-closed/KC-85/Joystick_Journalist)](https://www.github.com/KC-85/Joystick_Journalist/issues?q=is%3Aissue+is%3Aclosed) | ![screenshot](documentation/github/gh_issues_closed.png) |

### MoSCoW Prioritization

I've decomposed my Epics into User Stories for prioritizing and implementing them. Using this approach, I was able to apply "MoSCow" prioritization and labels to my User Stories within the Issues tab.

- **Must Have**: guaranteed to be delivered - required to Pass the project (*max ~60% of stories*)
- **Should Have**: adds significant value, but not vital (*~20% of stories*)
- **Could Have**: has small impact if left out (*the rest ~20% of stories*)
- **Won't Have**: not a priority for this iteration - future features

## Testing

> [!NOTE]
> For all testing, please refer to the [TESTING.md](TESTING.md) file.

## Deployment

The live deployed application can be found deployed on [Heroku](https://joystick-journalist-3eda94de87b5.herokuapp.com).

### Heroku Deployment

This project uses [Heroku](https://www.heroku.com), a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud.

Deployment steps are as follows, after account setup:

- Select **New** in the top-right corner of your Heroku Dashboard, and select **Create new app** from the dropdown menu.
- Your app name must be unique, and then choose a region closest to you (EU or USA), then finally, click **Create App**.
- From the new app **Settings**, click **Reveal Config Vars**, and set your environment variables to match your private `env.py`|`.env` file.

> [!IMPORTANT]
> This is a sample only; you would replace the values with your own if cloning/forking my repository.

| Key | Value |
| --- | --- |
| `ALLOWED_HOSTS` | user-inserts-own-allowed-hosts |
| `CSRF_TRUSTED_ORIGINS` | user-inserts-own-trusted-origins |
| `DATABASE_URL` | user-inserts-own-postgres-database-url |
| `DISABLE_COLLECTSTATIC` | 1 (*this is temporary, and can be removed for the final deployment*) |
| `SECRET_KEY` | any-random-secret-key |

Heroku needs some additional files in order to deploy properly.

- [requirements.txt](requirements.txt)
- [Procfile](Procfile)

You can install this project's **[requirements.txt](requirements.txt)** (*where applicable*) using:

- `pip3 install -r requirements.txt`
- `pip install -r requirements.txt`

If you have your own packages that have been installed, then the requirements file needs updated using:

- `pip3 freeze --local > requirements.txt`
- `pip freeze --local > requirements.txt`

The **[Procfile](Procfile)** can be created with the following command:

- `echo web: gunicorn app_name.wsgi > Procfile`
- *replace `app_name` with the name of your primary Django app name; the folder where `settings.py` is located*

For Heroku deployment, follow these steps to connect your own GitHub repository to the newly created app:

Either (*recommended*):

- Select **Automatic Deployment** from the Heroku app.

Or:

- In the Terminal/CLI, connect to Heroku using this command: `heroku login -i`
- Set the remote for Heroku: `heroku git:remote -a app_name` (*replace `app_name` with your app name*)
- After performing the standard Git `add`, `commit`, and `push` to GitHub, you can now type:
	- `git push heroku main`

The project should now be connected and deployed to Heroku!

### PostgreSQL

This project uses a [Code Institute PostgreSQL Database](https://dbs.ci-dbs.net) for the Relational Database with Django.

> [!CAUTION]
> - PostgreSQL databases by Code Institute are only available to CI Students.
> - You must acquire your own PostgreSQL database through some other method if you plan to clone/fork this repository.
> - Code Institute students are allowed a maximum of 8 databases.
> - Databases are subject to deletion after 18 months.

To obtain my own Postgres Database from Code Institute, I followed these steps:

- Submitted my email address to the CI PostgreSQL Database link above.
- An email was sent to me with my new Postgres Database.
- The Database connection string will resemble something like this:
    - `postgres://<db_username>:<db_password>@<db_host_url>/<db_name>`
- You can use the above URL with Django; simply paste it into your `env.py`|`.env` file and Heroku Config Vars as `DATABASE_URL`.

### WhiteNoise

This project uses the [WhiteNoise](https://whitenoise.readthedocs.io/en/latest/) to aid with static files temporarily hosted on the live Heroku site.

To include WhiteNoise in your own projects:

- Install the latest WhiteNoise package:
    - `pip install whitenoise`
- Update the `requirements.txt` file with the newly installed package:
    - `pip freeze --local > requirements.txt`
- Edit your `settings.py` file and add WhiteNoise to the `MIDDLEWARE` list, above all other middleware (apart from Django’s "SecurityMiddleware"):

```python
# settings.py

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    # any additional middleware
]
```


### Local Development

This project can be cloned or forked in order to make a local copy on your own system.

For either method, you will need to install any applicable packages found within the [requirements.txt](requirements.txt) file.

- `pip3 install -r requirements.txt`.

You will need to create a new file called `env.py` or `.env` at the root-level, and include the same environment variables listed above from the Heroku deployment steps.

> [!IMPORTANT]
> This is a sample only; you would replace the values with your own if cloning/forking my repository.

Sample `env.py`|`.env` file:

```python
import os

os.environ.setdefault("SECRET_KEY", "any-random-secret-key")
os.environ.setdefault("DATABASE_URL", "user-inserts-own-postgres-database-url")

# local environment only (do not include these in production/deployment!)
os.environ.setdefault("DEBUG", "True")
```

Once the project is cloned or forked, in order to run it locally, you'll need to follow these steps:

- Start the Django app: `python3 manage.py runserver`
- Stop the app once it's loaded: `CTRL+C` (*Windows/Linux*) or `⌘+C` (*Mac*)
- Make any necessary migrations: `python3 manage.py makemigrations --dry-run` then `python3 manage.py makemigrations`
- Migrate the data to the database: `python3 manage.py migrate --plan` then `python3 manage.py migrate`
- Create a superuser: `python3 manage.py createsuperuser`
- Load fixtures (*if applicable*): `python3 manage.py loaddata file-name.json` (*repeat for each file*)
- Everything should be ready now, so run the Django app again: `python3 manage.py runserver`

If you'd like to backup your database models, use the following command for each model you'd like to create a fixture for:

- `python3 manage.py dumpdata your-model > your-model.json`
- *repeat this action for each model you wish to backup*
- **NOTE**: You should never make a backup of the default *admin* or *users* data with confidential information.

#### Cloning

You can clone the repository by following these steps:

1. Go to the [GitHub repository](https://www.github.com/KC-85/Joystick_Journalist).
2. Locate and click on the green "Code" button at the very top, above the commits and files.
3. Select whether you prefer to clone using "HTTPS", "SSH", or "GitHub CLI", and click the "copy" button to copy the URL to your clipboard.
4. Open "Git Bash" or "Terminal".
5. Change the current working directory to the location where you want the cloned directory.
6. In your IDE Terminal, type the following command to clone the repository:
	- `git clone https://www.github.com/KC-85/Joystick_Journalist.git`
7. Press "Enter" to create your local clone.

Alternatively, if using Gitpod, you can click below to create your own workspace using this repository.

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://www.github.com/KC-85/Joystick_Journalist)

**Please Note**: in order to directly open the project in Gitpod, you should have the browser extension installed. A tutorial on how to do that can be found [here](https://www.gitpod.io/docs/configure/user-settings/browser-extension).

#### Forking

By forking the GitHub Repository, you make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original owner's repository. You can fork this repository by using the following steps:

1. Log in to GitHub and locate the [GitHub Repository](https://www.github.com/KC-85/Joystick_Journalist).
2. At the top of the Repository, just below the "Settings" button on the menu, locate and click the "Fork" Button.
3. Once clicked, you should now have a copy of the original repository in your own GitHub account!

### Local VS Deployment

There are no remaining major differences between the local version when compared to the deployed version online.

## Credits

### Content

| Source | Notes |
| --- | --- |
| [Markdown Builder](https://markdown.2bn.dev) | Help generating Markdown files |
| [Chris Beams](https://chris.beams.io/posts/git-commit) | "How to Write a Git Commit Message" |
| [I Think Therefore I Blog](https://codeinstitute.net) | Code Institute walkthrough project inspiration |
| [Bootstrap](https://getbootstrap.com) | Various components / responsive front-end framework |
| [Whitenoise](https://whitenoise.readthedocs.io) | Static file service |
| [Python Tutor](https://pythontutor.com) | Additional Python help |
| [ChatGPT](https://chatgpt.com) | Help with code logic and explanations |
| [Udemy](https://www.udemy.com/course/python-django-the-practical-guide/) | Help with the more intricate sections of Django |

### Media

| Source | Notes |
| --- | --- |
| [ChatGPT](https://chatgpt.com) | Icons used throughout the site |


### Acknowledgements

- I would like to thank my Code Institute mentor, [Tim Nelson](https://www.github.com/TravelTimN) for the support & answers to my questions throughout the development of this project.
- I would like to thank the [Code Institute](https://codeinstitute.net) Tutor Team for their assistance with troubleshooting and debugging some project issues.
- I would like to thank the [Code Institute Slack community](https://code-institute-room.slack.com) for the moral support; it kept me going during periods of self doubt and impostor syndrome.
- I would like to thank all of my friends and my good friend & flatmate, Janet for believing in me, and allowing me to make this transition into software development.
- I would like to thank my employer, for supporting me in my career development change towards becoming a software developer.
- I would like to thank Tutor Support for their support and assistance with this project.


