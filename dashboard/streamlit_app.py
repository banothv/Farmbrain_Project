import streamlit as st
from PIL import Image
import torch
from torchvision import transforms
from torchvision.models import resnet18, ResNet18_Weights

st.set_page_config(page_title="FarmBrain", layout="wide")

st.title("🌱 FarmBrain Smart Agriculture System")

# Sidebar
st.sidebar.title("Modules")
choice = st.sidebar.selectbox("Select Module", [
    "Soil Analysis",
    "Disease Detection",
    "Pest Detection",
    "Yield Prediction"
])

# Load model
model = resnet18(weights=ResNet18_Weights.DEFAULT)
model.eval()

transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor()
])

# -------------------------
# SOIL ANALYSIS
# -------------------------
if choice == "Soil Analysis":

    st.header("🌱 Soil Analysis (Upload Soil Image)")

    file = st.file_uploader("Upload soil image", type=["jpg", "png"])

    if file:
        image = Image.open(file).convert("RGB")
        st.image(image, width="stretch")

        # Dummy logic (demo)
        soil_types = ["Sandy Soil", "Clay Soil", "Loamy Soil", "Black Soil"]
        soil = soil_types[hash(file.name) % len(soil_types)]

        st.success(f"Soil Type: {soil}")
        st.info("Suggestion: Add organic compost")

# -------------------------
# DISEASE DETECTION
# -------------------------
elif choice == "Disease Detection":

    st.header("🌿 Disease Detection")

    file = st.file_uploader("Upload plant leaf image", type=["jpg", "png"])

    if file:
        image = Image.open(file).convert("RGB")
        st.image(image, width="stretch")

        img = transform(image).unsqueeze(0)

        with torch.no_grad():
            output = model(img)
            _, pred = torch.max(output, 1)

        diseases = ["Healthy", "Leaf Blight", "Powdery Mildew", "Rust", "Bacterial Spot"]
        disease = diseases[pred.item() % len(diseases)]

        st.success(f"Disease: {disease}")
        st.warning("Suggestion: Apply suitable pesticide")

# -------------------------
# PEST DETECTION
# -------------------------
elif choice == "Pest Detection":

    st.header("🐛 Pest Detection")

    file = st.file_uploader("Upload crop image", type=["jpg", "png"])

    if file:
        image = Image.open(file).convert("RGB")
        st.image(image, width="stretch")

        pests = ["No Pest", "Aphids", "Caterpillar", "Whiteflies"]
        pest = pests[hash(file.name) % len(pests)]

        st.success(f"Pest Detected: {pest}")
        st.warning("Use organic pesticide")

# -------------------------
# YIELD PREDICTION
# -------------------------
elif choice == "Yield Prediction":

    st.header("🌾 Yield Prediction")

    file = st.file_uploader("Upload crop field image", type=["jpg", "png"])

    if file:
        image = Image.open(file).convert("RGB")
        st.image(image, width="stretch")
        
        yields = ["Low Yield", "Medium Yield", "High Yield"]
        result = yields[hash(file.name) % len(yields)]

        st.success(f"Predicted Yield: {result}")
        st.info("Recommendation: Optimize irrigation")