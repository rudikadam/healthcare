#!/usr/bin/env python3
"""
Simple test script to verify the healthcare chatbot API endpoints
"""

import requests
import json

BASE_URL = "http://localhost:5000"

def test_health_questions():
    """Test the health questions endpoint"""
    print("Testing health questions endpoint...")
    try:
        response = requests.get(f"{BASE_URL}/api/health-questions")
        if response.status_code == 200:
            questions = response.json()
            print(f"✅ Successfully retrieved {len(questions)} health questions")
            return True
        else:
            print(f"❌ Failed to get health questions: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Error testing health questions: {e}")
        return False

def test_symptom_analysis():
    """Test the symptom analysis endpoint"""
    print("\nTesting symptom analysis endpoint...")
    try:
        test_data = {
            "primary_symptom": "headache",
            "duration": "2 days",
            "severity": 6,
            "additional_symptoms": ["fever", "fatigue"],
            "medication": "ibuprofen"
        }
        
        response = requests.post(
            f"{BASE_URL}/api/analyze-symptoms",
            headers={"Content-Type": "application/json"},
            json=test_data
        )
        
        if response.status_code == 200:
            result = response.json()
            print("✅ Successfully analyzed symptoms")
            print(f"   Rules-based suggestions: {len(result.get('rules_based_suggestions', []))}")
            print(f"   AI suggestions available: {'ai_suggestions' in result}")
            return True
        else:
            print(f"❌ Failed to analyze symptoms: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Error testing symptom analysis: {e}")
        return False

def test_chat():
    """Test the chat endpoint"""
    print("\nTesting chat endpoint...")
    try:
        test_message = {"message": "I have a headache, what should I do?"}
        
        response = requests.post(
            f"{BASE_URL}/api/chat",
            headers={"Content-Type": "application/json"},
            json=test_message
        )
        
        if response.status_code == 200:
            result = response.json()
            print("✅ Successfully sent chat message")
            print(f"   Response received: {len(result.get('response', ''))} characters")
            return True
        else:
            print(f"❌ Failed to send chat message: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Error testing chat: {e}")
        return False

def main():
    """Run all tests"""
    print("🏥 Healthcare Chatbot API Test Suite")
    print("=" * 40)
    
    tests = [
        test_health_questions,
        test_symptom_analysis,
        test_chat
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        if test():
            passed += 1
    
    print(f"\n📊 Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! The API is working correctly.")
    else:
        print("⚠️  Some tests failed. Check the server logs for details.")

if __name__ == "__main__":
    main()
