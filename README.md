# Cache API

This API  will return a key-value pair of randomly generated UUID. Key will be a timestamp and value will be UUID. While the server is running, whenever the API is called, it would return all the previous UUIDs ever generated by the API alongside a new UUID.

Sample output

```
{

"2021-05-21 12:10:19.484523": "e8c928fea580474cae5aa3934c59c26f"

"2021-05-21 12:08:25.751933": "fcd25b46bec84ef79e14410b91fbf0b3",

"2021-05-21 12:07:27.150522": "6270d1d412b546a28b7d2c98130e1a5a",

}
```
##### Disclaimer
The instructions in this documentattion is intended for mac users. Equivalent steps can be taken on other OS by entering the same commands on terminal or their equivalents. Feel free to open an issue for clarification on machine specific problems.

## Running on Local Machine

This project is built with docker. Docker file builds 2 seperate containers to run the redis server and flask application in a development environment.

### Prerequisites
Ensure you have the following installed on your local device.

- Python ([Installation guide](https://www.python.org/downloads/))
- Docker ([Installation guide](https://docs.docker.com/compose/install/))
- Redis  ([Installation guide](https://redis.io/topics/quickstart))


To run this on your local machine, clone this repository and install the packages in the requirements.txt file (preferably in a virtual environment). 

While in the "cacheapi" root folder, run the following command (Installation is optional as the Dockerfile addresses this step when building image containers).

```
> pip install -r requirements.txt
```

Ensure environment variables in the local environment are set in a ".env" file. See the ".env.example"  file for a sample of the required environment variables.
- REDIS_PORT: The port where local redis instance for use is served.
- REDIS_HOST: The host for local redis server.
- SECRET_KEY: Implemented for use in UUID generation algorithm.
- TEST_REDIS_HOST: The port where local redis instance for test is served.
- TEST_REDIS_PORT: The host for local redis test server .

To deploy service in local machine, docker compose would be used. Run the following command in the root directory of the "cacheapi" project from your local terminal.

```
> docker-compose up -d --build 
```

The API should now be accessible via the url : "http://127.0.0.1:5000/"


