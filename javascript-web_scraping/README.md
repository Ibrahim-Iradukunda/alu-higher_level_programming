# JavaScript Web Scraping Project

## Overview
This project involves building JavaScript scripts that interact with web services and manipulate data using Node.js. The scripts cover various tasks such as reading and writing to files, sending GET requests, parsing API responses, and storing webpage content.

## Learning Objectives
By the end of this project, you will be able to:
- Understand why JavaScript is a powerful programming language.
- Manipulate JSON data effectively.
- Use the `request` and `fetch` APIs.
- Work with the `fs` module to read and write files.

## Requirements
- **Allowed Editors**: `vi`, `vim`, `emacs`
- **Node.js Version**: 10.14.x on Ubuntu 14.04 LTS
- All files should end with a new line and be executable.
- Files must be semistandard compliant (Standard + semicolons on top).
- `request` module is required (Note: it’s deprecated since February 2020).

### Install Node.js and Required Modules
1. Install Node 10:
    ```bash
    $ curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
    $ sudo apt-get install -y nodejs
    ```
2. Install `semistandard`:
    ```bash
    $ sudo npm install semistandard --global
    ```
3. Install `request` module:
    ```bash
    $ sudo npm install request --global
    $ export NODE_PATH=/usr/lib/node_modules
    ```

## Scripts

### 0. `0-readme.js`
Reads and prints the content of a file. Handles errors when the file doesn't exist.

### 1. `1-writeme.js`
Writes a string to a file. Handles errors while writing to the file.

### 2. `2-statuscode.js`
Displays the status code of a GET request to a specified URL using the `request` module.

### 3. `3-starwars_title.js`
Fetches and prints the title of a Star Wars movie using the Star Wars API based on a given movie ID.

### 4. `4-starwars_count.js`
Counts and prints the number of movies where the character "Wedge Antilles" is present, using the Star Wars API.

### 5. `5-request_store.js`
Gets the contents of a webpage and stores it in a file, writing the response in UTF-8 encoding.

### 6. `6-completed_tasks.js`
Fetches a list of tasks and computes the number of completed tasks for each user ID.

## Usage
1. Clone the repository:
    ```bash
    $ git clone https://github.com/yourusername/alu-higher_level_programming.git
    ```
2. Navigate to the project directory:
    ```bash
    $ cd javascript-web_scraping
    ```
3. Run the scripts with appropriate arguments. For example:
    ```bash
    $ ./0-readme.js <file-path>
    ```

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

