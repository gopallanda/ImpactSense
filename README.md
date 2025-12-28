# 🌍 ImpactSense – Earthquake Alert Prediction Platform

ImpactSense is a machine learning–powered earthquake alert prediction platform that predicts the **risk zone of a region** based on seismic parameters.  
The system classifies regions into **Green, Yellow, Orange, or Red zones**, helping in early awareness and disaster preparedness.

---

## 🚀 Features

- 🔍 Predicts earthquake alert zones using a trained ML model
- 📊 Uses key seismic parameters as input
- ⚡ FastAPI-based backend for real-time predictions
- 🌐 React-based frontend for user interaction
- ☁️ Cloud deployment using Render (backend) and Vercel (frontend)

---

## 🧠 Input Parameters

The model takes the following inputs for a region:

| Parameter | Description |
|--------|-------------|
| `magnitude` | Earthquake magnitude |
| `depth` | Depth of the earthquake |
| `cdi` | Community Determined Intensity |
| `mmi` | Modified Mercalli Intensity |
| `sig` | Significance value |

---

## 🎯 Output Zones

Based on the input values, the system predicts one of the following alert zones:

- 🟢 **Green Zone** – Low risk  
- 🟡 **Yellow Zone** – Moderate risk  
- 🟠 **Orange Zone** – High risk  
- 🔴 **Red Zone** – Severe risk  

---

## 🤖 Machine Learning Model & Performance

To build an accurate prediction system, multiple machine learning models were evaluated and compared, including:

- Linear Regression  
- Logistic Regression  
- Decision Tree  
- Random Forest  
- XGBoost  
- Gradient Boosting  

After experimentation and performance comparison, **Gradient Boosting** was selected as the final model due to its superior results.

### 🔧 Model Optimization
- Hyperparameter tuning was applied to the Gradient Boosting model
- Feature selection and data balancing techniques were used
- Model training and evaluation were performed on a balanced dataset

### ✅ Final Model Performance
- **Algorithm Used**: Gradient Boosting Classifier  
- **Accuracy Achieved**: **~95%**

The trained model was saved and loaded using a serialized file (`.pkl`) to ensure fast and consistent predictions during deployment.

## 🏗️ Project Structure

