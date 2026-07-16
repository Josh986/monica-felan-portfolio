#!/usr/bin/env python3
"""Generate 4 food technologist-specific resume PDFs for Monica D. Felán."""
import os
from weasyprint import HTML

OUT_DIR = os.path.dirname(os.path.abspath(__file__))

# ------------------------------------------------------------------ #
# Shared contact / education / certs (constant across all variants)  #
# ------------------------------------------------------------------ #
NAME = "MONICA D. FELÁN"
CONTACT = ("Pasadena, TX &nbsp;|&nbsp; 979.549.6720 &nbsp;|&nbsp; "
           "felanmonica94@outlook.com &nbsp;|&nbsp; linkedin.com/in/monica-d-felan94")

CERTS = """
<div class="cert-item"><b>ServSafe Food Protection Manager Certification</b> &nbsp;&mdash;&nbsp; Valid through April 2028</div>
<div class="cert-item"><b>HACCP Certification</b> &nbsp;&mdash;&nbsp; In progress (completion expected July 2026)</div>
"""

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
  .cert-item {{ font-size: 9.3pt; color: #374151; margin-bottom: 3px; }}
  .cert-item b {{ color: #1a2744; }}
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
    <div class="row"><span class="lbl">Food Safety & Compliance:</span> {food_safety_skills}</div>
    <div class="row"><span class="lbl">Technical:</span> {tech_skills}</div>
    <div class="row"><span class="lbl">Professional:</span> {prof_skills}</div>
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
  {certs}

  <h2>Professional Development</h2>
  {pro_dev}

  <h2>Education</h2>
  {education}
</body></html>
"""


def build(target_role, summary, food_safety_skills, tech_skills, prof_skills, houston_bullets, headstart_bullets):
    hb = "".join(f"<li>{b}</li>" for b in houston_bullets)
    sb = "".join(f"<li>{b}</li>" for b in headstart_bullets)
    return TEMPLATE.format(
        name=NAME, target_role=target_role, contact=CONTACT, summary=summary,
        food_safety_skills=food_safety_skills, tech_skills=tech_skills, prof_skills=prof_skills,
        houston_bullets=hb, headstart_bullets=sb,
        certs=CERTS, pro_dev=PRO_DEV, education=EDUCATION,
    )


# ------------------------------------------------------------------ #
# Resume definitions                                                 #
# ------------------------------------------------------------------ #
resumes = {}

# ---- 1. Food Safety & Quality Assurance (FSQA) Technician ----
resumes["fsqa_tech"] = dict(
    filename="Monica_Felan_FSQA_Technician.pdf",
    target_role="Food Safety & Quality Assurance (FSQA) Technician",
    summary=("Food safety and compliance professional with 4+ years managing food operations, inventory controls, "
             "and audit-ready documentation across 3–6 service locations. ServSafe Food Protection Manager and "
             "HACCP certified (in progress), with a proven record of supporting two successful compliance audits. "
             "Strong in regulatory documentation, multi-site coordination, sanitation monitoring, and GMP adherence. "
             "Seeking an FSQA Technician role in food manufacturing to apply food safety, quality assurance, and "
             "audit-support experience."),
    food_safety_skills=("ServSafe Certified | HACCP (in progress) | Audit Preparation & Support | GMP Compliance | "
                        "Sanitation Monitoring | Food Safety Documentation | Allergen Control | Temperature Monitoring | "
                        "Regulatory Record-Keeping | Corrective Action Documentation"),
    tech_skills=("Microsoft Excel, Word, Outlook & Calendar | Inventory Management Systems | LIMS (developing) | "
                 "Data Collection & Maintenance | Report Generation | Food Safety Logs | Traceability Systems"),
    prof_skills=("Attention to Detail | Multi-Site Coordination | Critical Thinking | Training & Education | "
                 "Cross-Functional Communication | Time Management | Problem Solving"),
    houston_bullets=[
        "Maintain program data and participant records in compliance with federal nutrition program requirements, ensuring accuracy and regulatory readiness.",
        "Deliver health education and consultation while adhering to standardized protocols and documentation requirements.",
        "Compile statistical site information for program reporting and oversight.",
    ],
    headstart_bullets=[
        "Managed food safety and inventory operations across 3–6 program locations, overseeing food, milk, menus, and kitchen supplies while maintaining audit-ready documentation.",
        "Achieved two successful center audit outcomes by maintaining meticulous records of food inventory, kitchen maintenance, allergen controls, and compliance documentation.",
        "Organized and updated specialty menus, allergen lists, and site binders to support consistent food safety execution and regulatory compliance across multiple locations.",
        "Applied ServSafe food safety principles to daily operations, including temperature monitoring, sanitation verification, and supplier record maintenance.",
    ],
)

# ---- 2. Quality Control (QC) Technician ----
resumes["qc_tech"] = dict(
    filename="Monica_Felan_QC_Technician.pdf",
    target_role="Quality Control (QC) Technician",
    summary=("Quality-focused professional with a BS in Food, Nutrition, and Dietetics and 4+ years maintaining "
             "accurate operational records, conducting inspections, and ensuring compliance with food safety standards. "
             "ServSafe and HACCP certified (in progress), with hands-on experience managing inventory, performing "
             "quality checks, and supporting successful compliance audits across 3–6 locations. Strong in data collection, "
             "documentation, and attention to detail. Seeking a Quality Control Technician role in food manufacturing."),
    food_safety_skills=("ServSafe Certified | HACCP (in progress) | Quality Inspections | GMP Compliance | "
                        "Food Safety Testing (developing) | Sampling & Documentation | Product Specifications | "
                        "SOP Adherence | Deviation Reporting | Audit Support"),
    tech_skills=("Microsoft Excel (data analysis, reporting) | Microsoft Word & Outlook | LIMS (developing) | "
                 "Inventory Management Systems | Data Collection & Maintenance | Quality Logs & Records | Laboratory Equipment (developing)"),
    prof_skills=("Strong Attention to Detail | Data Accuracy | Organizational Skills | Time Management | "
                 "Critical Thinking | Team Collaboration | Communication"),
    houston_bullets=[
        "Compile and maintain accurate participant and site data, ensuring records meet program quality and compliance standards.",
        "Conduct educational sessions while maintaining documentation of program delivery and participant engagement.",
    ],
    headstart_bullets=[
        "Performed quality inspections of food, milk, and kitchen supply inventory across 3–6 locations, ensuring products met safety and program specifications.",
        "Maintained detailed quality and compliance records that supported two successful center audits with zero major findings in food safety documentation.",
        "Monitored and documented inventory controls, supplier records, and product specifications to ensure consistent quality across multiple sites.",
        "Organized specialty requirement lists and allergen documentation where accuracy and attention to detail were critical to program safety.",
    ],
)

# ---- 3. Food Safety Compliance Specialist ----
resumes["compliance"] = dict(
    filename="Monica_Felan_Food_Safety_Compliance_Specialist.pdf",
    target_role="Food Safety Compliance Specialist",
    summary=("Compliance-focused food safety professional with 4+ years managing regulatory documentation, audit "
             "preparation, and multi-site food operations. ServSafe Food Protection Manager and HACCP certified "
             "(in progress), with a proven track record of achieving two successful compliance audits across 3–6 "
             "service locations. Strong in regulatory record-keeping, traceability, corrective action documentation, "
             "and training. Seeking a Food Safety Compliance Specialist role to support manufacturing compliance, "
             "audits, and regulatory readiness."),
    food_safety_skills=("ServSafe Certified | HACCP (in progress) | Regulatory Compliance (FDA/USDA awareness) | "
                        "Audit Preparation & Support | GMP & SSOP Adherence | Traceability & Record-Keeping | "
                        "Corrective Action Documentation | Food Safety Training | Sanitation Verification | Allergen Control"),
    tech_skills=("Microsoft Excel (compliance reporting, data tracking) | Microsoft Word, Outlook & Calendar | "
                 "Inventory Management Systems | Food Safety Logs | Regulatory Documentation | Traceability Systems | "
                 "LIMS (developing) | Report Generation"),
    prof_skills=("Regulatory Knowledge | Audit Readiness | Multi-Site Coordination | Training & Education | "
                 "Problem Solving | Cross-Functional Communication | Attention to Detail | Time Management"),
    houston_bullets=[
        "Maintain regulatory documentation and participant records in compliance with federal program requirements.",
        "Deliver health education and training while adhering to standardized compliance protocols.",
        "Compile and report site data for regulatory oversight and program compliance verification.",
    ],
    headstart_bullets=[
        "Managed food safety compliance documentation across 3–6 program locations, maintaining audit-ready records that supported two successful center compliance audits.",
        "Maintained traceability records for food, milk, and supply inventory, ensuring regulatory readiness and accurate product tracking across multiple sites.",
        "Organized allergen control documentation and specialty requirement lists where compliance accuracy was essential to program safety.",
        "Applied ServSafe food safety standards to daily operations, including sanitation verification, temperature monitoring, and corrective action documentation.",
    ],
)

# ---- 4. Food Technologist (R&D / Product Development) ----
resumes["food_tech_rd"] = dict(
    filename="Monica_Felan_Food_Technologist_RD.pdf",
    target_role="Food Technologist (R&D / Product Development)",
    summary=("Food science professional with a BS in Food, Nutrition, and Dietetics and 4+ years applying nutritional "
             "knowledge, product formulation concepts, and quality standards to food program operations. ServSafe and "
             "HACCP certified (in progress), with experience developing specialty menus, managing product specifications, "
             "and coordinating multi-site program implementation. Strong in documentation, recipe/formula management, and "
             "cross-functional collaboration. Seeking a Food Technologist role in R&D or product development."),
    food_safety_skills=("ServSafe Certified | HACCP (in progress) | Product Specifications | Recipe/Formula Management | "
                        "Allergen Control & Labeling | Nutritional Analysis | Ingredient Functionality (developing) | "
                        "GMP Compliance | Sensory Evaluation (developing) | Food Safety Standards"),
    tech_skills=("Microsoft Excel (formulations, data analysis) | Microsoft Word & Outlook | Nutritional Analysis Software | "
                 "Recipe/Menu Development | Inventory Management Systems | Data Collection & Documentation | "
                 "Laboratory Equipment (developing) | Product Testing (developing)"),
    prof_skills=("Formula/Recipe Development | Attention to Detail | Project Coordination | Cross-Functional Collaboration | "
                 "Problem Solving | Time Management | Communication | Training & Education"),
    houston_bullets=[
        "Develop and deliver nutrition education programs, applying nutritional science principles to program design and participant consultation.",
        "Maintain program data and participant information with strong attention to accuracy and detail.",
    ],
    headstart_bullets=[
        "Developed and managed specialty menus and product specifications across 3–6 program locations, applying nutritional science and allergen control principles to formula development.",
        "Coordinated multi-site program implementation, managing recipe/menu documentation, ingredient lists, and product specifications to ensure consistent execution.",
        "Maintained detailed product and ingredient documentation, including allergen controls and specialty requirement lists where formula accuracy was critical.",
        "Supported two successful compliance audits by maintaining organized records of product formulations, ingredient specifications, and nutritional documentation.",
    ],
)

# ------------------------------------------------------------------ #
# Render                                                             #
# ------------------------------------------------------------------ #
for key, r in resumes.items():
    html = build(r["target_role"], r["summary"], r["food_safety_skills"], r["tech_skills"], r["prof_skills"],
                 r["houston_bullets"], r["headstart_bullets"])
    out_path = os.path.join(OUT_DIR, r["filename"])
    HTML(string=html).write_pdf(out_path)
    print(f"Generated: {r['filename']}")

print("\nAll food technologist resumes generated.")
