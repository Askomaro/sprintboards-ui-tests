In order to run tests, Chrome WebDriver has to be installed and be visible in $PATH.

Install dependencies and libraries into a virtual environment:
`pip3 install -r requirements`

To run tests with a user credentials:
`pytest tests/ --login=* --password=*`
where * - login and password
