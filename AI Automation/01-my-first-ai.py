from google import genai

# 1. Client connecting
client = genai.Client(api_key="Api key")

print("AI is thinking....")

response = client.models.generate_content(
    model="gemini-1.5-flash",
    contents="Write a 2-line motivational quote for a CS student learning python."
)

print("\n--- AI Response ---")
print(response.text)
print("-------------------")
