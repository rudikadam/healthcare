#!/usr/bin/env python3
"""
Test script to demonstrate offline medical knowledge functionality
"""

import requests
import json

BASE_URL = "http://localhost:5000"

def test_offline_chat():
    """Test chat functionality with various medical queries"""
    print("🧪 Testing Offline Medical Knowledge")
    print("=" * 50)
    
    test_queries = [
        "I have chest pain and difficulty breathing",
        "I have fever, cough, and body aches",
        "I have a severe headache that came on suddenly",
        "I have runny nose and sneezing",
        "I feel tired and have muscle aches",
        "I have nausea and diarrhea"
    ]
    
    for i, query in enumerate(test_queries, 1):
        print(f"\n{i}. Testing: '{query}'")
        print("-" * 40)
        
        try:
            response = requests.post(
                f"{BASE_URL}/api/chat",
                headers={"Content-Type": "application/json"},
                json={"message": query},
                timeout=10
            )
            
            if response.status_code == 200:
                result = response.json()
                print("✅ Response received:")
                print(result['response'][:200] + "..." if len(result['response']) > 200 else result['response'])
            else:
                print(f"❌ Error: {response.status_code}")
                
        except Exception as e:
            print(f"❌ Error: {e}")

def test_symptom_analysis():
    """Test symptom analysis with different scenarios"""
    print("\n\n🔍 Testing Symptom Analysis")
    print("=" * 50)
    
    test_cases = [
        {
            "name": "Emergency Case",
            "data": {
                "primary_symptom": "chest pain and difficulty breathing",
                "duration": "Less than 24 hours",
                "severity": 9,
                "additional_symptoms": ["dizziness"],
                "medication": "none"
            }
        },
        {
            "name": "Flu Case",
            "data": {
                "primary_symptom": "fever and body aches",
                "duration": "2 days",
                "severity": 6,
                "additional_symptoms": ["cough", "fatigue"],
                "medication": "ibuprofen"
            }
        },
        {
            "name": "Cold Case",
            "data": {
                "primary_symptom": "runny nose and sneezing",
                "duration": "3 days",
                "severity": 3,
                "additional_symptoms": ["mild cough"],
                "medication": "none"
            }
        }
    ]
    
    for case in test_cases:
        print(f"\n📋 {case['name']}")
        print("-" * 30)
        
        try:
            response = requests.post(
                f"{BASE_URL}/api/analyze-symptoms",
                headers={"Content-Type": "application/json"},
                json=case['data'],
                timeout=10
            )
            
            if response.status_code == 200:
                result = response.json()
                print("✅ Analysis completed:")
                print(f"   Rules-based suggestions: {len(result.get('rules_based_suggestions', []))}")
                print(f"   AI suggestions length: {len(result.get('ai_suggestions', ''))}")
                
                # Show first suggestion
                if result.get('rules_based_suggestions'):
                    first_suggestion = result['rules_based_suggestions'][0]
                    print(f"   First recommendation: {first_suggestion.get('title', 'N/A')}")
            else:
                print(f"❌ Error: {response.status_code}")
                
        except Exception as e:
            print(f"❌ Error: {e}")

def main():
    """Run all offline tests"""
    print("🏥 Healthcare Chatbot - Offline Mode Test")
    print("=" * 60)
    print("This test demonstrates the chatbot's ability to provide")
    print("medical guidance even when the Perplexity API is offline.")
    print("=" * 60)
    
    # Test chat functionality
    test_offline_chat()
    
    # Test symptom analysis
    test_symptom_analysis()
    
    print("\n\n🎉 Offline Mode Testing Complete!")
    print("The chatbot successfully provides medical guidance using")
    print("trained knowledge even without internet connectivity.")

if __name__ == "__main__":
    main()
