# 🌱 FarmBrain – Smart Agriculture System

FarmBrain is a Python-based Smart Agriculture System developed using machine-learning, deep-learning, computer-vision, and Streamlit technologies.

The project provides an interactive web dashboard with different agriculture-related modules such as:

- 🌱 Soil Analysis
- 🦠 Disease Detection
- 🐛 Pest Detection
- 📊 Yield Prediction

The main objective of this project is to develop an interactive agriculture application that can be extended with machine-learning models and agricultural datasets.

---

# 🛠️ Technologies Used

The project uses the following technologies and Python libraries:

- Python
- PyTorch
- TorchVision
- TensorFlow
- Scikit-learn
- NumPy
- Pandas
- Matplotlib
- OpenCV
- Pillow
- Ultralytics
- Stable-Baselines3
- Gymnasium
- Streamlit

---

# 📁 Project Structure

```text
farmbrain_project/
│
├── dashboard/
│   └── streamlit_app.py
│
├── dataset/
│   ├── diseased/
│   └── healthy/
│
├── models/
│
├── utils/
│   ├── __pycache__/
│   └── preprocessing.py
│
├── main.py
├── predict.py
├── train.py
├── requirements.txt
└── README.md

# 🚀Project Development Process
Step 1: Created the FarmBrain Project
First, I created the main project for the FarmBrain Smart Agriculture System.
The project was organized into separate folders for the dashboard, dataset, models, utilities, and Python scripts.
farmbrain_project/
│
├── dashboard/
├── dataset/
├── models/
├── utils/
├── main.py
├── predict.py
├── train.py
├── requirements.txt
└── README.md
📸 Project Structure
 
Step 2: Created the Dataset Structure
I created the dataset directory and organized the image categories.
dataset/
│
├── diseased/
└── healthy/
The diseased and healthy folders are used to organize agricultural images for the machine-learning workflow.
📸 Dataset Structure
 
Step 3: Created the Python Virtual Environment
To keep the project dependencies isolated from the system Python installation, I created a Python virtual environment.
python -m venv .venv
This created the following environment:
.venv/
The virtual environment keeps the project's Python packages separated from other projects.
📸 Virtual Environment
 
Step 4: Activated the Virtual Environment
On Windows PowerShell, I activated the virtual environment using:
.venv\Scripts\Activate.ps1
Initially, PowerShell prevented the activation script from running.
I temporarily changed the execution policy using:
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
Then I activated the environment again:
.venv\Scripts\Activate.ps1
The terminal displayed:
(.venv)
This confirmed that the virtual environment was active.
📸 Virtual Environment Activated
 
Step 5: Created requirements.txt
I created a requirements.txt file containing the libraries required for the FarmBrain project.
torch
torchvision
tensorflow
scikit-learn
numpy
pandas
matplotlib
opencv-python
pillow
ultralytics
stable-baselines3
gymnasium
streamlit
The purpose of this file is to define the Python dependencies required by the project.
📸 Project Requirements
 
Step 6: Installed the Required Dependencies
After activating the virtual environment, I installed the required libraries using:
pip install -r requirements.txt
The required Python packages were successfully installed.
These packages provide functionality for:
- Machine learning
- Deep learning
- Image processing
- Data processing
- Computer vision
- Streamlit dashboard development
📸 Installing Dependencies
 
Step 7: Created the Streamlit Dashboard
I created the main Streamlit application:
dashboard/
└── streamlit_app.py
The dashboard was developed using Streamlit.
The application displays the FarmBrain title:
st.title("🌱 FarmBrain Smart Agriculture System")

📸 Streamlit Dashboard Code
 
🔗 Source Code
Step 8: Added Agriculture Modules
I added a module-selection menu to the Streamlit sidebar.
The available modules are:
Soil Analysis
Disease Detection
Pest Detection
Yield Prediction
The module selector is implemented using:
choice = st.sidebar.selectbox(    "Select Module",    [        "Soil Analysis",        "Disease Detection",        "Pest Detection",        "Yield Prediction"    ])

This allows the user to select an agriculture module from the dashboard.
📸 Agriculture Modules
 
Step 9: Added Image Processing
The project uses TorchVision to process uploaded images.
The image transformation pipeline is:
transform = transforms.Compose([    transforms.Resize((224, 224)),    transforms.ToTensor()])

The uploaded image is resized to:
224 × 224
and converted into a PyTorch tensor.
This prepares the image for processing by the image model.
📸 Image Processing Code
 
Step 10: Added ResNet18 Model
I added a ResNet18 model using TorchVision.
model = resnet18(    weights=ResNet18_Weights.DEFAULT)model.eval()

The model is loaded using the default TorchVision weights and placed into evaluation mode.
This provides the image-model component used by the application.
📸 ResNet18 Model
 
Step 11: Started the FarmBrain Application
After completing the dashboard setup, I started the Streamlit application using:
python -m streamlit run dashboard\streamlit_app.py
Streamlit started the application locally.
The application was available at:
http://localhost:8501
I opened this address in my web browser to test the application.
📸 Streamlit Application Running
 
Step 12: Tested Image Upload
I tested the dashboard by selecting the Pest Detection module.
The dashboard provides an image upload option.
I uploaded a crop image through the Streamlit application.
The uploaded image was successfully displayed on the dashboard.
📸 Crop Image Upload
 
Step 13: Fixed the Streamlit Compatibility Error
During testing, I encountered the following error:
TypeError:
ImageMixin.image() got an unexpected keyword argument
'use_column_width'
The previous code was:
st.image(image, use_column_width=True)

I updated the code to:
st.image(image, width="stretch")

After making this change, the image display worked correctly.
This fixed the Streamlit image-display compatibility issue in the development environment.
📸 Streamlit Compatibility Fix
 
Step 14: Successfully Tested the Final Application
After fixing the Streamlit image-display issue, I ran the application again.
The final test successfully showed:
- 🌱 FarmBrain Smart Agriculture System
- 🐛 Pest Detection module
- 📤 Crop image upload
- 🖼️ Uploaded crop image displayed successfully
- ✅ Streamlit dashboard working
The final application was successfully tested in the local development environment.
🖥️ Final Application Output
 
📁 Final Project Structure
After completing the development work, the project contains:
farmbrain_project/
│
├── dashboard/
│   └── streamlit_app.py
│
├── dataset/
│   ├── diseased/
│   └── healthy/
│
├── models/
│
├── utils/
│   ├── __pycache__/
│   └── preprocessing.py
│
├── assets/
│   ├── 01-project-structure.png
│   ├── 02-dataset-structure.png
│   ├── 03-virtual-environment.png
│   ├── 04-activate-venv.png
│   ├── 05-requirements.png
│   ├── 06-install-dependencies.png
│   ├── 07-streamlit-dashboard-code.png
│   ├── 08-agriculture-modules.png
│   ├── 09-image-processing.png
│   ├── 10-resnet-model.png
│   ├── 11-streamlit-running.png
│   ├── 12-image-upload.png
│   ├── 13-streamlit-error-fix.png
│   └── 14-final-farmbrain-output.png
│
├── main.py
├── predict.py
├── train.py
├── requirements.txt
└── README.md
🔗 Source Code
The main project files can be accessed below:
- [📁 Dataset](dataset/)
- [🤖 Models](models/)
🔄 Project Workflow
The development workflow followed in this project was:
Create FarmBrain Project
        ↓
Create Project Structure
        ↓
Create Dataset Directories
        ↓
Create Python Virtual Environment
        ↓
Activate Virtual Environment
        ↓
Create requirements.txt
        ↓
Install Required Dependencies
        ↓
Create Streamlit Dashboard
        ↓
Add Agriculture Modules
        ↓
Add Image Processing
        ↓
Add ResNet18 Model
        ↓
Run Streamlit Application
        ↓
Test Image Upload
        ↓
Fix Streamlit Compatibility Error
        ↓
Test Application Again
        ↓
Successfully Display Uploaded Crop Image
        ↓
Prepare Project Documentation
        ↓
Upload Project to GitHub
✅ What I Completed
- [x] Created FarmBrain project
- [x] Created project folder structure
- [x] Created dataset directories
- [x] Created Python virtual environment
- [x] Activated virtual environment
- [x] Created requirements.txt
- [x] Installed required dependencies
- [x] Created Streamlit dashboard
- [x] Added agriculture module selection
- [x] Added image preprocessing
- [x] Added ResNet18 model
- [x] Started Streamlit application
- [x] Tested image upload
- [x] Fixed Streamlit image-display compatibility issue
- [x] Successfully displayed uploaded crop image
- [x] Tested the final FarmBrain dashboard
- [x] Prepared project documentation for GitHub
🔮 Future Improvements
The project can be extended with additional functionality such as:
- Add and train custom agriculture-specific models
- Improve disease detection
- Improve pest detection
- Improve soil analysis
- Improve yield prediction
- Add more agricultural datasets
- Add model performance metrics
- Add prediction confidence scores
- Add additional dashboard visualizations
- Add automated testing
- Deploy the application online
👨‍💻 Author
Venkatesh
Data Engineer
📍 Hyderabad, India
📌 Project Summary
FarmBrain is a Smart Agriculture System developed using Python, machine-learning technologies, computer-vision tools, and Streamlit.
During development, I created the project structure, organized the dataset, configured the Python environment, installed the required dependencies, developed the Streamlit dashboard, added agriculture modules, implemented image preprocessing, configured the ResNet18 model, tested image upload functionality, fixed a Streamlit compatibility issue, and successfully ran the final application.
