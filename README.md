# Machine Translation Web App

This project is a web application for machine translation built using the **Hugging Face Transformers** library for natural language processing and **Flask** for web development. It allows users to input text in one language and receive translations in another language through a simple web interface.

## Features
- Supports translation between multiple language pairs (e.g., English to French, Spanish to German, etc.).
- Powered by pre-trained models from Hugging Face's Transformers library.
- Lightweight and responsive web interface built with Flask.
- Easy-to-use API for programmatic access.

## Technologies Used
- **Python**: Core programming language.
- **Hugging Face Transformers**: For loading and utilizing pre-trained translation models.
- **Flask**: A micro web framework for building the web application.
- **HTML/CSS**: For the front-end interface.
- **PyTorch/TensorFlow**: Backend frameworks for running the translation models (depending on your setup).

## Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Git (optional, for cloning the repository)

### Steps
1. **Clone the Repository**  
   git clone https://github.com/yourusername/machine-translation-webapp.git
   cd machine-translation-webapp

2. **Install Dependencies**
   pip install -r requirements.txt
   
3. **Run the Application
   python app.py
   The app will start on http://127.0.0.1:5000/ by default.
## Usage
- Open your browser and navigate to http://127.0.0.1:5000/.
- Enter the text you want to translate in the input field.
- Select the source and target languages from the dropdown menus.
- Click "Translate" to see the result.

## License
  This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments
- Hugging Face for their amazing Transformers library.
- Flask for the lightweight web framework.
