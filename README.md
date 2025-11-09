<h1>Test Automation Framework Design</h1>

<h2>Overview</h2> <p>This framework leverages Python as the programming language with Pytest as the test engine and runner. It incorporates best practices such as the Page Object Model (POM) design pattern, structured logging, and detailed reporting to create a robust, maintainable, and scalable test automation solution.</p>

<hr />

<h2>Technology Stack</h2> <ul> <li><strong>Programming Language:</strong> Python</li> <li><strong>Test Engine/Runner:</strong> Pytest</li> <li><strong>Logging:</strong> Python's built-in <code>logging</code> module</li> <li><strong>Reporting:</strong> Allure Framework</li> <li><strong>Design Pattern:</strong> Page Object Model (POM)</li> </ul>

<hr />

<h2>Directory Structure</h2> <pre><code>|- Configs -> Contains environment-specific configuration files (JSON/YAML) such as browser types, URLs, timeouts, passwords, API keys, tokens, etc.

|- Common -> Houses common reusable functions like setup and teardown routines, exception handling, and common assertions.

|- Utility -> Contains utility modules for parsers, schedulers, API calls, email sending, screenshot helpers, and other supportive functionalities.

|- Pages -> Contains Page Object classes representing UI pages. 
  |-- Each Page Object abstracts UI details, encapsulating element locators and interaction methods. 
  |-- This abstraction hides UI implementation details from test scripts.

|- Logs -> Stores runtime log files generated during test execution. Uses different log levels: INFO, ERROR, DEBUG.

|- Reports -> Stores generated test reports. 
  |-- Allure is used to create detailed, interactive HTML reports.

|- Tests -> Contains two subfolders: 
  |-- Test Data  : Holds test data files such as CSV or JSON. 
  |-- Tests      : Contains the actual test scripts defining WHAT to test and making assertions. </code></pre>

<hr />

<h2>Key Concepts</h2> <ul> <li><strong>Page Objects:</strong> Define HOW to interact with the UI and manage element locators.</li> <li><strong>Test Scripts:</strong> Define WHAT to test and include assertions, separated from UI interaction logic.</li> <li><strong>Logging:</strong> Centralized logging for traceability and debugging.</li> <li><strong>Reporting:</strong> Interactive and detailed reports for test results analysis.</li> </ul>

<hr />

<p>This framework design ensures separation of concerns, reusability, and ease of maintenance, making it suitable for complex test automation needs.</p>
