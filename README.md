# Python_PyTest_Allure

## Execute a test with Pytest
Install packages:
- pytest

Use the following command to execute a specific test:
```python
pytest <Test_Script.py>
```
Use the following command to execute all the tests at once:
```python
python -m pytest
```
Use the following command to execute all the tests with a specific marker (e.g. @pytest.mark.nrt):
```python
python -m pytest -v -m nrt
```
## Generate an HTML Report
Install packages:
- pytest-html

Use the following command to execute the test generating an HTML report:
```python
pytest <Test_Script.py> --html=.\TestReportHtml\<Report_Name>.html --self-contained-html
```
![HtmlReport](https://user-images.githubusercontent.com/56591355/196549100-aae711c0-22b9-4360-9fee-f82d1b9d0f1b.png)

## Generate an Allure Report
Install packages:
- allure-pytest
- allure-pytest-commons

Install allure from cmd, using the command:
```bash
npm install -g allure-commandline --save-dev
```
Execute the test generating an allure report in JSON format:
```python
python -m pytest <Test_Script.py> --alluredir=.\TestReportAllure
```

Convert JSON into HTML, to see this on the browser:
```python
allure serve .\TestReportAllure
```
This command will start a jetty server and the report will be visible inside the browser.
![AllureReport](https://user-images.githubusercontent.com/56591355/196549033-907568cd-06bf-4959-bf41-c5fd9e6b38bf.png)


NB: in case the following error appears: ps1 cannot be loaded because running scripts is disabled on this system
Use the following command through powershell script:
```powershell
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy Unrestricted
```