# Inverse Kinematics Web Application

This web application demonstrates inverse kinematics functionality. It uses a Flask server on the backend and React on the frontend. The application is containerized using Docker.

## Prerequisites

1. Install [Docker](https://www.docker.com/get-started)
2. Install [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) (if you haven't already)

## Setup and Running the Application

1. Clone the repository: `git clone https://github.com/nikhil1006/inversekinematicsweb.git`

    ```bash
    cd inversekinematicsweb
    ```
2. Build the Docker image: `docker build -t your-image-name`

    Replace `your-image-name` with a name of your choice for the Docker image.

3. Run the Docker container: `docker run -p 5000:5000 your-image-name`

    If port 5000 is already in use, you can choose another port, e.g., `-p 5001:5000`, and update your application configuration accordingly.

4. Access the application in your browser by navigating to `http://localhost:5000`.

## Development

When making changes to the application:

1. Rebuild the Docker image.

2. Run the updated Docker container.

3. Test your changes by accessing the application in your browser.

## Troubleshooting

If you encounter an error about the port being already in use, follow these steps:

1. Find the process using the port and stop it:

- On Linux/macOS:

  ```bash
  sudo lsof -i :5000
  sudo kill [PID]
  ```

  Replace `[PID]` with the process ID from the first command.

- On Windows:

  ```powershell
  netstat -a -n -o | findstr :5000
  taskkill /F /PID [PID]
  ```

  Replace `[PID]` with the process ID from the first command.

2. Alternatively, use a different port for your application, updating both the Docker run command and the application configuration as necessary.

## License

This project is licensed under the MIT License.










