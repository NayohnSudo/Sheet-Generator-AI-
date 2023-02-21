from flask import Flask, render_template, request
import openai
import docx
import os

app = Flask(__name__)

# Initialize the API client with your API key
openai.api_key = "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"

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/generate", methods=["POST"])
def generate():
    # Get the file from the uploaded file
    file = request.files["file"]

    # Extract the text from the Word document
    document = docx.Document(file)
    text = '\n'.join([paragraph.text for paragraph in document.paragraphs])

    # Use the extracted text as the prompt for the API
    prompt = f"Create a revision sheet based on the following text:\n{text}"

    # Use the API to generate text based on the user's prompt
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1000,
        n=1,
        stop=None,
        temperature=0.5,
    )

    # Extract the generated text from the API response
    generated_text = response["choices"][0]["text"]

    # Pass the generated text to the template
    return render_template("result.html", generated_text=generated_text)

if __name__ == "__main__":
    app.run(debug=True)
