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
![screenshot 1]()
*Add caption explaining what this shows*

![Screenshot2](Add screenshot 2 here with proper name)
*Add caption explaining what this shows*

![Screenshot3](Add screenshot 3 here with proper name)
*Add caption explaining what this shows*

# Diagrams
![Workflow](Add your workflow/architecture diagram here)
*Add caption explaining your workflow*


# Build Photos
![Components](Add photo of your components here)
*List out all components shown*

![Build](Add photos of build process here)
*Explain the build steps*

![Final](Add photo of final product here)
*Explain the final build*

### Project Demo
# Video
[Add your demo video link here]
*Explain what the video demonstrates*

# Additional Demos
[Add any extra demo materials/links]

## Team Contributions
- [Name 1]: [Specific contributions]
- [Name 2]: [Specific contributions]
- [Name 3]: [Specific contributions]

---
Made with ❤️ at TinkerHub Useless Projects 

![Static Badge](https://img.shields.io/badge/TinkerHub-24?color=%23000000&link=https%3A%2F%2Fwww.tinkerhub.org%2F)
![Static Badge](https://img.shields.io/badge/UselessProjects--25-25?link=https%3A%2F%2Fwww.tinkerhub.org%2Fevents%2FQ2Q1TQKX6Q%2FUseless%2520Projects)



