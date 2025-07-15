from app import criar_app
import os

app = criar_app()

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8080))  #porta railway
    app.run(host="0.0.0.0", port=port)