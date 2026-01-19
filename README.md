# Smart Study Assistant

## Overview

The AI Study Assistant is a web-based application that uses Google Cloud Vertex AI to help students study more efficiently. The app is built with Streamlit, which provides a simple and interactive user interface, while Vertex AI is responsible for all the intelligent processing behind the scenes.

Vertex AI powers the application using the Gemini 2.5 Flash model, which can understand both text and images. When a user uploads study material—such as typed notes, pictures of textbook pages, handwritten notes, or PDF files—Vertex AI analyzes the content and understands what it is about. It can read the text, extract important ideas, and make sense of visual information without needing separate tools for text extraction or image recognition.

The main purpose of the AI Study Assistant is to reduce the effort needed to study. Instead of spending a lot of time reading long chapters or organizing notes manually, students can upload their material and the application generates clear summaries, key definitions, and self-test questions, which makes revision faster and easier.

## Features

The AI Study Assistant includes a range of features that are designed to make studying easier and more efficient. Users can upload different types of study materials, including plain text, images of textbook pages, and pdf files of materials. The application processes this input and converts it into organized and easy-to-read study content. The output focuses on highlighting important ideas and concepts, helping users understand the material without having to go through everything manually. The clean and simple user interface ensures that users can interact with the application without any confusion.

## Technologies Used

- Streamlit: Used to build the web-based user interface, allowing users to interact with the application easily through a browser.

- Python: Serves as the main programming language for implementing the application logic and handling data processing.

- Google Cloud Vertex AI: Provides access to cloud-based artificial intelligence services that power the application’s core functionality.


- Gemini 2.5 Flash: The AI model used to analyze both text, image and pdf inputs and generate structured study content.
