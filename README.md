# weather_report

A CLI app to get data from the Weather Underground based on the user's location. Then present a weather report to the user.

For my portfolio and contact information, please visit: [Will Warren](https://willwile4.github.io)

## Objectives

* Understand the purpose and structure of Web APIs
* Understand JSON structure
* Be able to access an API using a token
* Be able to make HTTP requests via requests
* Be able to pull and merge information from multiple API endpoints
* Be able to write tests that mock API responses

### How to Run:
via CLI:
1. '$ echo layout python3 > .envrc'
2. '.direnv allow', wait for installation
3. '$ pip install -r requirements.txt'
4. '$ python3 weather_channel.py'
5. Use navigation menu to find desired information.

### Files:
1. README.md
2. requirements.txt
3. weather_channel.py
  - UI for weather report. user enters zip and which type of forecast they want, or all.
4. weather_cat.py
  - a suite of instances and getter methods
5. weather.py
  - Classes which call the end points and format/parse data

### Notes
1. Could expand functionality to include ability to read city names via regex.
2. Implement caching in order to avoid being rate limited.
