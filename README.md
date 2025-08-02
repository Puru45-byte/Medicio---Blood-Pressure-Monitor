# Medicio - Blood Pressure Monitor

Medicio is a web application designed to help users monitor their blood pressure levels and stay proactive about heart health. Built with Flask, it provides an easy-to-use interface for inputting patient data, viewing predictions, and learning about blood pressure management.

## Features
- User-friendly web interface
- Blood pressure prediction using a trained machine learning model
- Informative sections about blood pressure stages and risk factors
- Responsive design with Bootstrap
- Secure form for patient data input

## Project Structure
```
app.py                  # Main Flask application
train_model.py          # Script to train the ML model
model.pkl               # Saved machine learning model
patient_data.csv        # Sample patient data
static/                 # Static files (images, CSS, favicon)
templates/              # HTML templates
```

## Getting Started
### Prerequisites
- Python 3.8+
- pip

### Installation
1. Clone the repository:
   ```
   git clone <your-repo-url>
   cd smartbridge
   ```
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. (Optional) Train the model:
   ```
   python train_model.py
   ```
4. Run the application:
   ```
   python app.py
   ```
5. Open your browser and go to `http://localhost:5000`

## Usage
- Visit the homepage for information about blood pressure.
- Use the "Check your Blood Pressure" button to input your data and get predictions.
- View details and learn more about maintaining healthy blood pressure.

## Contributing
Contributions are welcome! Please open issues or submit pull requests for improvements.

## License
This project is licensed under the MIT License.

## Contact
For questions or support, contact: info@medicio.com
