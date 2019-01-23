# auto1-automation-test
Create automation test for search functionality

# Requirements
Using [pip](https://pip.pypa.io/en/stable/installing/), you need to install:
```bash
sudo pip install selenium
sudo pip install nose
```

# Usage
Just run:

```bash
nosetests auto1_selenium_test.py -v
```

# Output Example

```bash
test_car_first_registration_after_or_equal_2015 (auto1_selenium_test.TestSearchPage) ... ok
test_descending_price_order (auto1_selenium_test.TestSearchPage) ... ok

----------------------------------------------------------------------
Ran 2 tests in 34.431s

OK
```
