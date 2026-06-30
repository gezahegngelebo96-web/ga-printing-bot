import os

TOKEN = os.getenv("TOKEN")

print("RAW TOKEN:", TOKEN)

if not TOKEN:
    print("❌ TOKEN NOT FOUND IN RAILWAY")
else:
    print("✅ TOKEN FOUND")
