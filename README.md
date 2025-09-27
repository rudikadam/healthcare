# Healthcare AI Chatbot

A comprehensive healthcare chatbot prototype that allows users to log symptoms and receive AI-powered health suggestions. The system includes a 5-question health assessment, rules-based recommendation engine, and Perplexity AI integration for intelligent health insights.

## Features

- **5-Question Health Assessment**: Interactive questionnaire to analyze health symptoms
- **AI-Powered Suggestions**: Integration with Perplexity AI for intelligent health recommendations
- **Rules-Based System**: Predefined logic for common health scenarios
- **Real-time Chat Interface**: Interactive chatbot for health consultations
- **Responsive Bootstrap Frontend**: Modern, mobile-friendly user interface
- **Symptom Severity Tracking**: 1-10 scale severity assessment
- **Multi-symptom Support**: Handle multiple symptoms simultaneously

## Technology Stack

- **Backend**: Python Flask
- **Frontend**: HTML5, Bootstrap 5, JavaScript
- **AI Integration**: Perplexity AI API
- **Styling**: Bootstrap 5 with custom CSS gradients

## Setup Instructions

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Installation

1. **Clone or download the project files**

2. **Install Python dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**:
   ```bash
   python app.py
   ```

4. **Access the application**:
   Open your web browser and navigate to `http://localhost:5000`

## Usage

### Health Assessment

1. Click "Start Health Assessment" on the homepage
2. Answer the 5 health questions:
   - Primary symptom description
   - Duration of symptoms
   - Severity rating (1-10 scale)
   - Additional symptoms (multiple choice)
   - Recent medication usage
3. Click "Get Analysis" to receive recommendations

### AI Chat

1. Navigate to the "AI Chat" section
2. Type your health-related questions
3. Receive AI-powered responses and suggestions

## API Endpoints

- `GET /` - Main application page
- `GET /api/health-questions` - Retrieve health assessment questions
- `POST /api/analyze-symptoms` - Analyze symptoms and get recommendations
- `POST /api/chat` - Send chat messages to AI

## Health Assessment Questions

1. **Primary Symptom**: Free-text description of main health concern
2. **Duration**: How long symptoms have been present
3. **Severity**: 1-10 scale rating of symptom intensity
4. **Additional Symptoms**: Multiple choice selection of related symptoms
5. **Medication**: Recent medication usage information

## Rules-Based Recommendations

The system includes predefined rules for common health scenarios:

- **High Severity (8-10)**: Immediate medical attention recommended
- **Fever**: Temperature-based recommendations
- **Headache**: Duration and severity-based guidance
- **Respiratory Symptoms**: Cough and breathing-related advice
- **General Care**: Rest, hydration, and monitoring recommendations

## AI Integration

The chatbot uses Perplexity AI API to provide:
- General health information
- Symptom analysis
- When to seek medical attention
- Self-care recommendations

## Important Disclaimers

⚠️ **Medical Disclaimer**: This application is for informational purposes only and should not replace professional medical advice. Always consult healthcare professionals for proper diagnosis and treatment.

## File Structure

```
healthcarechatbot/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── templates/
│   └── index.html        # Main HTML template
└── README.md             # This file
```

## Customization

### Adding New Health Rules

Edit the `get_rules_based_suggestion()` function in `app.py` to add new health assessment rules.

### Modifying Questions

Update the `HEALTH_QUESTIONS` array in `app.py` to modify the assessment questionnaire.

### Styling Changes

Modify the CSS in the `<style>` section of `templates/index.html` to customize the appearance.

## Troubleshooting

### Common Issues

1. **Port already in use**: Change the port in `app.py` (line 150)
2. **API errors**: Check your Perplexity API key
3. **Module not found**: Ensure all dependencies are installed with `pip install -r requirements.txt`

### Support

For technical issues or questions, please check the console output for error messages and ensure all dependencies are properly installed.

## License

This project is for educational and demonstration purposes. Please ensure compliance with Perplexity AI's terms of service when using their API.
