# Just Eat API Client

This project is a Python-based API client for retrieving restaurant data from the Just Eat API. The client is capable of fetching restaurant information based on a given postcode. The retrieved data includes restaurant names, ratings, and cuisines offered.

## Project Structure

The project consists of the following files and directories:

- **just_eat_api/**
  - **\_\_init\_\_.py**: Empty file to indicate that this directory should be considered a Python package.
  - **client.py**: Contains the `JustEatClient` class, which interacts with the Just Eat API to fetch restaurant data.
  - **models.py**: Defines the `Restaurant` class representing restaurant entities.
- **main.py**: The main script to run the API client, fetch data, and store it in a JSON file.

## How to Use

To use this API client, follow these steps:

1. **Clone the Repository**: Clone this repository to your local machine.
2. **Install Dependencies**: Ensure you have Python installed. Install the required dependencies using the following commands:

    ```shell
    git clone https://github.com/arsenmakovei/just-eat-project.git
    cd just-eat-project
    python -m venv venv
    Windows: venv\Scripts\activate
    Linux, Unix: source venv/bin/activate
    pip install -r requirements.txt
    ```

3. **Run the Script**: Execute the `main.py` script. The script fetches restaurant data based on the provided postcode and stores the information in a JSON file named `restaurants.json`.

    ```shell
    python main.py
    ```

4. **View the Output**: After the script runs successfully, you can find the retrieved restaurant data in the `restaurants.json` file.

## Configuration

In the `main.py` file, you can customize the following parameters:

- **postcode**: Specify the postcode for which you want to fetch restaurant data. Update the `postcode` variable in the `main.py` script.

- **proxy**: If you are behind a proxy, you can specify the proxy URL in the `proxy` variable in the `main.py` script.

## Error Handling

The API client handles various exceptions, including connection errors and blocked requests. If any issues occur during the API call, appropriate error messages will be displayed.

---

Feel free to explore and modify this project as needed to fit your requirements. Happy coding!

