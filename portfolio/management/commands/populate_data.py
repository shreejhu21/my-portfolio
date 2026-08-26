# -*- coding: utf-8 -*-
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
            title="M.S. Computer Science | Cybersecurity • Networking • Linux • Systems Security",
            bio=(
                "M.S. Computer Science student at Binghamton University focused on "
                "cybersecurity, networking, Linux, and systems security. Hands-on "
                "experience with TCP/IP, TCP sockets, Linux kernel security, "
                "vulnerability assessment, web security, and systems programming."
            ),
            email="ssukanthan@binghamton.edu",
            phone="",
            linkedin="https://www.linkedin.com/in/shreejha-sukanthan",
            github="https://github.com/shreejhu21",
            portfolio_link=""
        )

        self.stdout.write(self.style.SUCCESS(f'Created profile for {profile.name}'))

        # Education
        Education.objects.all().delete()
        Education.objects.create(
            institution="Binghamton University, State University of New York",
            degree="M.S. in Computer Science",
            start_date=date(2025, 1, 1),
            end_date=date(2026, 12, 1),
            gpa="",
            coursework=(
                "Computer Networks, Introduction to Computer Security, "
                "Science of Cybersecurity, Systems Programming, Database Systems, "
                "Design & Analysis of Algorithms"
            )
        )
        Education.objects.create(
            institution="SRM Institute of Science & Technology, Chennai, India",
            degree="B.Tech in Computer Science & Engineering (Cyber Security)",
            start_date=date(2021, 1, 1),
            end_date=date(2025, 5, 1),
            gpa="8.8/10",
            coursework=(
                "Information Assurance and Security, "
                "Penetration Testing & Vulnerability Assessment"
            )
        )
        self.stdout.write(self.style.SUCCESS('Created education entries'))

        # Experience
        Experience.objects.all().delete()
        Experience.objects.create(
            company="iByteCode Technologies Pvt Ltd",
            role="JavaScript Developer Intern",
            start_date=date(2023, 6, 1),
            end_date=date(2023, 12, 1),
            description=(
                "Built reusable JavaScript UI components aligned with internal standards "
                "to improve maintainability and speed up feature delivery.\n"
                "Developed an Angular CRUD application with dynamic data binding and "
                "form validation, enabling reliable create, read, update, and delete workflows.\n"
                "Integrated frontend modules with backend REST APIs and debugged end-to-end "
                "data-flow and state issues across client-server boundaries."
            )
        )
        self.stdout.write(self.style.SUCCESS('Created experience entries'))

        # Projects
        Project.objects.all().delete()
        Project.objects.create(
            title="Kernel Buffer Overflow — Attack & Defense",
            description=(
                "Implemented a vulnerable Linux kernel module in C and reproduced "
                "buffer-overflow-based privilege escalation in a controlled environment "
                "to analyze kernel memory vulnerabilities. Designed and evaluated bounds "
                "checking, input validation, and stack-canary mitigations while "
                "benchmarking mitigation overhead through micro-tests."
            ),
            technologies="C, Linux Kernel Modules, Kernel Memory Management, GCC, Make",
            date=date(2025, 1, 1),
            link="https://github.com/shreejhu21/Kernel-buffer-Overflow-Attack-and-Defense",
            image_url="https://i.ibb.co/FkdrD8zB/kernel-buffer-overflow.jpg",
            contribution=(
                "Independent project focused on kernel buffer-overflow exploitation "
                "and defensive mitigation techniques."
            ),
            metrics="",
            demo_command=""
        )
        Project.objects.create(
            title="Encrypted File Transfer Tool — Client–Server System",
            description=(
                "Implemented a TCP client in C to encrypt and transmit files with metadata, "
                "dynamic buffer management, partial-send handling, and server acknowledgments. "
                "Managed binary file I/O while developing shared socket, signal-handling, "
                "directory-management, and error-handling utilities."
            ),
            technologies="C, TCP Sockets, POSIX Threads, Linux, File I/O, XOR Cipher",
            date=date(2025, 1, 1),
            link="https://github.com/shreejhu21/EFTT",
            image_url="https://i.ibb.co/8DHwx2rm/encrypted-file-transfer.jpg",
            contribution=(
                "TCP client implementation and common utilities including socket handling, "
                "file I/O, dynamic memory management, signal handling, and error handling."
            ),
            metrics="",
            demo_command=""
        )
        Project.objects.create(
            title="Automated Web Vulnerability Scanner",
            description=(
                "Built a Django application integrating Nuclei and OWASP ZAP to automate "
                "web vulnerability scanning through a user-facing interface. Processed "
                "scanner outputs into severity-based findings and risk levels, generating "
                "structured results and downloadable security reports."
            ),
            technologies="Python, Django, HTTP, HTML/CSS, Nuclei, OWASP ZAP",
            date=date(2024, 1, 1),
            link="https://github.com/shreejhu21/sitescan",
            image_url="https://i.ibb.co/Rpmmm0f0/owasp-scanner.jpg",
            contribution=(
                "Undergraduate final-semester group project focused on Django-based "
                "scanner integration and security result processing."
            ),
            metrics="",
            demo_command=""
        )
        self.stdout.write(self.style.SUCCESS('Created project entries'))

        # Skills
        Skill.objects.all().delete()
        skills_data = {
            'PROG': [
                'Python', 'C', 'C++', 'SQL', 'JavaScript'
            ],

            'CYBER': [
                'Web Security',
                'Vulnerability Assessment',
                'SQL Injection',
                'XSS',
                'CSRF',
                'Buffer Overflow',
                'Privilege Escalation',
                'Input Validation'
            ],

            'NET': [
                'TCP/IP',
                'TCP Sockets',
                'HTTP/HTTPS',
                'DNS',
                'Routing & Switching',
                'Network Protocols'
            ],

            'SYS': [
                'Linux',
                'Linux Kernel Modules',
                'Memory Management',
                'Multithreading',
                'POSIX Threads',
                'System Calls',
                'File I/O',
                'Signal Handling'
            ],

            'TOOLS': [
                'Nuclei',
                'OWASP ZAP',
                'Docker',
                'Git',
                'GitHub',
                'GCC',
                'Make',
                'VS Code'
            ],

            'WEBDB': [
                'PostgreSQL',
                'MongoDB',
                'Django',
                'REST APIs',
                'HTML/CSS'
            ]
        }
        
        for category, skills in skills_data.items():
            for skill_name in skills:
                Skill.objects.create(name=skill_name, category=category)
        
        self.stdout.write(self.style.SUCCESS('Created skill entries'))

        # Capabilities
        Capability.objects.all().delete()
        Capability.objects.create(
            title="Cybersecurity & Vulnerability Assessment",
            description="Web security, vulnerability assessment, secure coding, and automated security testing using tools including Nuclei and OWASP ZAP.",
            icon="fas fa-shield-alt"
        )
        Capability.objects.create(
            title="Networking",
            description="TCP/IP, TCP socket programming, HTTP/HTTPS, DNS, routing and switching, and network protocol fundamentals.",
            icon="fas fa-network-wired"
        )
        Capability.objects.create(
            title="Linux & Systems Security",
            description="Linux systems, kernel modules, memory management, buffer-overflow analysis, privilege escalation, system calls, and multithreading.",
            icon="fas fa-microchip"
        )
        Capability.objects.create(
            title="Software Engineering",
            description="Building reliable applications using Python, C/C++, JavaScript, Django, REST APIs, SQL, Docker, and Git.",
            icon="fas fa-code"
        )
        self.stdout.write(self.style.SUCCESS('Created capability entries'))

        # Certifications
        Certification.objects.all().delete()
        Certification.objects.create(
            name="Crash Course on Python",
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
            description=(
                "Managed CS-GSO budgeting, expense tracking, and reimbursements to support "
                "student events and organizational operations. Provided technical support "
                "for CS-GSO events, including AV setup, presentation systems, and on-site "
                "troubleshooting."
            )
        )
        self.stdout.write(self.style.SUCCESS('Created leadership entries'))
