# Healthcare Chatbot - Offline Mode Guide

## 🚀 **Offline Medical Knowledge System**

Your healthcare chatbot now includes a comprehensive offline medical knowledge system that provides reliable health guidance even when the Perplexity API is unavailable or you're working offline.

## 🏥 **How It Works**

### **1. Dual-Mode Operation**
- **Online Mode**: Uses Perplexity AI for enhanced responses
- **Offline Mode**: Falls back to trained medical knowledge database
- **Automatic Switching**: Seamlessly switches between modes based on API availability

### **2. Comprehensive Medical Knowledge Base**

#### **Emergency Conditions Detection:**
- **Chest Pain**: Heart attack warning signs and immediate action steps
- **Breathing Difficulty**: Respiratory emergency protocols
- **Severe Headache**: Stroke and aneurysm warning signs
- **Stroke Symptoms**: FAST assessment criteria

#### **Common Conditions:**
- **Flu**: Multi-symptom detection with severity-based recommendations
- **Common Cold**: Self-care and when to seek medical attention
- **Headaches**: Different types and appropriate responses
- **Fever**: Temperature-based care guidelines

#### **Symptom-Specific Guidance:**
- Nausea and vomiting
- Diarrhea management
- Sore throat care
- Cough treatment
- Fatigue management
- Muscle aches relief

## 📊 **Knowledge Base Structure**

### **Emergency Conditions (`EMERGENCY_CONDITIONS`)**
```python
{
    "chest_pain": {
        "keywords": ["chest pain", "chest pressure", "heart pain"],
        "response": "Emergency protocol with 911 instructions"
    },
    "breathing_difficulty": {
        "keywords": ["difficulty breathing", "shortness of breath"],
        "response": "Respiratory emergency guidance"
    }
    # ... more emergency conditions
}
```

### **Common Conditions (`COMMON_CONDITIONS`)**
```python
{
    "flu": {
        "keywords": ["fever", "cough", "sore throat", "body aches"],
        "min_symptoms": 3,  # Requires 3+ symptoms to trigger
        "response": "Comprehensive flu care guidance"
    },
    "cold": {
        "keywords": ["runny nose", "sneezing", "congestion"],
        "exclude_keywords": ["fever", "body aches"],  # Excludes flu symptoms
        "response": "Cold management recommendations"
    }
    # ... more common conditions
}
```

## 🔧 **How to Use Offline Mode**

### **1. Automatic Fallback**
The system automatically detects API failures and switches to offline mode:

```python
try:
    # Try Perplexity API
    response = requests.post(PERPLEXITY_URL, ...)
    return ai_response
except Exception as e:
    # Fallback to trained medical knowledge
    return get_trained_medical_response(user_query)
```

### **2. Testing Offline Mode**
Run the offline test script to see the system in action:

```bash
python test_offline_mode.py
```

### **3. Manual Testing**
You can test offline responses by:
1. Disconnecting from internet
2. Sending chat messages
3. Running health assessments
4. Observing the trained medical responses

## 📈 **Adding New Medical Knowledge**

### **1. Add New Emergency Conditions**
```python
# In medical_knowledge.py
EMERGENCY_CONDITIONS["new_condition"] = {
    "keywords": ["symptom1", "symptom2", "symptom3"],
    "response": """🚨 EMERGENCY RESPONSE

Detailed emergency guidance here..."""
}
```

### **2. Add New Common Conditions**
```python
# In medical_knowledge.py
COMMON_CONDITIONS["new_condition"] = {
    "keywords": ["symptom1", "symptom2"],
    "min_symptoms": 2,
    "exclude_keywords": ["fever"],  # Optional
    "response": """Condition-specific guidance..."""
}
```

### **3. Add Symptom-Specific Advice**
```python
# In medical_knowledge.py
SYMPTOM_GUIDANCE["new_symptom"] = "Specific advice for this symptom..."
```

## 🎯 **Benefits of Offline Mode**

### **1. Reliability**
- Always available, even without internet
- No dependency on external services
- Consistent response quality

### **2. Speed**
- Instant responses (no API call delays)
- No network timeouts
- Immediate medical guidance

### **3. Privacy**
- No data sent to external APIs
- All processing happens locally
- Complete data control

### **4. Cost-Effective**
- No API usage costs
- No rate limiting concerns
- Unlimited usage

## 🧪 **Testing Scenarios**

### **Emergency Scenarios:**
- "I have chest pain and difficulty breathing"
- "I have a severe headache that came on suddenly"
- "I think I'm having a stroke"

### **Common Illness Scenarios:**
- "I have fever, cough, and body aches"
- "I have runny nose and sneezing"
- "I feel tired and have muscle aches"

### **Symptom-Specific Scenarios:**
- "I have nausea and vomiting"
- "I have diarrhea"
- "I have a sore throat"

## 📋 **Response Quality**

### **Emergency Responses:**
- Clear emergency indicators (🚨)
- Immediate action steps
- 911 call instructions
- Warning about time sensitivity

### **Common Condition Responses:**
- Structured self-care guidance
- When to seek medical care
- Prevention tips
- Medication recommendations

### **General Health Responses:**
- Comprehensive health guidance
- Professional consultation reminders
- Self-care best practices
- Risk group considerations

## 🔄 **Updating Medical Knowledge**

### **1. Regular Updates**
- Review and update emergency protocols
- Add new common conditions
- Update symptom guidance
- Incorporate latest medical guidelines

### **2. Version Control**
- Track changes to medical knowledge
- Test updates before deployment
- Maintain backup of working versions
- Document all modifications

### **3. Quality Assurance**
- Test all emergency scenarios
- Verify common condition responses
- Check symptom-specific advice
- Ensure professional medical accuracy

## 🎉 **Your Chatbot is Now Offline-Ready!**

Your healthcare chatbot now provides:
- ✅ **Reliable offline operation**
- ✅ **Comprehensive medical knowledge**
- ✅ **Emergency condition detection**
- ✅ **Common illness guidance**
- ✅ **Symptom-specific advice**
- ✅ **Automatic fallback system**
- ✅ **Professional medical accuracy**

The system ensures users always receive helpful medical guidance, whether online or offline! 🏥✨
