# Testing

> [!NOTE]
> Return back to the [README.md](README.md) file.

## Code Validation

### HTML

🛑 IMPORTANT 🛑

RE: Python/Jinja syntax in HTML

Python projects that use Jinja syntax, such as `{% for loops %}`, `{% url 'home' %}`, and `{{ variable|filter }}` will not validate properly if you're copying/pasting into the HTML validator.

In order to properly validate these types of files, it's recommended to [validate by uri](https://validator.w3.org/#validate_by_uri) from the deployed Heroku pages.

Unfortunately, pages that require a user to be "logged-in" and authenticated (CRUD functionality) will not work using this method, due to the fact that the HTML Validator (W3C) doesn't have access to login to an account on your project. In order to properly validate HTML pages with Jinja syntax for authenticated pages, follow these steps:

- Navigate to the deployed pages which require authentication.
- Right-click anywhere on the page, and select **View Page Source** (usually `CTRL+U` or `⌘+U` on Mac).
- This will display the entire "compiled" code, without any Jinja syntax.
- Copy everything, and use the [validate by input](https://validator.w3.org/#validate_by_input) method.
- Repeat this process for every page that requires a user to be logged-in/authenticated (e.g.: CRUD functionality).

🛑 ---- END --- 🛑

I have used the recommended [HTML W3C Validator](https://validator.w3.org) to validate all of my HTML files.

| Directory | File | URL | Screenshot | Notes |
| --- | --- | --- | --- | --- |
| reviews | [all_reviews.html](https://github.com/KC-85/Joystick_Journalist/blob/main/reviews/templates/reviews/all_reviews.html) | Link (if applicable) | ![screenshot](documentation/validation/html-reviews-all_reviews.png) | Note: Delete review shows in the compiled HTML. |
| reviews | [form_page.html](https://github.com/KC-85/Joystick_Journalist/blob/main/reviews/templates/reviews/form_page.html) | Link (if applicable) | ![screenshot](documentation/validation/html-reviews-form_page.png) | Note: This template is for adding games. |
| reviews | [hero.html](https://github.com/KC-85/Joystick_Journalist/blob/main/reviews/templates/reviews/hero.html) | Link (if applicable) | ![screenshot](documentation/validation/html-reviews-hero.png) | Notes (if applicable) |
| reviews | [landing_page.html](https://github.com/KC-85/Joystick_Journalist/blob/main/reviews/templates/reviews/landing_page.html) | Link (if applicable) | ![screenshot](documentation/validation/html-reviews-landing_page.png) | Note: Add review shows in the compiled HTML. |
| reviews | [login.html](https://github.com/KC-85/Joystick_Journalist/blob/main/reviews/templates/reviews/login.html) | Link (if applicable) | ![screenshot](documentation/validation/html-reviews-login.png) | Notes (if applicable) |
| reviews | [register.html](https://github.com/KC-85/Joystick_Journalist/blob/main/reviews/templates/reviews/register.html) | Link (if applicable) | ![screenshot](documentation/validation/html-reviews-register.png) | Notes (if applicable) |
| reviews | [lockout.html](https://github.com/KC-85/Joystick_Journalist/blob/main/reviews/templates/reviews/lockout.html) | Link (if applicable) | ![screenshot](documentation/validation/html-reviews-lockout.png) | Notes (if applicable) |


### CSS

I have used the recommended [CSS Jigsaw Validator](https://jigsaw.w3.org/css-validator) to validate all of my CSS files.

| Directory | File | URL | Screenshot | Notes |
| --- | --- | --- | --- | --- |
| reviews | [style.css](https://github.com/KC-85/Joystick_Journalist/blob/main/reviews/static/css/style.css) | Link (if applicable) | ![screenshot](documentation/validation/css-reviews-style.png) | Notes (if applicable) |


### JavaScript

I have used the recommended [JShint Validator](https://jshint.com) to validate all of my JS files.

| Directory | File | URL | Screenshot | Notes |
| --- | --- | --- | --- | --- |
| reviews | [main.js](https://github.com/KC-85/Joystick_Journalist/blob/main/reviews/static/js/main.js) | N/A | ![screenshot](documentation/validation/js-reviews-main.png) | Notes (if applicable) |


### Python

🛑 IMPORTANT 🛑

**IMPORTANT**: Django settings

The Django `settings.py` file comes with 4 lines that are quite long, and will throw the `E501 line too long` error. This is default behavior, but can be fixed by adding the "`  # noqa`" comment at the end of those lines.

```python
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",  # noqa
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",  # noqa
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",  # noqa
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",  # noqa
    },
]
```

**IMPORTANT**: *migration* and *pycache* files

You do not have to validate files from the `migrations/` or `pycache/` folders! Ignore these `.py` files, and validate just the files that you've created or modified.

🛑 --- END --- 🛑

I have used the recommended [PEP8 CI Python Linter](https://pep8ci.herokuapp.com) to validate all of my Python files.

| Directory | File | URL | Screenshot | Notes |
| --- | --- | --- | --- | --- |
| core | [settings.py](https://github.com/KC-85/Joystick_Journalist/blob/main/core/settings.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/KC-85/Joystick_Journalist/main/core/settings.py) | ![screenshot](documentation/validation/py-core-settings.png) | Where it shows validation errors for *Password Validation* in settings.py, these cannot be fixed by just separating the line with brackets/parentheses, as this would cause the validated code to not function properly, hence **#noqa** |
| core | [urls.py](https://github.com/KC-85/Joystick_Journalist/blob/main/core/urls.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/KC-85/Joystick_Journalist/main/core/urls.py) | ![screenshot](documentation/validation/py-core-urls.png) | Notes (if applicable) |
| root directory | [manage.py](https://github.com/KC-85/Joystick_Journalist/blob/main/manage.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/KC-85/Joystick_Journalist/main/manage.py) | ![screenshot](documentation/validation/py--manage.png) | Notes (if applicable) |
| reviews | [admin.py](https://github.com/KC-85/Joystick_Journalist/blob/main/reviews/admin.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/KC-85/Joystick_Journalist/main/reviews/admin.py) | ![screenshot](documentation/validation/py-reviews-admin.png) | Notes (if applicable) |
| reviews | [forms.py](https://github.com/KC-85/Joystick_Journalist/blob/main/reviews/forms.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/KC-85/Joystick_Journalist/main/reviews/forms.py) | ![screenshot](documentation/validation/py-reviews-forms.png) | Notes (if applicable) |
| reviews | [login_middleware.py](https://github.com/KC-85/Joystick_Journalist/blob/main/reviews/login_middleware.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/KC-85/Joystick_Journalist/main/reviews/login_middleware.py) | ![screenshot](documentation/validation/py-reviews-login_middleware.png) | Notes (if applicable) |
| reviews | [models.py](https://github.com/KC-85/Joystick_Journalist/blob/main/reviews/models.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/KC-85/Joystick_Journalist/main/reviews/models.py) | ![screenshot](documentation/validation/py-reviews-models.png) | Notes (if applicable) |
| reviews | [urls.py](https://github.com/KC-85/Joystick_Journalist/blob/main/reviews/urls.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/KC-85/Joystick_Journalist/main/reviews/urls.py) | ![screenshot](documentation/validation/py-reviews-urls.png) | Notes (if applicable) |
| reviews | [views.py](https://github.com/KC-85/Joystick_Journalist/blob/main/reviews/views.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/KC-85/Joystick_Journalist/main/reviews/views.py) | ![screenshot](documentation/validation/py-reviews-views.png) | Notes (if applicable) |


## Responsiveness


I've tested my deployed project to check for responsiveness issues.

| Page | Mobile | Tablet | Desktop | Notes |
| --- | --- | --- | --- | --- |
| Register | ![screenshot](documentation/responsiveness/mobile_register.png) | ![screenshot](documentation/responsiveness/tablet_register.png) | ![screenshot](documentation/responsiveness/desktop_register.png) | Works as expected |
| Login | ![screenshot](documentation/responsiveness/mobile_login.png) | ![screenshot](documentation/responsiveness/tablet_login.png) | ![screenshot](documentation/responsiveness/desktop_login.png) | Works as expected |
| Landing Page | ![screenshot](documentation/responsiveness/mobile_landing_page.png) | ![screenshot](documentation/responsiveness/tablet_landing_page.png) | ![screenshot](documentation/responsiveness/desktop_landing_page.png) | Works as expected |
| Add Game | ![screenshot](documentation/responsiveness/mobile_add_game.png) | ![screenshot](documentation/responsiveness/tablet_add_game.png) | ![screenshot](documentation/responsiveness/desktop_add_game.png) | Works as expected |
| Add Review | ![screenshot](documentation/responsiveness/mobile_add_review.png) | ![screenshot](documentation/responsiveness/tablet_add_review.png) | ![screenshot](documentation/responsiveness/desktop_add_review.png) | Works as expected |
| Edit Review | ![screenshot](documentation/responsiveness/mobile_edit_review.png) | ![screenshot](documentation/responsiveness/tablet_edit_review.png) | ![screenshot](documentation/responsiveness/desktop_edit_review.png) | Works as expected |
| All Reviews | ![screenshot](documentation/responsiveness/mobile_all_reviews.png) | ![screenshot](documentation/responsiveness/tablet_all_reviews.png) | ![screenshot](documentation/responsiveness/desktop_all_reviews.png) | Works as expected |
| 404 | ![screenshot](documentation/responsiveness/mobile-404.png) | ![screenshot](documentation/responsiveness/tablet-404.png) | ![screenshot](documentation/responsiveness/desktop-404.png) | Works as expected |

## Browser Compatibility

I've tested my deployed project on multiple browsers to check for compatibility issues.

| Page | Chrome | Firefox | Brave | Notes |
| --- | --- | --- | --- | --- |
| Hero Page | ![screenshot](documentation/browsers/chrome-hero.png) | ![screenshot](documentation/browsers/firefox-hero.png) | ![screenshot](documentation/browsers/brave-hero.png) | Works as expected |
| Register | ![screenshot](documentation/browsers/chrome-register.png) | ![screenshot](documentation/browsers/firefox-register.png) | ![screenshot](documentation/browsers/brave-register.png) | Works as expected |
| Login | ![screenshot](documentation/browsers/chrome-login.png) | ![screenshot](documentation/browsers/firefox-login.png) | ![screenshot](documentation/browsers/brave-login.png) | Works as expected |
| Landing Page | ![screenshot](documentation/browsers/chrome-landing_page.png) | ![screenshot](documentation/browsers/firefox-landing_page.png) | ![screenshot](documentation/browsers/brave-landing_page.png) | Works as expected |
| Add Game | ![screenshot](documentation/browsers/chrome-add-game.png) | ![screenshot](documentation/browsers/firefox-add-game.png) | ![screenshot](documentation/browsers/brave-add-game.png) | Works as expected |
| Add Review | ![screenshot](documentation/browsers/chrome-add-review.png) | ![screenshot](documentation/browsers/firefox-add-review.png) | ![screenshot](documentation/browsers/brave-add-review.png) | Works as expected |
| Edit Review | ![screenshot](documentation/browsers/chrome-edit-review.png) | ![screenshot](documentation/browsers/firefox-edit-review.png) | ![screenshot](documentation/browsers/brave-edit-review.png) | Works as expected |
| 404 | ![screenshot](documentation/browsers/chrome-404.png) | ![screenshot](documentation/browsers/firefox-404.png) | ![screenshot](documentation/browsers/brave-404.png) | Works as expected |

## Lighthouse Audit

I've tested my deployed project using the Lighthouse Audit tool to check for any major issues. Some warnings are outside of my control, and mobile results tend to be lower than desktop.

| Page | Mobile | Desktop |
| --- | --- | --- |
| Hero | ![screenshot](documentation/lighthouse/mobile/hero_section.png) | ![screenshot](documentation/lighthouse/desktop/hero_section.png) |
| Login | ![screenshot](documentation/lighthouse/mobile/login.png) | ![screenshot](documentation/lighthouse/desktop/login.png) |
| Register | ![screenshot](documentation/lighthouse/mobile/register.png) | ![screenshot](documentation/lighthouse/desktop/register.png) |
| Landing Page (Game List) | ![screenshot](documentation/lighthouse/mobile/landing_page.png) | ![screenshot](documentation/lighthouse/desktop/landing_page.png) |
| Add Game | ![screenshot](documentation/lighthouse/mobile/add_game.png) | ![screenshot](documentation/lighthouse/desktop/add_game.png) |
| Add Review | ![screenshot](documentation/lighthouse/mobile/add_review.png) | ![screenshot](documentation/lighthouse/desktop/add_review.png) |
| Edit Review | ![screenshot](documentation/lighthouse/mobile/edit_review.png) | ![screenshot](documentation/lighthouse/desktop/edit_review.png) |
| All Reviews | ![screenshot](documentation/lighthouse/mobile/all_reviews.png) | ![screenshot](documentation/lighthouse/desktop/all_reviews.png) |
| 404 | ![screenshot](documentation/lighthouse/mobile/404.png) | ![screenshot](documentation/lighthouse/desktop/404.png) |

- **Note:** Delete Review shows up a pop up message instead of a seperate page, and therefore I am unable to test it's lighthouse score.

## Defensive Programming


Defensive programming was manually tested with the below user acceptance testing:

| Page | Expectation | Test | Result | Screenshot |
| --- | --- | --- | --- | --- |
| Registration | Users cannot submit an empty registration form | Attempted to submit empty registration form | Blocked with validation messages | ![screenshot](documentation/defensive/register-empty.png) |
| Login | Users cannot login with invalid credentials | Attempted login with incorrect password | Login denied with error | ![screenshot](documentation/defensive/login-invalid.png) |
| Axes Lockout | Lock user after 3 failed login attempts | Entered wrong password 3 times | Lockout page displayed | ![screenshot](documentation/defensive/lockout.png) |
| Add Review | Guest users cannot create reviews | Tried to access add review URL as guest | Redirected to login | ![screenshot](documentation/defensive/add-review-guest.png) |
| Edit Review | Users cannot edit another user’s review | Logged in as User-B and attempted to edit User-A review | Review button does not come up on another users review | ![screenshot](documentation/defensive/edit-review-denied.png) |
| Delete Review | Users cannot delete another user’s review | Logged in as User-B and attempted delete User-A review | Delete button does not come up on another users review | ![screenshot](documentation/defensive/delete-review-denied.png) |
| Add Game | Only superusers can add new games | Logged in as standard user and attempted access | Hidden UI | ![screenshot](documentation/defensive/add-game-denied.png) |
| Admin Area | Standard users cannot access Django admin | Attempted to access `/admin` as standard user | Access denied / redirected | ![screenshot](documentation/defensive/admin-denied.png) |
| 404 Error Page | Invalid URLs show custom 404 page | Navigated to invalid URL | Custom 404 displayed | ![screenshot](documentation/defensive/404.png) |


## User Story Testing

| Target | Expectation | Outcome | Screenshot |
| --- | --- | --- | --- |
| As a site visitor/guest | I would like to see an introduction to the site (Hero Section) | Pass | ![screenshot](documentation/features/landing_page_game_list.png) |
| As a site visitor/guest | I would like to be able to register for a user account | Pass | ![screenshot](documentation/features/register.png) |
| As a registered user | I would like to login to the site | Pass | ![screenshot](documentation/features/login.png) |
| As a registered user | I would like to add a game | Pass | ![screenshot](documentation/features/add_game.png) |
| As a registered user | I would like to see details for each game, such as genre and release year | Pass | ![screenshot](documentation/features/landing_page_game_list.png) |
| As a registered user | I would like to add a game review | Pass | ![screenshot](documentation/features/add_review.png) |
| As a registered user | I would like to update a game review i made | Pass | ![screenshot](documentation/features/edit_review.png) |
| As a registered user  | I would like to delete a game review that i made | Pass | ![screenshot](documentation/features/delete_review.png) |
| As a registered user | I would like to delete a game that i added | Pass | ![screenshot](documentation/features/delete_game.png) |
| As a site owner | I would like to edit or delete a user review | Pass | ![screenshot](documentation/features/update_review_admin.png) |
| As a registered user | I would like my comment to show my name | Pass | ![screenshot](documentation/features/all_reviews.png) |
| As a registered user | I would like to edit or delete my own reviews | Pass | ![screenshot](documentation/features/edit_review.png) |
| As a registered user | I would like to see a 404 error page if I get lost | Pass | ![screenshot](documentation/features/404.png) |
| As a site owner | I would like to see a login error page | Pass | ![screenshot](documentation/features/lockout_page.png) |


## Automated Testing

I have conducted a series of automated tests on my application.

> [!NOTE]
> I fully acknowledge and understand that, in a real-world scenario, an extensive set of additional tests would be more comprehensive.

### Python (Unit Testing)

I have used Django's built-in unit testing framework to test the application functionality. In order to run the tests, I ran the following command in the terminal each time:

- `python3 manage.py test name-of-app`

To create the coverage report, I would then run the following commands:

- `pip3 install coverage`
- `pip3 freeze --local > requirements.txt`
- `pip freeze > requirements.txt`
- `coverage run manage.py test`
- `coverage report`

To see the HTML version of the reports, and find out whether some pieces of code were missing, I ran the following commands:

- `coverage html`
- `coverage run --source+'.' manage.py test`
- `coverage report -m`

Below are the results from the full coverage report on my application that I've tested:

![screenshot](documentation/automation/html-coverage.png)

#### Unit Test Issues

- No issues with unit testing.

## Bugs

- Please see **[Issues](https://www.github.com/KC-85/Joystick_Journalist/issues)** for bugs.

### Fixed Bugs

[![GitHub issue custom search](https://img.shields.io/github/issues-search?query=repo%3AKC-85%2FJoystick_Journalist%20label%3Abug&label=bugs)](https://www.github.com/KC-85/Joystick_Journalist/issues?q=is%3Aissue+is%3Aclosed+label%3Abug)

I've used [GitHub Issues](https://www.github.com/KC-85/Joystick_Journalist/issues) to track and manage bugs and issues during the development stages of my project.

All previously closed/fixed bugs can be tracked [here](https://www.github.com/KC-85/Joystick_Journalist/issues?q=is%3Aissue+is%3Aclosed+label%3Abug).

![screenshot](documentation/bugs/gh-issues-closed.png)

### Unfixed Bugs

- All known bugs are fixed.

[![GitHub issues](https://img.shields.io/github/issues/KC-85/Joystick_Journalist)](https://www.github.com/KC-85/Joystick_Journalist/issues)

Any remaining open issues can be tracked [here](https://www.github.com/KC-85/Joystick_Journalist/issues).

![screenshot](documentation/bugs/gh-issues-open.png)

### Known Issues

- There are no known issues.

> [!IMPORTANT]
> There are no remaining bugs that I am aware of, though, even after thorough testing, I cannot rule out the possibility.

