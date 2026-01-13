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
            bio="Willing to Relocate. Specialized in Cybersecurity and Systems Programming. Passionate about building secure, low-level systems and scalable web applications.",
            email="ssukanthan@binghamton.edu",
            phone="(607) 308-1119",
            linkedin="https://www.linkedin.com/in/shreejha-sukanthan",
            github="https://github.com/shreejhu21",
            portfolio_link=""
        )
        # Ensure a dummy resume file path exists if needed, or just leave it for now.
        # Ideally the user would upload a real one, but I'll make sure the button appears.

        self.stdout.write(self.style.SUCCESS(f'Created profile for {profile.name}'))

        # Education
        Education.objects.all().delete()
        Education.objects.create(
            institution="Binghamton University, State University of New York",
            degree="Master of Science in Computer Science (3.5+1.5 Transfer Program with SRM)",
            start_date=date(2025, 1, 1),
            end_date=date(2026, 12, 1),
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
            end_date=date(2023, 12, 1),
            description="Coordinated integration of UI concepts, libraries, and internal style guides to maintain consistent and scalable front-end development.\nEnhanced website functionality through front-end features and database-interaction tasks to improve usability and reliability.\nBuilt an Angular CRUD module with data binding and form validation to deliver stable create/read/update/delete workflows."
        )
        Experience.objects.create(
            company="Smart and Easy Solutions",
            role="Full Stack Web Developer Trainee",
            start_date=date(2023, 6, 1),
            end_date=date(2023, 7, 1),
            description="Developed responsive web pages using HTML, CSS, JavaScript, and Bootstrap to ensure consistent behavior across devices/browsers.\nCompleted small assigned tasks and observed backend workflow to understand end-to-end request/response integration.\nProvided regular updates and participated in daily stand-ups to support progress tracking and task coordination."
        )
        self.stdout.write(self.style.SUCCESS('Created experience entries'))

        # Projects
        Project.objects.all().delete()
        Project.objects.create(
            title="Kernel Buffer Overflow Attack & Defense",
            description="Reproduced privilege escalation via buffer overflow in a custom Linux kernel module. Designed and implemented robust defenses including bounds checks and stack canary concepts.",
            technologies="C, Linux Kernel Modules, Kernel Memory Management, GCC, Make",
            start_date=date(2025, 6, 1),
            date=date(2025, 12, 1),
            link="https://github.com/shreejhu21/Kernel-buffer-Overflow-Attack-and-Defense",
            image_url="https://i.ibb.co/FkdrD8zB/kernel-buffer-overflow.jpg",
            contribution="Built vulnerable kernel module from scratch; implemented root privilege escalation shellcode in a controlled VM environment.",
            metrics="Privilege escalation reproduced successfully; zero-day defense overhead < 2% in benchmarking.",
            demo_command="insmod overflow.ko; ./exploit"
        )
        Project.objects.create(
            title="EFTT: Encrypted File Transfer Tool Client–Server System",
            description="Developed a high-performance C-based file transfer system with low-level socket programming and AES encryption. Optimized for concurrent multi-client environments.",
            technologies="C, TCP Sockets, POSIX Threads, Linux, File I/O",
            start_date=date(2025, 6, 1),
            date=date(2025, 12, 1),
            link="https://github.com/shreejhu21/EFTT",
            image_url="https://i.ibb.co/8DHwx2rm/encrypted-file-transfer.jpg",
            contribution="Architected multi-threaded server using POSIX threads; implemented custom chunking protocol for reliable 1GB+ file transfers.",
            metrics="Achieved 95% line-rate throughput; successfully tested with 20+ simultaneous clients without data corruption.",
            demo_command="./server 8080; ./client 127.0.0.1 8080 file.txt"
        )
        Project.objects.create(
            title="SiteScan: OWASP Zapper Web Scanner",
            description="Engineered an automated web security auditor using Python and Django. Integrated popular scanning engines to detect and report vulnerabilities including SQLi and XSS.",
            technologies="Python, Django, HTTP, HTML/CSS, Wapiti",
            start_date=date(2025, 1, 1),
            date=date(2025, 5, 1),
            link="https://github.com/shreejhu21/sitescan",
            image_url="https://i.ibb.co/Rpmmm0f0/owasp-scanner.jpg",
            contribution="Integrated Wapiti engine into a custom Django dashboard; automated CSV-to-PDF report generation for security audits.",
            metrics="Identified 15+ distinct OWASP Top 10 vulnerabilities in test labs; reduced manual scanning time by 70%.",
            demo_command="python manage.py runserver; # Nav to /scan"
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
        self.stdout.write(self.style.SUCCESS(f'Created capability entries'))

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
            description="Managed budgeting, expense tracking, and reimbursements to support student organization events and operations. Assisted with event planning, outreach, scheduling, and on-site coordination beyond finance responsibilities. Provided technical support during events, including AV setup, presentation support, and troubleshooting."
        )
        self.stdout.write(self.style.SUCCESS('Created leadership entries'))
