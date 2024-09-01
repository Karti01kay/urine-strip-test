[Live](https://urine-strip-test.onrender.com)

# Introduction
A web interface that allows users to upload an image of their urine strip (see below) and identify the colors on the strip (see strip images below). Each strip
will have 10 colors. You will have to analyze the image and return the results as a json with 10 colors (RGB values).


# Overview of the solution  
We can break the task into several steps:

1) Create a Web Interface: Using a framework like Flask (Python) or Node.js (JavaScript) to handle file uploads.
2) Image Processing: Use OpenCV to analyze the uploaded image and extract the colors.
3) Return Results: Convert the extracted colors into a JSON format and return it to the user. 
    
   
# Steps on how to run  
1)  Create a root folder  
```
mkdir urine-test
```  
2) Change into the project directory
```
cd urine test
```
3) Open the project in Visual Studio Code and then open a new terminal. Create a virtual environment using the below command
```
# Windows
py -m venv .venv
# Linux
python -m venv .venv
```
4) Activate the virtual environment
```
# Windows
.\.venv\Scripts\activate
# Linux
source .venv\bin\activate
```
5) Install the dependencies
```
pip install flask opencv-python
```  
6) Copy the given files: 
```
app.py
index.html
```  
8) Run the application
```
python app.py
```
9) Visit the following link in your web browser, upload an image, and receive the JSON response with the identified colors.
```
http://127.0.0.1:5000
```


#     Screenshots to show the working
![SS1 - homepage](https://res.cloudinary.com/dkddubkcn/image/upload/v1720258742/Screenshot_275_qujzun.png)
Screenshot 1

![SS2 - example1](https://res.cloudinary.com/dkddubkcn/image/upload/v1720258742/Screenshot_276_e5j89o.png)
Screenshot 2

![SS3 - example2](https://res.cloudinary.com/dkddubkcn/image/upload/v1720258742/Screenshot_277_giztvv.png)
Screenshot 3
