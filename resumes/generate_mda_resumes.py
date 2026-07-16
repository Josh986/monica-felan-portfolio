#!/usr/bin/env python3
"""Generate 4 MD Anderson-tailored resume PDFs for Monica D. Felan.

Roles (from careers.mdanderson.org sourcing):
  1. Program Coordinator - Infectious Diseases
  2. Patient Services Coordinator - Radiation Oncology
  3. Senior Research Data Coordinator - Goal Concordant Care Research
  4. Senior Administrative Assistant - Hematopathology
"""
import os
from weasyprint import HTML

OUT_DIR = os.path.dirname(os.path.abspath(__file__))

NAME = "MONICA D. FELÁN"
CONTACT = ("Pasadena, TX &nbsp;|&nbsp; 979.549.6720 &nbsp;|&nbsp; "
           "felanmonica94@outlook.com &nbsp;|&nbsp; linkedin.com/in/monica-felan")
CERTS = "ServSafe Food Protection Manager Certification &nbsp;&mdash;&nbsp; April 2023 – April 2028"

EDUCATION = """
  <div class="entry">
    <div class="entry-head">
      <span class="ttl">Stephen F. Austin State University</span>
      <span class="loc">Nacogdoches, TX</span>
    </div>
    <div class="entry-sub">
      <span class="sub">Bachelor of Science in Food, Nutrition, and Dietetics</span>
      <span class="date">May 2019</span>
    </div>
  </div>
"""

PRO_DEV = """
  <div class="pd-line"><b>WIC Nutrition Counseling Workshop</b> &mdash; Austin, TX (June 2025)</div>
  <div class="pd-line"><b>National Child Nutrition Conference</b>, Nutrition Specialist Attendee &mdash; San Diego, CA (April 2023)</div>
  <div class="pd-line"><b>Nacogdoches Medical Center (NMC)</b>, Dietetic Intern &mdash; Nacogdoches, TX (July 2019)</div>
"""

TEMPLATE = """<!DOCTYPE html>
<html><head><meta charset="utf-8"><style>
  @page {{ size: letter; margin: 0.5in 0.6in; }}
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{ font-family: 'Helvetica Neue', Arial, sans-serif; color: #1f2937; font-size: 10pt; line-height: 1.4; }}
  .name {{ font-size: 21pt; font-weight: 800; letter-spacing: .04em; color: #1a2744; }}
  .role {{ font-size: 11.5pt; font-weight: 600; color: #2a8c8c; margin-top: 1px; letter-spacing: .02em; }}
  .contact {{ font-size: 8.6pt; color: #4b5563; margin-top: 5px; }}
  .rule {{ height: 2.5px; background: #2a8c8c; margin: 8px 0 10px; border-radius: 2px; }}
  h2 {{ font-size: 9.5pt; font-weight: 800; text-transform: uppercase; letter-spacing: .1em;
        color: #1a2744; border-bottom: 1px solid #d1d5db; padding-bottom: 2px; margin: 12px 0 6px; }}
  p.summary {{ font-size: 9.4pt; color: #374151; text-align: justify; }}
  .skills-grid {{ font-size: 9.2pt; }}
  .skills-grid .row {{ margin-bottom: 3px; }}
  .skills-grid .lbl {{ font-weight: 700; color: #1a2744; }}
  .entry {{ margin-bottom: 8px; }}
  .entry-head {{ display: flex; justify-content: space-between; }}
  .entry-head .ttl {{ font-weight: 700; color: #1a2744; font-size: 10pt; }}
  .entry-head .loc {{ color: #4b5563; font-size: 9pt; }}
  .entry-sub {{ display: flex; justify-content: space-between; }}
  .entry-sub .sub {{ font-style: italic; color: #2a8c8c; font-size: 9.3pt; font-weight: 600; }}
  .entry-sub .date {{ color: #6b7280; font-size: 8.8pt; }}
  ul {{ margin: 4px 0 0 16px; }}
  ul li {{ font-size: 9.3pt; color: #374151; margin-bottom: 2.5px; }}
  .pd-line {{ font-size: 9pt; color: #374151; margin-bottom: 3px; }}
  .cert {{ font-size: 9.3pt; color: #374151; }}
  .cert b {{ color: #1a2744; }}
</style></head>
<body>
  <div class="name">{name}</div>
  <div class="role">{target_role}</div>
  <div class="contact">{contact}</div>
  <div class="rule"></div>

  <h2>Professional Summary</h2>
  <p class="summary">{summary}</p>

  <h2>Core Skills</h2>
  <div class="skills-grid">
    <div class="row"><span class="lbl">Professional:</span> {prof_skills}</div>
    <div class="row"><span class="lbl">Technical:</span> {tech_skills}</div>
  </div>

  <h2>Work Experience</h2>
  <div class="entry">
    <div class="entry-head">
      <span class="ttl">WIC Program &mdash; Houston Health Department</span>
      <span class="loc">Houston, TX</span>
    </div>
    <div class="entry-sub">
      <span class="sub">Nutritionist</span>
      <span class="date">March 2024 – Present</span>
    </div>
    <ul>{houston_bullets}</ul>
  </div>
  <div class="entry">
    <div class="entry-head">
      <span class="ttl">Head Start of Greater Dallas</span>
      <span class="loc">Dallas, TX</span>
    </div>
    <div class="entry-sub">
      <span class="sub">Nutrition Specialist</span>
      <span class="date">February 2021 – October 2023</span>
    </div>
    <ul>{headstart_bullets}</ul>
  </div>

  <h2>Certifications</h2>
  <div class="cert">{certs}</div>

  <h2>Professional Development</h2>
  {pro_dev}

  <h2>Education</h2>
  {education}
</body></html>
"""


def build(target_role, summary, prof_skills, tech_skills, houston_bullets, headstart_bullets):
    hb = "".join(f"<li>{b}</li>" for b in houston_bullets)
    sb = "".join(f"<li>{b}</li>" for b in headstart_bullets)
    return TEMPLATE.format(
        name=NAME, target_role=target_role, contact=CONTACT, summary=summary,
        prof_skills=prof_skills, tech_skills=tech_skills,
        houston_bullets=hb, headstart_bullets=sb,
        certs=CERTS, pro_dev=PRO_DEV, education=EDUCATION,
    )


resumes = {}

# 1. Program Coordinator - Infectious Diseases
resumes["program_coordinator"] = dict(
    filename="Monica_Felan_Program_Coordinator_MDAnderson.pdf",
    target_role="Program Coordinator",
    summary=("Organized program coordination professional with 4+ years administering multi-site public health "
             "programs, maintaining compliance documentation, and serving as a liaison across teams and community "
             "stakeholders. Skilled in coordinating educational programs and events, compiling accurate reports, and "
             "maintaining controlled records that support successful audits. Seeking a Program Coordinator role where "
             "documentation discipline, coordination, and clear communication drive program success."),
    prof_skills=("Program Coordination | Stakeholder & Community Liaison | Compliance Documentation | Event & Class "
                 "Coordination | Reporting & Record Keeping | Multi-Site Operations | Public Speaking | Time Management"),
    tech_skills=("Microsoft Excel, Word, Outlook & Calendar | Zoom | Data Collection & Maintenance | "
                 "Report Generation | Scheduling & Coordination | Audit Documentation"),
    houston_bullets=[
        "Coordinate and facilitate health education classes and programs, serving as the point of contact for participants, families, and community partners.",
        "Distribute accurate program information and act as a liaison between clients and program services across a high-volume public health setting.",
        "Compile, maintain, and report statistical site and participant data, ensuring documentation stays accurate, current, and audit-ready.",
    ],
    headstart_bullets=[
        "Coordinated program operations, schedules, and specialized requirement documentation across 3–6 locations, keeping records consistent and controlled.",
        "Organized, labeled, and maintained site binders, requirement lists, and program documentation to support smooth multi-site execution.",
        "Contributed to two successful center audits by preparing and maintaining audit-ready records covering inventory, compliance, and operational concerns.",
    ],
)

# 2. Patient Services Coordinator - Radiation Oncology
resumes["patient_services"] = dict(
    filename="Monica_Felan_Patient_Services_Coordinator_MDAnderson.pdf",
    target_role="Patient Services Coordinator",
    summary=("Client-focused coordination professional with 4+ years delivering direct services to clients and "
             "families in high-volume public health settings. Experienced in scheduling coordination, accurate "
             "record-keeping, and clear communication across multiple sites. Known for a warm, professional service "
             "approach and disciplined documentation. Seeking a Patient Services Coordinator role that values "
             "compassionate client service, organization, and operational accuracy in a healthcare environment."),
    prof_skills=("Patient/Client Service | Scheduling & Appointment Coordination | Accurate Record Keeping | "
                 "Multi-Site Support | Confidential Documentation | Communication & Empathy | Problem Solving"),
    tech_skills=("Microsoft Excel, Word, Outlook & Calendar | Zoom | Scheduling Systems | Data Entry & Maintenance | "
                 "Records Management | Report Generation"),
    houston_bullets=[
        "Serve clients and their families directly in a high-volume public health program, providing information, guidance, and a professional, compassionate experience.",
        "Coordinate appointments, class scheduling, and follow-ups while maintaining accurate, confidential participant records.",
        "Compile and maintain participant data, ensuring records are current and readily accessible for reporting and service continuity.",
    ],
    headstart_bullets=[
        "Coordinated schedules, documentation, and service delivery across 3–6 program locations, maintaining accurate operational records.",
        "Maintained organized, up-to-date participant and requirement records, supporting consistent service across multiple sites.",
        "Supported two successful center audits through disciplined, audit-ready record-keeping and reporting.",
    ],
)

# 3. Senior Research Data Coordinator - Goal Concordant Care Research
resumes["research_data"] = dict(
    filename="Monica_Felan_Research_Data_Coordinator_MDAnderson.pdf",
    target_role="Senior Research Data Coordinator",
    summary=("Public health professional with 4+ years in participant engagement, health education and counseling, "
             "and data collection within regulated public program environments. Experienced in gathering and "
             "maintaining accurate participant data, administering education programs, and preserving compliance "
             "documentation. Seeking a Senior Research Data Coordinator role that leverages strong participant "
             "engagement, data discipline, and public health program experience."),
    prof_skills=("Participant Engagement | Health Education & Counseling | Data Collection & Maintenance | "
                 "Public Health Program Administration | Compliance Documentation | Reporting | Confidentiality"),
    tech_skills=("Microsoft Excel, Word, Outlook & Calendar | Zoom | Data Collection & Entry | Statistical Record "
                 "Maintenance | Report Generation | Documentation Systems"),
    houston_bullets=[
        "Engage program participants directly, delivering health education and counseling while collecting accurate participant information.",
        "Compile, enter, and maintain statistical participant and site data, ensuring completeness, accuracy, and confidentiality.",
        "Administer education programs and distribute accurate information to participants across a high-volume public health program.",
    ],
    headstart_bullets=[
        "Collected, organized, and maintained participant and program data across 3–6 sites, supporting accurate reporting and program administration.",
        "Maintained controlled documentation and requirement records in line with program compliance standards.",
        "Supported two successful center audits by maintaining accurate, audit-ready data and compliance records.",
    ],
)

# 4. Senior Administrative Assistant - Hematopathology
resumes["sr_admin_asst"] = dict(
    filename="Monica_Felan_Senior_Administrative_Assistant_MDAnderson.pdf",
    target_role="Senior Administrative Assistant",
    summary=("Detail-driven administrative professional with 4+ years managing filing systems, procurement and "
             "inventory records, compliance documentation, and report preparation across multi-site operations. "
             "Experienced in supporting leadership, maintaining controlled records, and keeping high-volume programs "
             "organized and audit-ready. Seeking a Senior Administrative Assistant role that values organization, "
             "documentation discipline, and dependable operational support."),
    prof_skills=("Administrative & Executive Support | Filing & Records Management | Procurement & Inventory Records | "
                 "Compliance Documentation | Report Preparation | Scheduling & Calendar Management | Multi-Site Operations"),
    tech_skills=("Microsoft Excel, Word, Outlook & Calendar | Zoom | Inventory & Procurement Systems | Data Entry & "
                 "Maintenance | Report Generation | Filing & Documentation Systems"),
    houston_bullets=[
        "Maintain accurate participant and program records, prepare reports, and manage documentation for a high-volume public program.",
        "Manage calendars, class scheduling, and correspondence, distributing accurate information to participants and staff.",
        "Compile and maintain statistical data and files, ensuring records remain organized, current, and audit-ready.",
    ],
    headstart_bullets=[
        "Managed procurement and inventory records for food, supplies, and specialized requirements across 3–6 locations, maintaining precise filing systems.",
        "Organized, labeled, and updated site binders, requirement lists, and compliance documentation supporting consistent multi-site administration.",
        "Prepared audit-ready records and reports that contributed to two successful center audits covering inventory, maintenance, and compliance.",
    ],
)


def main():
    for key, r in resumes.items():
        html = build(
            r["target_role"], r["summary"], r["prof_skills"], r["tech_skills"],
            r["houston_bullets"], r["headstart_bullets"],
        )
        out_path = os.path.join(OUT_DIR, r["filename"])
        HTML(string=html).write_pdf(out_path)
        print(f"✓ {r['filename']}")


if __name__ == "__main__":
    main()
