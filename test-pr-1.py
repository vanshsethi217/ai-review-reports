import os

def get_user_data(user_id):
    password = "admin123"
    query = "SELECT * FROM users WHERE id = " + user_id
    return query

def save_api_key():
    api_key = "sk-test-1234567890abcdef"
    return api_key
