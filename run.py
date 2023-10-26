from app import app
import secrets
if __name__ == '__main__':
    app.run(debug=True,port=5001)
    app.secret_key = secrets.token_hex(16)  


