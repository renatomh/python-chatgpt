# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 11:30:19 2023

@author: RenatoHenz

Script to create a chat wrapper for ChatGPT

References:
    * https://platform.openai.com/docs/api-reference/introduction
    * https://platform.openai.com/docs/guides/chat/introduction
    
"""

# Dependencies
import openai

# Setting the API Key (you must get one to run the script)
openai.api_key = 'YOUR_OPENAI_API_KEY'
# Defining messages list
messages = []

# While program is running
while True:
    # First, we'l get the user input
    user_input = input('> ')
    
    # Now, we'll add to the messages list in order to provide to the chatbot
    messages.append({
        "role": "user",
        "content": user_input,
        })
    
    # Making an API request to the chatbot
    res = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=messages
    )
    
    # Showing the response to the user and total tokens for the response
    print(res.choices[0].message.content)
    print(f"Total Tokens: {res.usage.total_tokens}")
    # Appending the response to the messages list
    messages.append({
        "role": "assistant",
        "content": res.choices[0].message.content,
        })
