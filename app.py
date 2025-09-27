from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import requests
import json
import os
from datetime import datetime
from medical_knowledge import get_medical_response, get_symptom_specific_advice

app = Flask(__name__)
CORS(app)

# Perplexity API configuration
PERPLEXITY_API_KEY = "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"
PERPLEXITY_URL = "https://api.perplexity.ai/chat/completions"

# Health assessment questions
HEALTH_QUESTIONS = [
    {
        "id": 1,
        "question": "What is your primary symptom or health concern?",
        "type": "text",
        "options": []
    },
    {
        "id": 2,
        "question": "How long have you been experiencing this symptom?",
        "type": "select",
        "options": ["Less than 24 hours", "1-3 days", "4-7 days", "1-2 weeks", "More than 2 weeks"]
    },
    {
        "id": 3,
        "question": "Rate the severity of your symptom (1-10 scale):",
        "type": "scale",
        "options": list(range(1, 11))
    },
    {
        "id": 4,
        "question": "Do you have any additional symptoms?",
        "type": "multiselect",
        "options": ["Fever", "Nausea", "Dizziness", "Fatigue", "Cough", "Shortness of breath", "Chest pain", "None"]
    },
    {
        "id": 5,
        "question": "Have you taken any medication recently?",
        "type": "text",
        "options": []
    }
]

# Rules-based suggestion system
def get_rules_based_suggestion(symptoms, severity, duration, additional_symptoms):
    """Generate suggestions based on predefined rules"""
    suggestions = []
    
    # High severity symptoms - immediate medical attention
    if severity >= 8:
        suggestions.append({
            "type": "urgent",
            "title": "Seek Immediate Medical Attention",
            "description": "Your symptoms are severe. Please contact emergency services or visit the nearest emergency room immediately.",
            "action": "Call 911 or go to ER"
        })
        return suggestions
    
    # Fever-related rules (enhanced with medical knowledge)
    if "fever" in symptoms.lower() or "fever" in additional_symptoms:
        if severity >= 8 or "fever" in additional_symptoms and severity >= 6:
            suggestions.append({
                "type": "urgent",
                "title": "Seek Immediate Medical Attention",
                "description": "High fever with flu-like symptoms may indicate serious complications. Contact emergency services or visit ER immediately.",
                "action": "Call 911 or go to ER"
            })
        elif severity >= 6:
            suggestions.append({
                "type": "doctor_visit",
                "title": "Schedule Doctor Visit",
                "description": "Fever with flu symptoms requires medical evaluation. Contact your healthcare provider within 24 hours.",
                "action": "Call your doctor"
            })
        else:
            suggestions.append({
                "type": "home_remedy",
                "title": "Home Care for Fever",
                "description": "Rest, stay hydrated, monitor temperature. Use acetaminophen or ibuprofen as directed. Stay home until fever-free for 24 hours.",
                "action": "Rest, hydrate, and monitor"
            })
    
    # Flu-specific rules
    flu_symptoms = ["fever", "cough", "sore throat", "runny nose", "body aches", "headache", "fatigue", "chills"]
    flu_count = sum(1 for symptom in flu_symptoms if symptom in symptoms.lower() or symptom in additional_symptoms)
    
    if flu_count >= 3 and severity >= 5:
        suggestions.append({
            "type": "doctor_visit",
            "title": "Possible Flu - See Healthcare Provider",
            "description": "Multiple flu-like symptoms detected. Consider antiviral treatment within 48 hours of symptom onset for best results.",
            "action": "Schedule appointment within 48 hours"
        })
    elif flu_count >= 2:
        suggestions.append({
            "type": "home_remedy",
            "title": "Flu-like Symptoms - Home Care",
            "description": "Rest, stay hydrated, use fever reducers, and monitor symptoms. Stay home to prevent spreading illness.",
            "action": "Rest and isolate"
        })
    
    # Headache rules
    if "headache" in symptoms.lower():
        if severity >= 7 or duration in ["More than 2 weeks"]:
            suggestions.append({
                "type": "doctor_visit",
                "title": "Consult Healthcare Provider",
                "description": "Persistent or severe headaches should be evaluated by a medical professional.",
                "action": "Schedule appointment"
            })
        else:
            suggestions.append({
                "type": "home_remedy",
                "title": "Headache Relief",
                "description": "Rest in a dark, quiet room. Apply cold compress and stay hydrated. Avoid triggers like bright lights.",
                "action": "Rest and apply cold compress"
            })
    
    # Cough and respiratory symptoms (enhanced)
    if "cough" in symptoms.lower() or "shortness of breath" in additional_symptoms:
        if "chest pain" in additional_symptoms or severity >= 7:
            suggestions.append({
                "type": "urgent",
                "title": "Respiratory Emergency",
                "description": "Chest pain with respiratory symptoms requires immediate medical attention.",
                "action": "Call 911 or go to ER"
            })
        elif "difficulty breathing" in symptoms.lower() or "shortness of breath" in additional_symptoms:
            suggestions.append({
                "type": "urgent",
                "title": "Breathing Difficulty - Emergency",
                "description": "Difficulty breathing is a medical emergency. Seek immediate care.",
                "action": "Call 911 immediately"
            })
        else:
            suggestions.append({
                "type": "home_remedy",
                "title": "Respiratory Care",
                "description": "Stay hydrated, use humidifier, rest, and monitor for worsening symptoms. Consider cough suppressants if appropriate.",
                "action": "Rest and stay hydrated"
            })
    
    # Emergency warning signs (based on CDC guidelines)
    emergency_symptoms = ["difficulty breathing", "chest pain", "severe muscle pain", "dizziness", "confusion", "seizures", "severe weakness"]
    if any(emergency in symptoms.lower() or emergency in additional_symptoms for emergency in emergency_symptoms):
        suggestions.append({
            "type": "urgent",
            "title": "Emergency Warning Signs",
            "description": "You have symptoms that require immediate medical attention. Do not delay seeking care.",
            "action": "Call 911 or go to ER immediately"
        })
    
    # General recommendations
    if not suggestions:
        if severity >= 5:
            suggestions.append({
                "type": "monitor",
                "title": "Monitor Symptoms",
                "description": "Keep track of your symptoms and seek medical attention if they worsen or persist.",
                "action": "Monitor and rest"
            })
        else:
            suggestions.append({
                "type": "home_remedy",
                "title": "General Self-Care",
                "description": "Get plenty of rest, stay hydrated, and maintain a healthy diet. Monitor symptoms for any changes.",
                "action": "Rest and maintain healthy habits"
            })
    
    return suggestions

def get_trained_medical_response(user_query):
    """Get response from comprehensive trained medical knowledge base when API is offline"""
    return get_medical_response(user_query)

def call_perplexity_api(user_query):
    """Call Perplexity API for AI-powered health suggestions with fallback to trained data"""
    headers = {
        "Authorization": f"Bearer {PERPLEXITY_API_KEY}",
        "Content-Type": "application/json"
    }
    
    # Create a health-focused prompt with medical knowledge
    prompt = f"""
    As a healthcare assistant, provide brief, general health guidance for the following symptoms: {user_query}
    
    Based on medical knowledge, please provide:
    1. Possible causes (general information only)
    2. When to seek medical attention (including emergency warning signs)
    3. General self-care recommendations
    4. Prevention tips if applicable
    
    Important medical guidelines to consider:
    - Flu symptoms include fever, cough, sore throat, runny nose, body aches, headache, fatigue, chills
    - Emergency signs: difficulty breathing, chest pain, severe muscle pain, dizziness, confusion, seizures
    - Antiviral treatment for flu is most effective within 48 hours of symptom onset
    - Stay home until fever-free for 24 hours without medication
    - High-risk groups include those over 65, under 5, pregnant, or with chronic conditions
    
    Keep the response concise and always remind the user to consult healthcare professionals for proper diagnosis.
    """
    
    data = {
        "model": "llama-3.1-sonar-small-128k-online",
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful healthcare assistant. Provide general health information only. Always recommend consulting healthcare professionals for proper medical advice."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        "max_tokens": 500,
        "temperature": 0.3
    }
    
    try:
        response = requests.post(PERPLEXITY_URL, headers=headers, json=data, timeout=10)
        response.raise_for_status()
        result = response.json()
        return result['choices'][0]['message']['content']
    except Exception as e:
        print(f"API Error: {str(e)} - Using trained medical knowledge instead")
        return get_trained_medical_response(user_query)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/health-questions')
def get_health_questions():
    return jsonify(HEALTH_QUESTIONS)

@app.route('/api/analyze-symptoms', methods=['POST'])
def analyze_symptoms():
    try:
        data = request.get_json()
        
        # Extract data from request
        primary_symptom = data.get('primary_symptom', '')
        duration = data.get('duration', '')
        severity = data.get('severity', 1)
        additional_symptoms = data.get('additional_symptoms', [])
        medication = data.get('medication', '')
        
        # Generate rules-based suggestions
        rules_suggestions = get_rules_based_suggestion(
            primary_symptom, severity, duration, additional_symptoms
        )
        
        # Create query for AI analysis
        ai_query = f"""
        Primary symptom: {primary_symptom}
        Duration: {duration}
        Severity: {severity}/10
        Additional symptoms: {', '.join(additional_symptoms) if additional_symptoms else 'None'}
        Recent medication: {medication}
        """
        
        # Get AI suggestions (with fallback to trained medical knowledge)
        ai_suggestions = call_perplexity_api(ai_query)
        
        # Prepare response
        response = {
            "timestamp": datetime.now().isoformat(),
            "rules_based_suggestions": rules_suggestions,
            "ai_suggestions": ai_suggestions,
            "assessment_summary": {
                "primary_symptom": primary_symptom,
                "severity": severity,
                "duration": duration,
                "additional_symptoms": additional_symptoms
            }
        }
        
        return jsonify(response)
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json()
        user_message = data.get('message', '')
        
        # Get AI response
        ai_response = call_perplexity_api(user_message)
        
        return jsonify({
            "response": ai_response,
            "timestamp": datetime.now().isoformat()
        })
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
