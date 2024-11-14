from flask import Flask, render_template, request
from PyPDF2 import PdfReader
import random

app = Flask(__name__)

# Function to extract text from a PDF
def extract_text_from_pdf(pdf_path):
    reader = PdfReader(pdf_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text()  # Extract text from each page
    return text

# Function to generate questions from extracted text
def generate_mcqs(text, num_questions=5):
    # Placeholder question generation logic
    questions = []
    sentences = text.split('.')
    
    for i in range(min(num_questions, len(sentences))):
        question = sentences[i]
        options = [f"Option {j}" for j in range(1, 5)]  # Example options
        correct_answer = options[0]  # Assume option 1 is correct (for demo)
        random.shuffle(options)  # Randomize options

        questions.append({
            'question': question,
            'options': options,
            'answer': correct_answer
        })
    
    return questions

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['file']
        num_questions = int(request.form['num_questions'])

        # Extract text from the uploaded PDF file
        text = extract_text_from_pdf(file)
        
        # Generate MCQs from the extracted text
        mcqs = generate_mcqs(text, num_questions)
        
        # Render the results page with generated MCQs
        return render_template('results.html', mcqs=mcqs)
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
