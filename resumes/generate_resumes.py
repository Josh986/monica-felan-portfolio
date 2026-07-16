#!/usr/bin/env python3
"""Generate a master resume + 10 role-tailored resume PDFs for Monica D. Felán."""
import os
from weasyprint import HTML

OUT_DIR = os.path.dirname(os.path.abspath(__file__))

# ------------------------------------------------------------------ #
# Shared contact / education / certs (constant across all variants)  #
# ------------------------------------------------------------------ #
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

# ------------------------------------------------------------------ #
# HTML template                                                      #
# ------------------------------------------------------------------ #
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


# ------------------------------------------------------------------ #
# Resume definitions                                                 #
# ------------------------------------------------------------------ #
resumes = {}

# ---- MASTER (transition-ready, general) ----
resumes["master"] = dict(
    filename="Monica_Felan_Master_Resume.pdf",
    target_role="Operations, Compliance & Training Coordinator",
    summary=("Detail-oriented operations, compliance, and training professional with 4+ years coordinating "
             "multi-site programs, maintaining audit-ready records, and delivering education. Proven ability to "
             "manage inventory and specialized requirements across 3–6 locations, build controlled documentation, "
             "and support successful compliance audits. Strong organizational, communication, and reporting skills "
             "seeking a mid-level operations, compliance, or coordination role."),
    prof_skills=("Multi-Site Coordination | Compliance Documentation | Audit Preparation | Record & Report Keeping | "
                 "Training & Education Delivery | Public Speaking | Critical Thinking | Time Management | Team Collaboration"),
    tech_skills=("Microsoft Excel, Word, Outlook & Calendar | Zoom | Inventory Management Systems | Inventory Reordering | "
                 "Data Collection & Maintenance | Report Generation | Audit Documentation"),
    houston_bullets=[
        "Develop and deliver health education and consultation to program clients and their families across a high-volume public program.",
        "Facilitate classes and educational programs, distributing accurate program information to participants and the community.",
        "Compile and maintain statistical site and participant data, ensuring records remain accurate and current.",
    ],
    headstart_bullets=[
        "Coordinated inventory of food, milk, menus, and supplies across 3–6 program locations, maintaining accurate operational records.",
        "Organized, labeled, and updated specialized requirement lists, site binders, and documentation to support consistent multi-site execution.",
        "Delivered two successful center audit outcomes by maintaining audit-ready records and reports covering inventory, maintenance, and compliance concerns.",
    ],
)

# 1. Supply Chain Compliance Specialist
resumes["supply_chain"] = dict(
    filename="Monica_Felan_Supply_Chain_Compliance_Specialist.pdf",
    target_role="Supply Chain Compliance Specialist",
    summary=("Operations and compliance professional with 4+ years managing inventory, replenishment, and "
             "compliance documentation across 3–6 service locations. Skilled in inventory controls, reordering, "
             "operational reporting, and audit preparation, with a track record of maintaining audit-ready records "
             "that supported successful center audits. Seeking to apply multi-site inventory and compliance "
             "experience within a supply chain operations environment."),
    prof_skills=("Inventory Controls | Replenishment & Reordering | Multi-Site Operations | Compliance Documentation | "
                 "Operational Reporting | Audit Preparation | Record Keeping | Critical Thinking | Time Management"),
    tech_skills=("Inventory Management Systems | Inventory Reordering | Microsoft Excel | Report Generation | "
                 "Data Collection & Maintenance | Microsoft Word, Outlook & Calendar | Zoom"),
    houston_bullets=[
        "Compile and maintain statistical site and participant data, ensuring accuracy and completeness of operational records.",
        "Deliver program education and communicate operational updates across teams and locations.",
    ],
    headstart_bullets=[
        "Coordinated inventory, replenishment records, and compliance documentation across 3–6 service locations, helping maintain audit-ready operations.",
        "Managed food, milk, and supply inventory using inventory management systems and reordering workflows to keep sites consistently stocked.",
        "Contributed to two successful center audit outcomes by maintaining accurate inventory reports and compliance documentation.",
    ],
)

# 2. QMS Coordinator
resumes["qms"] = dict(
    filename="Monica_Felan_QMS_Coordinator.pdf",
    target_role="Quality Management Systems (QMS) Coordinator",
    summary=("Documentation-focused operations professional with 4+ years maintaining standardized, audit-ready "
             "records across multiple locations. Experienced in building controlled documentation, site binders, "
             "and specialized requirement lists, and in demonstrating audit readiness through disciplined record "
             "and report keeping. Seeking a QMS Coordinator role leveraging strong documentation control and "
             "audit-support experience."),
    prof_skills=("Document Control | Audit Readiness | Process Consistency | Compliance Documentation | "
                 "Record & Report Keeping | Critical Thinking | Attention to Detail | Team Collaboration"),
    tech_skills=("Microsoft Excel, Word & Outlook | Report Generation | Data Collection & Maintenance | "
                 "Inventory Management Systems | Audit Documentation | Zoom"),
    houston_bullets=[
        "Compile and maintain statistical site and participant records with a focus on accuracy and consistency.",
        "Communicate standardized program information across teams and locations.",
    ],
    headstart_bullets=[
        "Maintained standardized, audit-ready operational records—including specialized requirement documentation, inventory reports, and site binders—to support consistent execution across multiple locations.",
        "Built and updated organized binders, menus, and specialty lists, applying critical thinking to specialized dietary and allergy requirements where accuracy was essential.",
        "Demonstrated audit readiness that contributed to two successful center audit outcomes.",
    ],
)

# 3. Renewable Energy Project Coordinator
resumes["renewable"] = dict(
    filename="Monica_Felan_Renewable_Energy_Project_Coordinator.pdf",
    target_role="Renewable Energy Project Coordinator",
    summary=("Multi-site program coordinator with 4+ years organizing requirements, records, calendars, and "
             "stakeholder communication across 3–6 locations. Strong in scheduling, documentation, reporting, and "
             "implementation support, with excellent presentation and time-management skills. Seeking a project "
             "coordinator role supporting renewable energy initiatives."),
    prof_skills=("Project Coordination | Stakeholder Communication | Scheduling & Calendars | Documentation | "
                 "Status Reporting | Implementation Support | Public Speaking | Time Management"),
    tech_skills=("Microsoft Excel, Word, Outlook & Calendar | Zoom | Report Generation | "
                 "Data Collection & Maintenance | Inventory Management Systems"),
    houston_bullets=[
        "Coordinate classes, programs, and schedules while communicating updates to stakeholders and the community.",
        "Compile and maintain site and participant records to support timely, organized program execution.",
    ],
    headstart_bullets=[
        "Coordinated multi-site program operations by organizing requirements, maintaining accurate records, communicating updates, and supporting timely execution across 3–6 locations.",
        "Managed calendars, inventory, and documentation across several sites, tracking multiple moving parts simultaneously.",
        "Maintained reports and records that supported two successful center audit outcomes.",
    ],
)

# 4. EHS Training Coordinator
resumes["ehs"] = dict(
    filename="Monica_Felan_EHS_Training_Coordinator.pdf",
    target_role="Environmental, Health & Safety (EHS) Training Coordinator",
    summary=("Training and compliance professional with 4+ years designing and delivering educational sessions "
             "while maintaining accurate participant and program records. Combines strong facilitation, public "
             "speaking, and presentation skills with disciplined compliance documentation in record-driven "
             "environments. Seeking an EHS Training Coordinator role focused on training administration and "
             "compliance record maintenance."),
    prof_skills=("Training Administration | Education Delivery | Facilitation | Public Speaking | Presentation Skills | "
                 "Compliance Documentation | Record Keeping | Interpersonal Communication"),
    tech_skills=("Microsoft Excel, Word, Outlook & Calendar | Zoom | Report Generation | "
                 "Data Collection & Maintenance | Audit Documentation"),
    houston_bullets=[
        "Develop and deliver health education and consultation, combining clear facilitation with accurate program documentation.",
        "Conduct classes and programs, maintaining participant and program information required for compliance.",
    ],
    headstart_bullets=[
        "Designed and delivered educational sessions while maintaining accurate participant and program information across multiple sites.",
        "Maintained required records in compliance-conscious environments, supporting two successful center audit outcomes.",
        "Organized specialized requirement lists and documentation to support consistent, compliant program delivery.",
    ],
)

# 5. Aviation Operations Compliance Coordinator
resumes["aviation"] = dict(
    filename="Monica_Felan_Aviation_Operations_Compliance_Coordinator.pdf",
    target_role="Aviation Operations Compliance Coordinator",
    summary=("Detail-oriented operations and documentation professional with 4+ years supporting procedure-driven, "
             "multi-site operations. Experienced in maintaining accurate requirement records, coordinating updates "
             "across stakeholders, and preparing documentation for successful audits. Seeking an operations "
             "compliance, document control, or training records coordinator role within aviation operations."),
    prof_skills=("Operational Documentation | Compliance Records | Multi-Site Coordination | Audit Preparation | "
                 "Cross-Team Communication | Attention to Detail | Record & Report Keeping | Time Management"),
    tech_skills=("Microsoft Excel, Word, Outlook & Calendar | Zoom | Report Generation | "
                 "Data Collection & Maintenance | Inventory Management Systems | Audit Documentation"),
    houston_bullets=[
        "Compile and maintain statistical site and participant records within a procedure-driven public program.",
        "Coordinate information and updates across teams, classrooms, and program stakeholders.",
    ],
    headstart_bullets=[
        "Supported procedure-driven, multi-site operations by maintaining accurate requirement records, coordinating updates across stakeholders, and preparing documentation for successful audits.",
        "Maintained specialized menus, allergy requirements, and maintenance records with strong detail orientation across 3–6 locations.",
        "Contributed to two successful center audit outcomes through disciplined operational documentation.",
    ],
)

# 6. Learning Operations Specialist
resumes["learning"] = dict(
    filename="Monica_Felan_Learning_Operations_Specialist.pdf",
    target_role="Learning Operations Specialist",
    summary=("Education and program operations professional with 4+ years delivering training and maintaining "
             "participant, site, and program data. Skilled in virtual facilitation using Zoom and Microsoft Office, "
             "with strong data-maintenance and reporting discipline. Seeking a Learning Operations Specialist role "
             "coordinating course operations, learner records, and virtual sessions."),
    prof_skills=("Learning Operations | Virtual Facilitation | Training Delivery | Learner Records | "
                 "Data Maintenance | Reporting | Presentation Skills | Time Management"),
    tech_skills=("Zoom | Microsoft Excel, Word, Outlook & Calendar | Report Generation | "
                 "Data Collection & Maintenance | LMS Concepts (developing)"),
    houston_bullets=[
        "Conduct classes and educational programs, using virtual tools such as Zoom to deliver consistent learning experiences.",
        "Maintain participant, site, and program data to support accurate learning-operations reporting.",
    ],
    headstart_bullets=[
        "Delivered educational programming and maintained related participant and site information, supporting consistent learning operations.",
        "Coordinated program materials, schedules, and records across 3–6 sites with strong data-maintenance discipline.",
        "Maintained records and reports that supported two successful center audit outcomes.",
    ],
)

# 7. Legal Operations Project Coordinator
resumes["legal_ops"] = dict(
    filename="Monica_Felan_Legal_Operations_Project_Coordinator.pdf",
    target_role="Legal Operations Project Coordinator",
    summary=("Process- and documentation-focused coordinator with 4+ years managing high-detail operational "
             "documentation and reporting across multiple sites. Experienced in keeping records current, organized, "
             "and available to support audit and compliance reviews, with strong cross-functional coordination and "
             "deadline awareness. Seeking a Legal Operations Project Coordinator role centered on process and "
             "project coordination."),
    prof_skills=("Process Coordination | Project Coordination | Documentation Management | Reporting | "
                 "Compliance Support | Cross-Functional Coordination | Deadline Management | Clear Communication"),
    tech_skills=("Microsoft Excel, Word, Outlook & Calendar | Zoom | Report Generation | "
                 "Data Collection & Maintenance | Audit Documentation"),
    houston_bullets=[
        "Compile and maintain detailed site and participant documentation, ensuring records are current and organized.",
        "Coordinate across teams to keep operational materials complete and deadline-ready.",
    ],
    headstart_bullets=[
        "Managed high-detail operational documentation and reporting across multiple sites, ensuring records were current, organized, and available to support audit and compliance reviews.",
        "Coordinated cross-functional information and updates across 3–6 program locations with clear communication and deadline awareness.",
        "Supported two successful center audit outcomes by keeping reports and operational materials complete and current.",
    ],
)

# 8. Implementation Operations Specialist
resumes["implementation"] = dict(
    filename="Monica_Felan_Implementation_Operations_Specialist.pdf",
    target_role="Implementation Operations Specialist",
    summary=("Operations and enablement professional with 4+ years translating specialized requirements into clear, "
             "usable materials and coordinating updates across sites. Strong in training end users, maintaining "
             "accurate data, and driving follow-through on process adoption. Seeking an Implementation Operations "
             "Specialist role centered on process, training, and adoption."),
    prof_skills=("Process Implementation | Training & Enablement | Requirement Translation | Workflow Organization | "
                 "Data Accuracy | Follow-Through | Communication | Documentation"),
    tech_skills=("Microsoft Excel, Word, Outlook & Calendar | Zoom | Report Generation | "
                 "Data Collection & Maintenance | Inventory Management Systems"),
    houston_bullets=[
        "Train and educate end users through classes, programs, consultation, and presentations.",
        "Maintain accurate participant and program data, supporting consistent process execution.",
    ],
    headstart_bullets=[
        "Translated specialized operational requirements into clear, usable materials and coordinated updates across sites, helping teams apply consistent processes.",
        "Organized lists, menus, binders, and site resources so staff could adopt standardized workflows across 3–6 locations.",
        "Maintained accurate records and documentation that supported two successful center audit outcomes.",
    ],
)

# 9. Project Controls Specialist
resumes["project_controls"] = dict(
    filename="Monica_Felan_Project_Controls_Specialist.pdf",
    target_role="Project Controls Specialist",
    summary=("Detail-oriented operations professional with 4+ years maintaining accurate multi-site operational "
             "reports, inventory information, and requirement documentation. Skilled in organized tracking, "
             "reporting, and audit-ready oversight, with strong time management and attention to detail. Seeking a "
             "project controls or project coordination role supporting schedules, status reporting, and "
             "administrative controls."),
    prof_skills=("Project Documentation | Status Reporting | Issue Tracking | Administrative Controls | "
                 "Multi-Site Reporting | Attention to Detail | Time Management | Record Keeping"),
    tech_skills=("Microsoft Excel, Word, Outlook & Calendar | Zoom | Report Generation | "
                 "Data Collection & Maintenance | Inventory Management Systems | MS Project (developing)"),
    houston_bullets=[
        "Compile and maintain statistical site and participant reports needed for operational oversight.",
        "Track and communicate program information across teams to keep records current.",
    ],
    headstart_bullets=[
        "Maintained accurate multi-site operational reports, inventory information, and requirement documentation, enabling organized tracking and audit-ready program oversight.",
        "Organized inventory, menus, maintenance information, and supply needs across 3–6 locations with strong attention to detail.",
        "Maintained reports and records that supported two successful center audit outcomes.",
    ],
)

# 10. Food Safety & Supplier Compliance Specialist
resumes["food_safety"] = dict(
    filename="Monica_Felan_Food_Safety_Supplier_Compliance_Specialist.pdf",
    target_role="Food Safety & Supplier Compliance Specialist",
    summary=("Food program and compliance professional with 4+ years overseeing food, milk, menu, and inventory "
             "documentation across 3–6 locations. ServSafe Food Protection Manager certified (through April 2028), "
             "with a proven record of maintaining audit-ready records that supported two successful center audits. "
             "Seeking a Food Safety & Supplier Compliance Specialist role within food manufacturing, distribution, "
             "or supply chain."),
    prof_skills=("Food Safety Oversight | Supplier & Inventory Compliance | Audit Preparation | "
                 "Documentation Control | Record & Report Keeping | Critical Thinking | Time Management"),
    tech_skills=("Inventory Management Systems | Inventory Reordering | Microsoft Excel, Word & Outlook | "
                 "Report Generation | Data Collection & Maintenance | Audit Documentation | HACCP (developing)"),
    houston_bullets=[
        "Develop and deliver nutrition education while maintaining accurate program records.",
        "Compile and maintain statistical site and participant data relevant to food-program compliance.",
    ],
    headstart_bullets=[
        "Oversaw food, milk, menu, kitchen-supply, and inventory documentation across 3–6 locations; maintained audit-ready records that supported two successful center audit reports.",
        "Organized specialty menus, allergy requirements, and kitchen maintenance records where food-safety accuracy was essential.",
        "Applied ServSafe-certified food safety knowledge to inventory, menu, and compliance oversight.",
    ],
)

# ------------------------------------------------------------------ #
# Render                                                             #
# ------------------------------------------------------------------ #
for key, r in resumes.items():
    html = build(r["target_role"], r["summary"], r["prof_skills"], r["tech_skills"],
                 r["houston_bullets"], r["headstart_bullets"])
    out_path = os.path.join(OUT_DIR, r["filename"])
    HTML(string=html).write_pdf(out_path)
    print(f"Generated: {r['filename']}")

print("\nAll resumes generated.")
