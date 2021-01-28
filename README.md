# PythonSelenium automation framework
### Web automation using Python and Selenium
> https://selenium-python.readthedocs.io/

### Demo sites used for automation
* https://www.nopcommerce.com/en/demo
* https://admin-demo.nopcommerce.com/login

### Trigger tests using below command from project root directory
> py.test -v -s -n=2 test_cases/test_login.py --browser Chrome
* -n=2 [Specifies to use 2 workers nodes for parallel execution. Package used: pytest-xdist.]
* --browser Chrome [Specifies which browser is to be used for running tests]

# Reference
> https://github.com/pavanoltraining/nopCommerceProject
>
> https://www.youtube.com/playlist?list=PLUDwpEzHYYLt2RzOb-_eafLAP0VSoyJhf