# BugWise Audio Journal
![BugWise_landingPage](https://github.com/GoodnessJames/BugWise/assets/128673364/059ef7cd-22bc-4958-b9ba-023a41a5000c)

## Introduction
Everyone deserves to have an archive of their bug fixes. It's an annoying thing to be faced with a bug you've resolved in the past but you're completely clueless on how you went about the solution. Bugs should not just be fixed but have a story too! This is why we created **BugWise**.

Bugwise transforms the debugging experience by harnessing the power of voice. It's not just a tool; it's a paradigm shift in how developers approach debugging. Developers can post a voice recording of their bug fixes alongside the bug title and provide some text annotation for context. BugWise empowers developers, from beginners to seasoned professionals, to document their debugging journey through the rich medium of audio. Now, say goodbye to text-based bug trackers and embrace a more efficient, flexible, and connected bug-fixing experience.

![Screenshot (53)](https://github.com/GoodnessJames/BugWise/assets/128673364/b6299b70-24a0-40bd-983f-08aef419c09b)

## The Context
BugWise Audio Journal serves as our Portfolio Project, marking the culmination of our Foundations Year at ALX SE (Holberton) School. Within this initiative, we had the autonomy to select both our collaborative partners and the project we wished to undertake. The sole requirement was the delivery of a functional program by the conclusion of the three-week development period.

## The Team
We are two content creation enthusiasts who are passionate about coding but also like to keep it fun!
-  [Goodness James, Akoma](https://linkedin.com/in/goodness-akoma) - Transcriber, Cybersecurity specialist, Skin-care enthusiast, Cat lover but also a very talented Software Engineer.
- [Elizabeth Ginika, Nna](https://www.linkedin.com/in/ginika-elizabeth-nna-b17573117/) - Economist, Content writer, and Customer support specialist, the "fashionista touch" Software Engineer of the team.

Follow us on LinkedIn for tech-related awesomeness!

## Blog Posts
After the development phase, we each wrote a blog post to reflect on the BugWise journey.

- Goodness' article: [BugWise: Just speak your solution.](https://medium.com/@goodnessakoma/bugwise-audio-journal-a2f85f0212d2)
- Elizabeth's article: [BugWise: The paradigm shift in how developers approach debugging.](https://www.linkedin.com/posts/ginika-elizabeth-nna-b17573117_bugwise-developertools-codingjourney-activity-7155741410304917504-Zobd?utm_source=share&utm_medium=member_android)

## Tutorial
Take a tour of the deployed version at [bugwise](https://bugwise.pythonanywhere.com/)

## Key Features
Here is a little preview of our main features:
### User Registration and Authentication:
  - Securely create an account using Bugwise's user-friendly registration system.
  - Rely on robust Python frameworks for user authentication, ensuring a secure and seamless process.
![BugWise_registration](https://github.com/GoodnessJames/BugWise/assets/128673364/84b8c03f-6088-4d5d-8e27-e7bfb679f5c4)

### Voice Recording:
  - Bugwise becomes your coding companion, capturing and storing audio data with JavaScript Web API.
  - Articulate your thoughts and debugging process with ease, turning spoken words into a rich tapestry of insights.
![BugWise_voiceRecording](https://github.com/GoodnessJames/BugWise/assets/128673364/e76120e5-1cd3-471f-bef2-66d7aec09b91)

### Basic Text Input:
  - Harmoniously combine spoken explanations with traditional text annotations for a comprehensive debugging diary.
  - Seamless integration of HTML and CSS allows developers to complement audio recordings with text annotations.
![BugWise_textInput](https://github.com/GoodnessJames/BugWise/assets/128673364/4214cdd7-3c0b-4f5b-9ee1-b93ecf365b53)

## Known Bugs
Some mobile devices are not able to use the recording feature of BugWise even after granting microphone permission.

The text input of bug posts are squished vertically when viewing on mobile.

## Architecture
### Overview
Our web app is built with the Flask framework, coded mainly in Python. BugWise is back-end heavy, meaning that we focused our time and energy on developing a simple but easy-to-use app. We designed most of the User Interface, using plain CSS and HTML. We also incorporated some Bootstrap elements which offered a nice styling to the web app.
![BugWise_architecture](https://github.com/GoodnessJames/BugWise/assets/128673364/253b8a9f-8fb5-41b5-bdea-e4c0001996be)


## Built With
Python - The Backend Language

Javascript - The Media Recorder API

HTML - The Frontend Structure

CSS - The Frontend Styling

Flask - The Web Development Framework

Jinja2 - Templating Engine

SQLAlchemy - Python SQL Toolkit and Object Relational Mapper

SQLite - Database Management System

## Future
There are plenty of features that we would love to implement into BugWise in the future and they include:
- Adding a comment feature, sharing a post, and connecting with the post author.
- Include code snippets and attach images to bug posts.
- Activate the sidebar.
- Set posts to public or private.
- Include search functionality.
- Implement tags & categorize bug posts.

## Contributions
We welcome contributions! To contribute to BugWise Audio Journal, follow these steps:
1. Fork the repository
2. Create a new branch (git checkout -b feature/your-feature)
3. Commit your changes (git commit -am 'Add some feature')
4. Push to the branch (git push origin feature/your-feature)
5. Open a Pull Request

## Acknowledgments
**ALX SE School** - For the help, advice, and resources they provided us with during this project and our curriculum.

**Corey Schafer** - Our perennial go-to expert for Flask tutorials.

**YOU** - For reading this documentation and testing out BugWise. We hope you enjoyed the ride!

## Related Projects
[AirBnB Clone](https://github.com/GoodnessJames/AirBnB_clone_v4): A simple web app made in Python, Flask, and JQuery.

[Simple Shell](https://github.com/GoodnessJames/simple_shell): A command line interpreter that replicates the Linux shell program.
