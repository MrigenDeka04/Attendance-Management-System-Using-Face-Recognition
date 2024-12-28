# Face-Recognition-Attendance-Management-System
Attendance Management System based on Face Recognition using Python and OpenCv  

### Overview
<img src="https://github.com/user-attachments/assets/30971c35-7649-4dbe-a339-89849bb68040">

### Code Requirements
- Opencv(`pip install opencv-python`)
- Tkinter(Available in python)
- PIL (`pip install Pillow`)
- Pandas(`pip install pandas`)


### Project Structure

- After run you need to give your face data to system so enter your ID and name in box than click on `Take Images` button.
- It will collect 70 images of your faces, it save a images in `TrainingImage` folder
- After that we need to train a model(for train a model click on `Train Image` button.
- It will take 2-5 minutes for training(for 10 person data).
- After training click on `Automatic Attendance` ,it can fill attendance by your face using our trained model (model will save in `TrainingImageLabel` )
- it will create `.csv` file of attendance according to time & subject.
- You can store data in database (install wampserver),change the DB name according to your in `AMS_Run.py`.
- `Manually Fill Attendance` Button in UI is for fill a manually attendance (without facce recognition),it's also create a `.csv` and store in a database.

### Screenshots

### User Interface
<img src="https://github.com/user-attachments/assets/e586ab0f-60b0-4644-ad77-dd6d16434eb5">

### Model is trained
<img src="https://github.com/user-attachments/assets/ac02ec86-7916-4bcd-935a-7bc0e70e60ce">

### When it Recognises me
<img src="https://github.com/user-attachments/assets/2565e65b-2f43-4a02-8de8-4d9d91cbd541">

### Generated Excel file
<img src="https://github.com/user-attachments/assets/04584dc8-2ca5-46a6-addf-e1087aa3c3d1">





### Notes
- Noisy image can reduce the accuracy, so quality of images should be good.
- Create a `TrainingImage` folder in a project.

