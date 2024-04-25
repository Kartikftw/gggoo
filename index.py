class Resume:
    def __init__(self, name, contact_info, objective, education, experience, skills):
        self.name = name
        self.contact_info = contact_info
        self.objective = objective
        self.education = education
        self.experience = experience
        self.skills = skills

    def display_resume(self):
        print("Resume of " + self.name)
        print("Contact Information:")
        for key, value in self.contact_info.items():
            print(f"{key}: {value}")
        print("\nObjective:")
        print(self.objective)
        print("\nEducation:")
        for degree in self.education:
            print("- " + degree)
        print("\nExperience:")
        for job in self.experience:
            print("- " + job)
        print("\nSkills:")
        for skill in self.skills:
            print("- " + skill)

# Example data for a resume
contact_info = {
    "Address": "Ratangarh",
    "Phone": "1234567890",
    "Email": "sharmakartik163@gmail.com"
}

objective = "To obtain a position in software development where I can utilize my skills and experience to contribute to the success of the team."

education = [
    "Bachelor of Science in Computer Science, University Name, Year",
    "High School Diploma, High School Name, Year"
]

experience = [
    "Software Engineer Intern, Company Name, Year",
    "Web Developer, Company Name, Year"
]

skills = [
    "Python",
    "Java",
    "HTML/CSS",
    "JavaScript",
    "SQL"
]

my_resume = Resume("Kartik Sharma", contact_info, objective, education, experience, skills)
my_resume.display_resume()
