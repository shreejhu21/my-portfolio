from django.core.management.base import BaseCommand
from portfolio.models import Profile, Education, Experience, Project, Skill, Capability, Certification, Leadership
from datetime import date

class Command(BaseCommand):
    help = 'Populates the database with resume data'

    def handle(self, *args, **kwargs):
        # Profile
        Profile.objects.all().delete()
        profile = Profile.objects.create(
            name="Shreejha Sukanthan",
            title="Master of Science in Computer Science Student",
            bio="Willing to Relocate. Passionate about Cybersecurity, Systems Programming, and Full Stack Development.",
            email="ssukanthan@binghamton.edu",
            phone="(607) 308-1119",
            linkedin="https://www.linkedin.com/in/shreejha-sukanthan",
            github="https://github.com/shreejhu21",
            portfolio_link=""
        )
        self.stdout.write(self.style.SUCCESS(f'Created profile for {profile.name}'))

        # Education
        Education.objects.all().delete()
        Education.objects.create(
            institution="Binghamton University, State University of New York",
            degree="Master of Science in Computer Science",
            start_date=date(2025, 1, 1), # Approximate based on Exp Dec 2026
            end_date=date(2026, 12, 31),
            gpa="3.14/4.00",
            coursework="Design & Analysis of Algorithms, Systems Programming, Database Systems, Computer Networks, Science of Cybersecurity, Introduction to Computer Security"
        )
        Education.objects.create(
            institution="SRM Institute of Science & Technology Ramapuram, Chennai, India",
            degree="Bachelor of Technology in Computer Science and Engineering with specialization in cybersecurity",
            end_date=date(2025, 5, 1),
            coursework="Data Structures and Algorithms, Object-Oriented Programming, Operating Systems"
        )
        self.stdout.write(self.style.SUCCESS('Created education entries'))

        # Experience
        Experience.objects.all().delete()
        Experience.objects.create(
            company="iByteCode Technologies Pvt Ltd",
            role="JavaScript Developer Intern",
            start_date=date(2023, 6, 1),
            end_date=date(2023, 12, 31),
            description="Coordinated integration of UI concepts, libraries, and internal style guides to maintain consistent and scalable front-end development.\nEnhanced website functionality through front-end features and database-interaction tasks to improve usability and reliability.\nBuilt an Angular CRUD module with data binding and form validation to deliver stable create/read/update/delete workflows."
        )
        Experience.objects.create(
            company="Smart and Easy Solutions",
            role="Full Stack Web Developer Trainee",
            start_date=date(2023, 6, 1),
            end_date=date(2023, 7, 31),
            description="Developed responsive web pages using HTML, CSS, JavaScript, and Bootstrap to ensure consistent behavior across devices/browsers.\nCompleted small assigned tasks and observed backend workflow to understand end-to-end request/response integration.\nProvided regular updates and participated in daily stand-ups to support progress tracking and task coordination."
        )
        self.stdout.write(self.style.SUCCESS('Created experience entries'))

        # Projects
        Project.objects.all().delete()
        Project.objects.create(
            title="Kernel Buffer Overflow Attack & Defense",
            description="Demonstrated a buffer overflow vulnerability in a custom Linux kernel module. Developed a proof-of-concept exploit to gain root privileges and implemented a patch using secure coding practices (bounds checking).",
            technologies="C, Linux Kernel, Assembly, GDB, Bash",
            date=date(2023, 11, 1),
            link="https://github.com/shreejhu21/Kernel-buffer-Overflow-Attack-and-Defense",
            image="projects/kernel_buffer_overflow.png"
        )
        Project.objects.create(
            title="EFTT: Encrypted File Transfer Tool",
            description="Built a secure file transfer application using Python and TCP sockets. Implemented AES-256 encryption for data confidentiality and RSA for key exchange. Features include integrity checks (SHA-256) and user authentication.",
            technologies="Python, Cryptography, TCP/IP, Socket Programming",
            date=date(2023, 5, 15),
            link="https://github.com/shreejhu21/EFTT",
            image="projects/encrypted_file_transfer.png"
        )
        Project.objects.create(
            title="SiteScan: OWASP Zapper Web Scanner",
            description="Developed a lightweight web vulnerability scanner inspired by OWASP ZAP. Detects common vulnerabilities like SQL Injection and XSS using heuristic analysis and payload injection. Generates detailed HTML reports.",
            technologies="Python, Requests, BeautifulSoup, HTML/CSS",
            date=date(2024, 1, 20),
            link="https://github.com/shreejhu21/sitescan",
            image="projects/owasp_scanner.png"
        )
        self.stdout.write(self.style.SUCCESS('Created project entries'))

        # Skills
        Skill.objects.all().delete()
        skills_data = {
            'LANG': ['Python', 'C', 'C++', 'JavaScript', 'SQL'],
            'FRAME': ['Django', 'Angular', 'HTML', 'CSS', 'Bootstrap', 'REST APIs'],
            'DB': ['PostgreSQL', 'MongoDB', 'Git', 'GitHub', 'Docker', 'Linux', 'Visual Studio Code'],
            'CONC': ['Data Structures & Algorithms', 'Object-Oriented Programming', 'Database Management Systems', 'Operating Systems', 'Computer Networks', 'TCP/IP', 'Multithreading', 'Memory Management', 'Web Security']
        }
        
        for category, skills in skills_data.items():
            for skill_name in skills:
                Skill.objects.create(name=skill_name, category=category)
        
        self.stdout.write(self.style.SUCCESS('Created skill entries'))

        # Capabilities
        Capability.objects.all().delete()
        Capability.objects.create(
            title="Full Stack Development",
            description="Building scalable web applications with Django, Angular, and modern JavaScript. Expertise in RESTful APIs and responsive UI design.",
            icon="fas fa-layer-group"
        )
        Capability.objects.create(
            title="Systems Programming",
            description="Low-level programming with C/C++, memory management, and Linux kernel module development. Understanding of OS internals and multithreading.",
            icon="fas fa-microchip"
        )
        Capability.objects.create(
            title="Database Management",
            description="Designing efficient database schemas and managing data with PostgreSQL and MongoDB. Proficient in SQL and ORM technologies.",
            icon="fas fa-database"
        )
        Capability.objects.create(
            title="Cybersecurity & Network Security",
            description="Vulnerability assessment, secure coding practices, and network defense strategies. Experience with OWASP tools and kernel-level security.",
            icon="fas fa-shield-alt"
        )
        self.stdout.write(self.style.SUCCESS('Created capability entries'))

        # Certifications
        Certification.objects.all().delete()
        Certification.objects.create(
            name="Python Crash Course",
            issuer="Google",
            date=date(2022, 8, 1)
        )
        Certification.objects.create(
            name="HTML with JavaScript",
            issuer="SRM Axis",
            date=date(2021, 5, 1)
        )
        self.stdout.write(self.style.SUCCESS('Created certification entries'))

        # Leadership
        Leadership.objects.all().delete()
        Leadership.objects.create(
            role="Treasurer",
            organization="CS-GSO (Computer Science Graduate Student Organization)",
            description="Managed budget allocation for student events and coordinated with university administration."
        )
        self.stdout.write(self.style.SUCCESS('Created leadership entries'))
