# BachchanMeter
<img width="3188" height="1202" alt="frame (3)" src="https://github.com/user-attachments/assets/517ad8e9-ad22-457d-9538-a9e62d137cd7" />


## Basic Details
### Team Name: Innovators


### Team Members
- Member 2: Aleesha Sujith - Muthoot Institute of Technology and Science
- Member 3: Gowri Krishna - Muthoot Institute of Technology and Science

### Project Description
BachchanMeter is a web application that takes in an image of a random tree and gives you it's height in Bachchans! If your tree is 12m tall, then our application measures it in terms of Bachchan units and gives 6.6 Bachchans as output.

### The Problem (that doesn't exist)
To find the height in Bachchan units for a random tree.

### The Solution (that nobody asked for)
It uses pixel height to measure the height of the tree approximately and at times with the use of reference objects. Then the height is divided by Big B's height to give you Bachchan units!

## Technical Details
### Technologies/Components Used
For Software:
- Languages Used: Python, Javascript, HTML, CSS
- Frameworks Used: Flask
- Libraries Used: OpenCV, Flask, Pillow, SciPy
- Tools used: pip, VS Code

For Hardware:
- No hardware used

### Implementation
For Software: 

The project uses a Flask backend to handle image uploads and process them using OpenCV.  
When a user uploads a photo of a tree, the following steps occur:

1. The image is sent to the Flask server via a POST request.
2. OpenCV reads and processes the image to detect the tree height in pixels.
3. A fixed reference height for Amitabh Bachchan (1.88m) is used to convert the tree's height into "Bachchan units".
4. The result is sent back to the frontend as JSON.
5. JavaScript updates the webpage to display the number of Bachchans tall the tree is.

*Tech stack*:
- Python (Flask, OpenCV)
- HTML, CSS, JavaScript
- GitHub for version control
  
## Installation

To set up the project locally, first clone the repository using git clone https://github.com/gowrikrishna985/amitabh.git and navigate into the project folder with cd amitabh.
It’s recommended to create a virtual environment to keep the project dependencies isolated by running python -m venv venv. Activate the environment with venv\Scripts\activate on Windows or source venv/bin/activate on Mac/Linux.

Once the environment is active, install the required dependencies using pip install flask opencv-python.
If you have a requirements.txt file, you can install all dependencies in one go with pip install -r requirements.txt.

After installing the dependencies, start the Flask application by running python app.py

## Run

After completing the installation steps, run the Flask server with:
python app.py

### Project Documentation

For Software: This project is a fun web application that estimates the height of a tree in units of Amitabh Bachchan’s height (1.88 m). It uses a Python backend powered by Flask and OpenCV for image processing, with a frontend built using HTML, CSS, and JavaScript.


# Screenshots (Add at least 3)
![screenshot 1](images/Screenshot%202025-08-09%20044921.png)
*The home page where photo is to be uploaded*

![Screenshot2](images/Screenshot%202025-08-09%20044956.png)
*The photo being uploaded*

![Screenshot3](images/Screenshot%202025-08-09%20045017.png)
*The final result*

# Diagrams

## Workflow of the Tree Height Estimator App

### 1. User Interaction (Frontend)
- The user visits the web page.
- The main content is centered and visually appealing, with an animated background.
- The user sees a file upload form labeled "Choose Tree Image".
- The user selects an image of a tree and clicks "Calculate Tree Height".

### 2. File Upload (Frontend → Backend)
- The selected image is sent to the Flask backend via a POST request to the `/upload` route.

### 3. Image Processing & Height Estimation (Backend)
- The backend receives the image and saves it temporarily.
- The backend calls the tree analysis logic (in `tree_analyzer.py`) to estimate the tree's height from the image.
- The estimated height (in meters) is calculated.

### 4. Amitabh Bachchan Conversion (Backend)
- The backend divides the tree height by 1.88 (Amitabh Bachchan's height in meters) to get the number of "Amitabhs".
- The number is rounded to the nearest integer for display.

### 5. Result Rendering (Backend → Frontend)
- The backend deletes the uploaded image after processing.
- The backend renders the `index.html` template, passing:
  - The estimated tree height (in meters)
  - The number of Amitabhs
  - Any success or error messages

### 6. Result Display (Frontend)
- The user sees:
  - A message with the estimated tree height in meters and as "X Amitabh Bachchans".
  - A vertical stack of Amitabh Bachchan images, one for each "Amitabh" calculated.
  - (Optionally) The uploaded tree image for visual comparison.
- The user can upload another image to repeat the process.


**Summary:**  
The app provides a fun, visual way to estimate tree height from an image, expressing the result in both meters and as multiples of Amitabh Bachchan's height, with a modern, animated, and responsive UI.



# Build Photos
![screenshot 1](images/Screenshot%202025-08-09%20044921.png)
*The home page where photo is to be uploaded with a text component.*

![Screenshot2](images/Screenshot%202025-08-09%20044956.png)
*The photo being uploaded*

![Screenshot3](images/Screenshot%202025-08-09%20045017.png)
*The final result*


### Project Demo
# Video
<video src="images/Screen Recording 2025-08-09 051245.mp4" controls width="720" poster="images/Screenshot%202025-08-09%20044921.png"></video>


## Team Contributions
- Aleesha Sujith: Backend
- Gowri Krishna: Frontend

---
Made with ❤️ at TinkerHub Useless Projects 

![Static Badge](https://img.shields.io/badge/TinkerHub-24?color=%23000000&link=https%3A%2F%2Fwww.tinkerhub.org%2F)
![Static Badge](https://img.shields.io/badge/UselessProjects--25-25?link=https%3A%2F%2Fwww.tinkerhub.org%2Fevents%2FQ2Q1TQKX6Q%2FUseless%2520Projects)



