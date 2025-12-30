# Testing

> [!NOTE]
> Return back to the [README.md](README.md) file.

⚠️ INSTRUCTIONS ⚠️

In the following sections, you need to convince the assessors that you have conducted enough manual testing to legitimately believe that the site works well. Essentially, in this part, you should go over all of your project's features, and ensure that they all work as intended, with the project providing an easy and straightforward way for the users to achieve their goals.

⚠️ --- END --- ⚠️

## Code Validation

⚠️ INSTRUCTIONS ⚠️

Use the space below to discuss code validation for all of your own code files (*where applicable*). You are not required to validate external libraries/frameworks.

**MANDATORY**: You must provide a screenshot for each file you validate.

**PRO TIP**: Where possible, always validate the live URL pages/files, not your local code using copy/paste. There could be subtle/hidden differences.

⚠️ --- END --- ⚠️

### HTML

⚠️ INSTRUCTIONS ⚠️

1. [*recommended*] If you are using the live deployed site URLs, validate using this link: https://validator.w3.org/#validate_by_uri
2. Otherwise, if you are copying/pasting your HTML code manually, use this link: https://validator.w3.org/#validate_by_input

It's recommended to validate the live pages (all of them) using the deployed URL. This will give you a custom URL as well, which you can use below on your testing documentation. It makes it easier to return back to a page for validating it again in the future. The URL will look something like this:

- https://validator.w3.org/nu/?doc=https://KC-85.github.io/Joystick_Journalist/index.html

⚠️ --- END --- ⚠️

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

⚠️ INSTRUCTIONS ⚠️

1. [*recommended*] If you are using the live deployed site, use this link: https://jigsaw.w3.org/css-validator/#validate_by_uri
2. If you are copying/pasting your CSS code, use this link: https://jigsaw.w3.org/css-validator/#validate_by_input

It's recommended to validate the live site for your primary CSS file on the deployed URL. This will give you a custom URL as well, which you can use below on your testing documentation. It makes it easier to return back to a page for validating it again in the future. The URL will look something like this:

- https://jigsaw.w3.org/css-validator/validator?uri=https://joystick-journalist-3eda94de87b5.herokuapp.com

If you have additional/multiple CSS files, then individual "[validation by input](https://jigsaw.w3.org/css-validator/#validate_by_input)" is recommended for the extra CSS files.

**IMPORTANT**: Third-Party tools

If you're using external libraries/frameworks (e.g: Bootstrap, Materialize, Font Awesome, etc.), then sometimes the tool will attempt to also validate these, even though it's not part of your own actual code that you wrote. You are not required to validate the external libraries or frameworks!

⚠️ --- END --- ⚠️

I have used the recommended [CSS Jigsaw Validator](https://jigsaw.w3.org/css-validator) to validate all of my CSS files.

| Directory | File | URL | Screenshot | Notes |
| --- | --- | --- | --- | --- |
| reviews | [style.css](https://github.com/KC-85/Joystick_Journalist/blob/main/reviews/static/css/style.css) | Link (if applicable) | ![screenshot](documentation/validation/css-reviews-style.png) | Notes (if applicable) |


### JavaScript

⚠️ INSTRUCTIONS ⚠️

If using modern JavaScript (ES6) methods, then make sure to include the following line at the very top of every single JavaScript file in your project (this should remain in your files for submission as well):

`/* jshint esversion: 11 */`

If you are also including jQuery (`$`), then the updated format will be:

`/* jshint esversion: 11, jquery: true */`

This allows the JShint validator to recognize modern ES6 methods, such as: `let`, `const`, `template literals`, `arrow functions (=>)`, etc.

**IMPORTANT**: External resources

Sometimes we'll write JavaScript that imports variables from other files, such as "an array of questions" from `questions.js`, which are used within the main `script.js` file elsewhere. If that's the case, the JShint validation tool doesn't know how to recognize "unused variables" that would normally be imported locally when running your own project. These warnings are acceptable, so showcase on your screenshot(s).

The same thing applies when using external libraries such as Stripe, Leaflet, Bootstrap, Materialize, etc. To instantiate these components, we need to use their respective declarator. Again, the JShint validation tool would flag these as "undefined/unused variables". These warnings are acceptable, so showcase on your screenshot(s).

⚠️ --- END --- ⚠️

I have used the recommended [JShint Validator](https://jshint.com) to validate all of my JS files.

| Directory | File | URL | Screenshot | Notes |
| --- | --- | --- | --- | --- |
| reviews | [main.js](https://github.com/KC-85/Joystick_Journalist/blob/main/reviews/static/js/main.js) | N/A | ![screenshot](documentation/validation/js-reviews-main.png) | Notes (if applicable) |


### Python

⚠️ INSTRUCTIONS ⚠️

The [CI Python Linter](https://pep8ci.herokuapp.com) can be used two different ways.

- Copy/Paste your Python code directly into the linter.
- As an API, using the "raw" URL appended to the linter URL.
    - To find the "raw" URL, navigate to your file directly on the GitHub repo.
    - On that page, GitHub provides a button on the right called "Raw" that you can click.
    - From that new page, copy the full URL, and paste it after the CI Python Linter URL (with a `/` separator).

It's recommended to validate each file using the API URL. This will give you a custom URL which you can use on your testing documentation. It makes it easier to return back to a file for validating it again in the future. Use the steps above to generate your own custom URLs for each Python file.

**IMPORTANT**: `E501 line too long` errors

You must strive to fix all Python lines that are too long (>80 characters). In rare cases where you cannot break the lines [*without breaking the functionality*], adding "`  # noqa`" (*NO Quality Assurance*) to the end of those lines will ignore linting validation. Do not use "`  # noqa`" all over your project just to clear down validation errors! This can still cause a project to fail, for failing to fix actual PEP8 validation errors.

Sometimes variables can get too long, or excessive `if/else` conditional statements. These are acceptable instances to use the "`  # noqa`" comment.

When trying to fix "line too long" errors, try to avoid using `/` to split lines. A better approach would be to use any type of opening bracket, and hit `<Enter>` just after that. Any opening bracket type will work: `(`, `[`, `{`. By using an opening bracket, Python knows where to appropriately indent the next line of code, without having to *guess* for yourself and attempt to "tab" to the correct indentation level.

⚠️ --- END --- ⚠️

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

⚠️ INSTRUCTIONS ⚠️

Use this space to discuss testing the live/deployed site on various device sizes.

The minimum requirement is to test the following 3 sizes:

- Mobile
- Tablet
- Desktop

**IMPORTANT**: You must provide screenshots of your results, to "prove" that you've actually tested them.

Using the [amiresponsive](http://ami.responsivedesign.is) mockup images (*or similar*) does not meet the requirements. Consider using some of the built-in device sizes from the Developer Tools.

If you have tested the project on your actual mobile phone or tablet, consider also including screenshots of these as well. It showcases a higher level of manual tests, and can be seen as a positive inclusion!

⚠️ --- END --- ⚠️

I've tested my deployed project to check for responsiveness issues.

| Page | Mobile | Tablet | Desktop | Notes |
| --- | --- | --- | --- | --- |
| Register | ![screenshot](documentation/responsiveness/mobile_register.png) | ![screenshot](documentation/responsiveness/tablet_register.png) | ![screenshot](documentation/responsiveness/desktop_register.png) | Works as expected |
| Login | ![screenshot](documentation/responsiveness/mobile_login.png) | ![screenshot](documentation/responsiveness/tablet_login.png) | ![screenshot](documentation/responsiveness/desktop_login.png) | Works as expected |
| Landing Page | ![screenshot](documentation/responsiveness/mobile_landing_page.png) | ![screenshot](documentation/responsiveness/tablet_landing_page.png) | ![screenshot](documentation/responsiveness/desktop_landing_page.png) | Works as expected |
| Add Game | ![screenshot](documentation/responsiveness/mobile_add_game.png) | ![screenshot](documentation/responsiveness/tablet_add_game.png) | ![screenshot](documentation/responsiveness/desktop_add_game.png) | Works as expected |
| Delete Game | ![screenshot](documentation/responsiveness/mobile-blog-post.png) | ![screenshot](documentation/responsiveness/tablet-blog-post.png) | ![screenshot](documentation/responsiveness/desktop-blog-post.png) | Works as expected |
| Add Review | ![screenshot](documentation/responsiveness/mobile-blog-post.png) | ![screenshot](documentation/responsiveness/tablet-blog-post.png) | ![screenshot](documentation/responsiveness/desktop-blog-post.png) | Works as expected |
| Edit Review | ![screenshot](documentation/responsiveness/mobile-blog-post.png) | ![screenshot](documentation/responsiveness/tablet-blog-post.png) | ![screenshot](documentation/responsiveness/desktop-blog-post.png) | Works as expected |
| Delete Review | ![screenshot](documentation/responsiveness/mobile-blog-post.png) | ![screenshot](documentation/responsiveness/tablet-blog-post.png) | ![screenshot](documentation/responsiveness/desktop-blog-post.png) | Works as expected |
| All Reviews | ![screenshot](documentation/responsiveness/mobile-blog-post.png) | ![screenshot](documentation/responsiveness/tablet-blog-post.png) | ![screenshot](documentation/responsiveness/desktop-blog-post.png) | Works as expected |
| 404 | ![screenshot](documentation/responsiveness/mobile-404.png) | ![screenshot](documentation/responsiveness/tablet-404.png) | ![screenshot](documentation/responsiveness/desktop-404.png) | Works as expected |

## Browser Compatibility

⚠️ INSTRUCTIONS ⚠️

Use this space to discuss testing the live/deployed site on various browsers. Consider testing at least 3 different browsers, if available on your system. You DO NOT need to use all of the browsers below, just pick any 3 (minimum).

Recommended browsers to consider:
- [Chrome](https://www.google.com/chrome)
- [Firefox (Developer Edition)](https://www.mozilla.org/firefox/developer)
- [Edge](https://www.microsoft.com/edge)
- [Safari](https://support.apple.com/downloads/safari)
- [Brave](https://brave.com/download)
- [Opera](https://www.opera.com/download)

**IMPORTANT**: You must provide screenshots of the browsers you've tested, to "prove" that you've actually tested them.

Please note, there are services out there that can test multiple browser compatibilities at the same time. Some of these are paid services, but some are free. If you use these, you must provide a link to the source used for attribution, and multiple screenshots of the results.

⚠️ --- END --- ⚠️

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

⚠️ INSTRUCTIONS ⚠️

Use this space to discuss testing the live/deployed site's Lighthouse Audit reports. Avoid testing the local version (Gitpod/VSCode/etc.), as this can have knock-on effects for performance. If you don't have "Lighthouse" in your Developer Tools, it can be added as an [extension](https://chrome.google.com/webstore/detail/lighthouse/blipmdconlkpinefehnmjammfjpmpbjk).

Unless your project is a single-page application (SPA), you should test Lighthouse Audit results for all of your pages, for both *mobile* and *desktop*.

**IMPORTANT**: You must provide screenshots of the results, to "prove" that you've actually tested them.

⚠️ --- END --- ⚠️

I've tested my deployed project using the Lighthouse Audit tool to check for any major issues. Some warnings are outside of my control, and mobile results tend to be lower than desktop.

| Page | Mobile | Desktop |
| --- | --- | --- |
| Hero | ![screenshot](documentation/lighthouse/mobile/hero_section.png) | ![screenshot](documentation/lighthouse/desktop/hero_section.png) |
| Login | ![screenshot](documentation/lighthouse/mobile/login.png) | ![screenshot](documentation/lighthouse/desktop/login.png) |
| Register | ![screenshot](documentation/lighthouse/mobile/register.png) | ![screenshot](documentation/lighthouse/desktop/register.png) |
| Landing Page (Game List) | ![screenshot](documentation/lighthouse/mobile/landing_page.png) | ![screenshot](documentation/lighthouse/desktop/landing_page.png) |
| Add Game | ![screenshot](documentation/lighthouse/mobile/add_game.png) | ![screenshot](documentation/lighthouse/desktop/add_game.png) |
| Delete Game | ![screenshot](documentation/lighthouse/mobile/delete_game.png) | ![screenshot](documentation/lighthouse/desktop/delete_game.png) |
| Add Review | ![screenshot](documentation/lighthouse/mobile/add_review.png) | ![screenshot](documentation/lighthouse/desktop/add_review.png) |
| Edit Review | ![screenshot](documentation/lighthouse/mobile/edit_review.png) | ![screenshot](documentation/lighthouse/desktop/edit_review.png) |
| All Reviews | ![screenshot](documentation/lighthouse/mobile-all-reviews.png) | ![screenshot](documentation/lighthouse/desktop-all-reviews.png) |
| 404 | ![screenshot](documentation/lighthouse/mobile-404.png) | ![screenshot](documentation/lighthouse/desktop-404.png) |

- **Note:** Delete Review shows up a pop up message instead of a seperate page, and therefore I am unable to test it's lighthouse score.

## Defensive Programming

⚠️ INSTRUCTIONS ⚠️

Defensive programming (defensive design) is extremely important! When building projects that accept user inputs or forms, you should always test the level of security for each form field. Examples of this could include (but not limited to):

All Projects:

- Users cannot submit an empty form (add the `required` attribute)
- Users must enter valid field types (ensure the correct input `type=""` is used)
- Users cannot brute-force a URL to navigate to a restricted pages

Python Projects:

- Users cannot perform CRUD functionality if not authenticated (if login functionality exists)
- User-A should not be able to manipulate data belonging to User-B, or vice versa
- Non-Authenticated users should not be able to access pages that require authentication
- Standard users should not be able to access pages intended for superusers/admins

You'll want to test all functionality on your application, whether it's a standard form, or CRUD functionality, for data manipulation on a database. Try to access various pages on your site as different user types (User-A, User-B, guest user, admin, superuser). You should include any manual tests performed, and the expected results/outcome.

Testing should be replicable (can someone else replicate the same outcome?). Ideally, tests cases should focus on each individual section of every page on the website. Each test case should be specific, objective, and step-wise replicable.

Instead of adding a general overview saying that everything works fine, consider documenting tests on each element of the page (eg. button clicks, input box validation, navigation links, etc.) by testing them in their "happy flow", their "bad/exception flow", mentioning the expected and observed results, and drawing a parallel between them where applicable.

Consider using the following format for manual test cases:

- Expected Outcome / Test Performed / Result Received / Fixes Implemented

- **Expected**: "Feature is expected to do X when the user does Y."
- **Testing**: "Tested the feature by doing Y."
- (either) **Result**: "The feature behaved as expected, and it did Y."
- (or) **Result**: "The feature did not respond to A, B, or C."
- **Fix**: "I did Z to the code because something was missing."

Use the table below as a basic start, and expand on it using the logic above.

⚠️ --- END --- ⚠️

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

⚠️ INSTRUCTIONS ⚠️

Testing User Stories is actually quite simple, once you've already got the stories defined on your README.

Most of your project's **Features** should already align with the **User Stories**, so this should be as simple as creating a table with the User Story, matching with the re-used screenshot from the respective Feature.

⚠️ --- END --- ⚠️

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

⚠️ INSTRUCTIONS ⚠️

Adjust the code below (file names, function names, etc.) to match your own project files/folders. Use these notes loosely when documenting your own Python Unit tests, and remove/adjust where applicable.

⚠️ SAMPLE ⚠️

I have used Django's built-in unit testing framework to test the application functionality. In order to run the tests, I ran the following command in the terminal each time:

- `python3 manage.py test name-of-app`

To create the coverage report, I would then run the following commands:

- `pip3 install coverage`
- `pip3 freeze --local > requirements.txt`
- `coverage run --omit=*/site-packages/*,*/migrations/*,*/__init__.py,env.py,manage.py test`
- `coverage report`

To see the HTML version of the reports, and find out whether some pieces of code were missing, I ran the following commands:

- `coverage html`
- `python3 -m http.server`

Below are the results from the full coverage report on my application that I've tested:

![screenshot](documentation/automation/html-coverage.png)

#### Unit Test Issues

⚠️ INSTRUCTIONS ⚠️

Use this section to list any known issues you ran into while writing your Python unit tests. Remember to include screenshots (where possible), and a solution to the issue (if known). This can be used for both "fixed" and "unresolved" issues. Remove this sub-section entirely if you somehow didn't run into any issues while working with your tests.

⚠️ --- END --- ⚠️

## Bugs

⚠️ INSTRUCTIONS ⚠️

Nobody likes bugs,... except the assessors! Projects seem more suspicious if a student doesn't properly track their bugs. If you're about to submit your project without any bugs listed below, you should ask yourself why you're doing this course in the first place, if you're able to build this entire application without running into any bugs. The best thing you can do for any project is to document your bugs! Not only does it show the true stages of development, but think of it as breadcrumbs for yourself in the future, should you encounter the same/similar bug again, it acts as a gentle reminder on what you did to fix the bug.

If/when you encounter bugs during the development stages of your project, you should document them here, ideally with a screenshot explaining what the issue was, and what you did to fix the bug.

Alternatively, an improved way to manage bugs is to use the built-in **[Issues](https://www.github.com/KC-85/Joystick_Journalist/issues)** tracker on your GitHub repository. This can be found at the top of your repository, the tab called "Issues".

If using the Issues tracker for bug management, you can simplify the documentation process for testing. Issues allow you to directly paste screenshots into the issue page without having to first save the screenshot locally. You can add labels to your issues (e.g. `bug`), assign yourself as the owner, and add comments/updates as you progress with fixing the issue(s). Once you've solved the issue/bug, you should then "Close" it.

When showcasing your bug tracking for assessment, you can use the following examples below.

⚠️ --- END --- ⚠️

### Fixed Bugs

[![GitHub issue custom search](https://img.shields.io/github/issues-search?query=repo%3AKC-85%2FJoystick_Journalist%20label%3Abug&label=bugs)](https://www.github.com/KC-85/Joystick_Journalist/issues?q=is%3Aissue+is%3Aclosed+label%3Abug)

I've used [GitHub Issues](https://www.github.com/KC-85/Joystick_Journalist/issues) to track and manage bugs and issues during the development stages of my project.

All previously closed/fixed bugs can be tracked [here](https://www.github.com/KC-85/Joystick_Journalist/issues?q=is%3Aissue+is%3Aclosed+label%3Abug).

![screenshot](documentation/bugs/gh-issues-closed.png)

### Unfixed Bugs

⚠️ INSTRUCTIONS ⚠️

You will need to mention any unfixed bugs and why they are not fixed upon submission of your project. This section should include shortcomings of the frameworks or technologies used. Although time can be a big variable to consider, paucity of time and difficulty understanding implementation is not a valid reason to leave bugs unfixed. Where possible, you must fix all outstanding bugs, unless outside of your control.

If you've identified any unfixed bugs, no matter how small, be sure to list them here! It's better to be honest and list them, because if it's not documented and an assessor finds the issue, they need to know whether or not you're aware of them as well, and why you've not corrected/fixed them.

⚠️ --- END --- ⚠️

[![GitHub issues](https://img.shields.io/github/issues/KC-85/Joystick_Journalist)](https://www.github.com/KC-85/Joystick_Journalist/issues)

Any remaining open issues can be tracked [here](https://www.github.com/KC-85/Joystick_Journalist/issues).

![screenshot](documentation/bugs/gh-issues-open.png)

### Known Issues

| Issue | Screenshot |
| --- | --- |
| On devices smaller than 375px, the page starts to have horizontal `overflow-x` scrolling. | ![screenshot](documentation/issues/overflow.png) |
| When validating HTML with a semantic `<section>` element, the validator warns about lacking a header `h2-h6`. This is acceptable. | ![screenshot](documentation/issues/section-header.png) |
| Validation errors on "signup.html" coming from the Django Allauth package. | ![screenshot](documentation/issues/allauth.png) |

> [!IMPORTANT]
> There are no remaining bugs that I am aware of, though, even after thorough testing, I cannot rule out the possibility.

