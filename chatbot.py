#   Rule-Based AI Chatbot
#   By: Umar Saeed Jan
#   DecodeLabs Internship 2026

# Knowledge Base — Dictionary
responses = {
    'hello'         : 'Hi there! How can I help you?',
    'hi'            : 'Hello! What can I do for you?',
    'how are you'   : 'I am doing great! Thanks for asking.',
    'what is ai'    : 'AI is Artificial Intelligence — machines that think like humans!',
    'your name'     : 'I am DecodeBot, your AI assistant!',
    'help'          : 'I can answer questions about AI. Just ask me anything!',
    'what is ml'    : 'ML is Machine Learning — AI that learns from data!',
    'who made you'  : 'I was built by Umar Saeed Jan at DecodeLabs!',
    'bye'           : 'Goodbye! Have a great day!',
    'thanks'        : 'You are welcome! Anything else?'
}


# Chatbot Function
def get_response(user_input):
    # Sanitization — lowercase + strip
    clean_input = user_input.lower().strip()
    
    # Exit check
    if clean_input == 'exit':
        return None
    
    # Dictionary lookup + Fallback
    reply = responses.get(
        clean_input,
        "I do not understand that yet. Try asking something else!"
    )
    return reply


print("=" * 40)
print("   Welcome to DecodeBot! 🤖")
print("   Type 'exit' to quit")
print("=" * 40)

# Main Loop — Infinite Loop
while True:
    # Input lو
    user_input = input("\nYou: ")
    
    # get response
    reply = get_response(user_input)
    
    # Exit check
    if reply is None:
        print("Bot: Goodbye! See you next time!")
        break
    
    # Print response
    print(f"Bot: {reply}")