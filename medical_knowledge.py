"""
Medical Knowledge Database for Healthcare Chatbot
This module contains trained medical knowledge for offline operation
"""

# Emergency conditions and their responses
EMERGENCY_CONDITIONS = {
    "chest_pain": {
        "keywords": ["chest pain", "chest pressure", "heart pain", "angina"],
        "response": """🚨 CHEST PAIN - MEDICAL EMERGENCY 🚨

This could be a heart attack or other serious condition. Please:

1. Call 911 immediately
2. Sit down and rest
3. Take aspirin if available (unless allergic)
4. Do not drive yourself to the hospital

**Warning Signs:**
- Pressure, squeezing, or pain in chest
- Pain spreading to arms, neck, jaw, or back
- Shortness of breath
- Nausea, cold sweat, or lightheadedness

**Time is critical - seek immediate medical attention!**"""
    },
    
    "breathing_difficulty": {
        "keywords": ["difficulty breathing", "shortness of breath", "can't breathe", "struggling to breathe"],
        "response": """🚨 BREATHING DIFFICULTY - EMERGENCY 🚨

Difficulty breathing is a medical emergency. Please:

1. Call 911 immediately
2. Sit upright if possible
3. Try to stay calm
4. Do not lie down

**Emergency Signs:**
- Severe shortness of breath
- Blue lips or fingernails
- Chest pain with breathing
- Rapid breathing
- Inability to speak in full sentences

**Seek immediate medical care - this is life-threatening!**"""
    },
    
    "severe_headache": {
        "keywords": ["severe headache", "thunderclap headache", "worst headache", "sudden severe headache"],
        "response": """⚠️ SEVERE HEADACHE - URGENT CARE NEEDED ⚠️

A sudden, severe headache can indicate serious conditions. Please:

1. Seek medical attention immediately
2. Call 911 if very severe
3. Do not take additional pain medication
4. Note any other symptoms

**Warning Signs:**
- Sudden, severe headache (like a "thunderclap")
- Headache with fever and stiff neck
- Headache after head injury
- Headache with vision changes or weakness
- Headache that wakes you from sleep

**This requires immediate medical evaluation!**"""
    },
    
    "stroke_symptoms": {
        "keywords": ["facial drooping", "arm weakness", "speech difficulty", "stroke", "numbness", "paralysis"],
        "response": """🚨 POSSIBLE STROKE - CALL 911 IMMEDIATELY 🚨

Time is critical for stroke treatment. Please:

1. Call 911 immediately
2. Note the time symptoms started
3. Do not drive yourself

**FAST Stroke Signs:**
- F: Face drooping (one side)
- A: Arm weakness (one side)
- S: Speech difficulty (slurred or confused)
- T: Time to call 911

**Every minute counts - call 911 now!**"""
    }
}

# Common conditions and their responses
COMMON_CONDITIONS = {
    "flu": {
        "keywords": ["fever", "cough", "sore throat", "body aches", "headache", "fatigue", "chills", "runny nose"],
        "min_symptoms": 3,
        "response": """🤒 FLU-LIKE SYMPTOMS DETECTED

You appear to have multiple flu symptoms. Here's what you should know:

**Immediate Actions:**
- Rest at home and avoid contact with others
- Stay hydrated with water, herbal teas, or broths
- Monitor your temperature regularly
- Use fever reducers (acetaminophen/ibuprofen) as directed

**When to Seek Medical Care:**
- If symptoms worsen or persist beyond 7 days
- If you have difficulty breathing or chest pain
- If you're in a high-risk group (over 65, under 5, pregnant, chronic conditions)
- If fever is above 102°F (39°C) and doesn't respond to medication

**Self-Care Tips:**
- Get plenty of rest
- Drink warm fluids to soothe throat
- Use a humidifier to ease breathing
- Gargle with salt water for sore throat

**Important:** Stay home until you're fever-free for 24 hours without medication to prevent spreading illness to others."""
    },
    
    "cold": {
        "keywords": ["runny nose", "sneezing", "congestion", "mild cough", "sore throat"],
        "exclude_keywords": ["fever", "body aches"],
        "response": """🤧 COLD SYMPTOMS DETECTED

You appear to have common cold symptoms. Here's how to manage them:

**Self-Care Recommendations:**
- Rest and get plenty of sleep
- Stay hydrated with warm fluids
- Use saline nasal spray for congestion
- Gargle with salt water for sore throat
- Use a humidifier to ease breathing

**Over-the-Counter Options:**
- Decongestants for stuffy nose
- Cough suppressants for dry cough
- Pain relievers for body aches
- Throat lozenges for sore throat

**When to See a Doctor:**
- Symptoms worsen after 7-10 days
- High fever (over 100.4°F/38°C)
- Difficulty breathing
- Severe ear pain
- Symptoms that improve then worsen again

**Prevention:**
- Wash hands frequently
- Avoid close contact with sick people
- Don't share personal items
- Cover coughs and sneezes"""
    },
    
    "headache": {
        "keywords": ["headache", "head pain", "migraine"],
        "response": """🤕 HEADACHE GUIDANCE

Here's how to manage your headache:

**Immediate Relief:**
- Rest in a dark, quiet room
- Apply cold compress to forehead or neck
- Stay hydrated
- Consider over-the-counter pain relievers as directed

**When to Seek Medical Care:**
- Sudden, severe headache
- Headache with fever, stiff neck, or rash
- Headache after head injury
- Headache with vision changes, weakness, or confusion
- Headaches that are getting worse
- New headaches after age 50

**Prevention Tips:**
- Maintain regular sleep schedule
- Stay hydrated
- Manage stress
- Avoid known triggers
- Limit caffeine and alcohol

**If headache persists or worsens, consult your healthcare provider.**"""
    },
    
    "fever": {
        "keywords": ["fever", "high temperature", "hot", "chills"],
        "response": """🌡️ FEVER MANAGEMENT

Here's how to manage your fever:

**Immediate Care:**
- Rest and stay hydrated
- Use fever reducers (acetaminophen/ibuprofen) as directed
- Apply cool compresses
- Wear light clothing
- Monitor temperature regularly

**When to Seek Medical Care:**
- Fever above 102°F (39°C) in adults
- Fever above 100.4°F (38°C) in infants under 3 months
- Fever lasting more than 3 days
- Fever with rash, severe headache, or stiff neck
- Fever with difficulty breathing or chest pain

**High-Risk Groups (Seek Care Sooner):**
- Infants under 3 months
- Adults over 65
- Pregnant women
- People with chronic conditions

**Stay home until fever-free for 24 hours without medication.**"""
    }
}

# General health advice
GENERAL_HEALTH_ADVICE = """🏥 GENERAL HEALTH GUIDANCE

Based on your symptoms, here are some general recommendations:

**Immediate Care:**
- Rest and stay hydrated
- Monitor your symptoms closely
- Use over-the-counter medications as directed
- Apply cold or warm compresses as appropriate

**When to Seek Medical Care:**
- Symptoms worsen or don't improve
- New symptoms develop
- You're concerned about your health
- You're in a high-risk group

**Self-Care Tips:**
- Maintain good hygiene
- Get adequate sleep
- Eat nutritious foods
- Stay physically active when possible
- Manage stress levels

**Important Reminder:**
This is general information only. Always consult with healthcare professionals for proper medical advice, diagnosis, and treatment. If you have any concerns about your health, please contact your healthcare provider."""

def get_medical_response(user_query):
    """Get medical response based on trained knowledge"""
    query_lower = user_query.lower()
    
    # Check for emergency conditions first
    for condition, data in EMERGENCY_CONDITIONS.items():
        if any(keyword in query_lower for keyword in data["keywords"]):
            return data["response"]
    
    # Check for common conditions
    for condition, data in COMMON_CONDITIONS.items():
        if "keywords" in data:
            keyword_matches = sum(1 for keyword in data["keywords"] if keyword in query_lower)
            
            # Check if we have enough symptoms to match this condition
            if keyword_matches >= data.get("min_symptoms", 1):
                # Check for exclusion keywords
                if "exclude_keywords" in data:
                    if any(exclude in query_lower for exclude in data["exclude_keywords"]):
                        continue
                
                return data["response"]
    
    # Return general health advice if no specific condition matches
    return GENERAL_HEALTH_ADVICE

# Additional medical knowledge for specific symptoms
SYMPTOM_GUIDANCE = {
    "nausea": "Rest, stay hydrated with small sips of water, avoid strong smells, eat bland foods like crackers or toast.",
    "diarrhea": "Stay hydrated, eat bland foods, avoid dairy and fatty foods, consider over-the-counter anti-diarrheal medication.",
    "sore_throat": "Gargle with salt water, drink warm fluids, use throat lozenges, rest your voice.",
    "cough": "Stay hydrated, use a humidifier, consider cough suppressants for dry cough, expectorants for productive cough.",
    "fatigue": "Get adequate rest, maintain regular sleep schedule, stay hydrated, eat nutritious foods.",
    "muscle_aches": "Rest, apply heat or cold packs, gentle stretching, over-the-counter pain relievers as directed."
}

def get_symptom_specific_advice(symptom):
    """Get specific advice for individual symptoms"""
    return SYMPTOM_GUIDANCE.get(symptom.lower(), "Monitor the symptom and consult your healthcare provider if it persists or worsens.")
