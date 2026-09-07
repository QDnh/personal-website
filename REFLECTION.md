Question 1: Choose one test from the provided suite and name it. In plain English, what does that test confirm about your site? Then name one thing your site could get wrong that this test would not catch.

Q1 Answer: I chose test_url_exists_at_correct_location from the HomePageTests class. The "test_url_exists_at_correct_location" test checks if the default '/' URL can be reached and stores the response data. It then checks the response data with an assertion. If the response data equals the assertion, it returns true. The assertion in this case, is the response data is equal to the HTTP status code for success. This test doesn't check if '/' and 'home' are the same. A different test does that.


Question 2. You built three pages that share one navigation bar. If you added a fourth link to your navigation, how many files would you edit? How many would you have edited if you had not used base.html, and why?

Q2 Answer: Using base.html, I would need to edit base.html, pages.urls.py, and pages.views.py. If I had added a fourth without inheritance, I would have needed to manually add the link to the fourth page onto every navigation bar of every page in addition to base.html, pages.urls.py, and pages.views.py. This assumes excluding the fourth page's html file. This is because without inheritance, there is a navigation bar on every page that must be edited.