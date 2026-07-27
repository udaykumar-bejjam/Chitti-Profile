#!/usr/bin/env python3
"""Generate profile PDF from the Word template to preserve exact formatting."""

from __future__ import annotations

import shutil
import subprocess
from copy import deepcopy
from pathlib import Path

from docx import Document
from docx.shared import Pt, RGBColor
from docx.text.paragraph import Paragraph

ROOT = Path(__file__).resolve().parent
TEMPLATE = ROOT / "chinni_resume_fresher.docx"
OUTPUT_DOCX = ROOT / "jessika_resume.docx"
OUTPUT_PDF = ROOT / "Jessika_Seedarla_Profile.pdf"


def set_run_text(run, text: str) -> None:
    run.text = text


def set_bullet(paragraph, label: str, description: str) -> None:
    runs = paragraph.runs
    if len(runs) >= 4:
        set_run_text(runs[2], label)
        set_run_text(runs[3], description)
    elif len(runs) == 1:
        set_run_text(runs[0], f"•\t{label}{description}")


def set_body_parts(paragraph, parts: list[tuple[str, bool]]) -> None:
  # parts: [(text, is_bold_run)] mapped to existing runs in order
    runs = paragraph.runs
    for idx, (text, _) in enumerate(parts):
        if idx < len(runs):
            set_run_text(runs[idx], text)
    if len(runs) > len(parts):
        for run in runs[len(parts) :]:
            set_run_text(run, "")


def insert_paragraph_after(paragraph) -> Paragraph:
    new_p = deepcopy(paragraph._element)
    paragraph._element.addnext(new_p)
    return Paragraph(new_p, paragraph._parent)


def delete_paragraph(paragraph) -> None:
    paragraph._element.getparent().remove(paragraph._element)


def build_document() -> Document:
    doc = Document(TEMPLATE)
    p = doc.paragraphs

    set_run_text(p[0].runs[0], "Jessika ")
    set_run_text(p[0].runs[1], "Seedarla")
    set_run_text(
        p[1].runs[0],
        "M.Sc. Biotechnology (2026)  ·  Gold Medalist  ·  Fresher  ·  Entry-Level Biopharma Candidate",
    )

    set_body_parts(
        p[4],
        [
            ("Recent ", False),
            ("M.Sc. Biotechnology graduate (2026) and Gold Medalist", True),
            (" seeking an opportunity in biopharma and life sciences. Brings a strong academic record as a ", False),
            ("Rank 1 B.Sc. Biotechnology graduate", True),
            (
                " and practical laboratory exposure through dissertation research, academic projects, and analytical laboratory training. Motivated to learn industrial processes, work with SOPs, and grow in QC microbiology, analytical testing, or bioprocess support.",
                False,
            ),
        ],
    )

    set_run_text(p[8].runs[0], "M.Sc. Biotechnology – Krishna University, Machilipatnam (Gold Medal)")

    new_p = deepcopy(p[21]._element)
    p[20]._element.addnext(new_p)
    gold_para = Paragraph(new_p, p[20]._parent)
    set_bullet(
        gold_para,
        "Gold Medal in M.Sc. Biotechnology – ",
        "Awarded for outstanding academic performance at Krishna University, Machilipatnam",
    )

    p = doc.paragraphs
    set_bullet(
        p[22],
        "Ranked 1st in B.Sc. Biotechnology – ",
        "Consistently topped all semesters at Harshini Degree College",
    )
    set_bullet(
        p[23],
        "Top Scorer in Intermediate (BiPC) – ",
        "Distinction grades with special excellence in Biology",
    )
    set_bullet(
        p[24],
        "Top Scorer in Class 10 (SSC) – ",
        "Distinction with outstanding performance in Science",
    )
    set_bullet(
        p[25],
        "Merit Certificates & Scholarships – ",
        "Received multiple honors for academic excellence",
    )
    set_bullet(
        p[26],
        "Perfect Academic Record – ",
        "Maintained consistency throughout school and college",
    )

    p = doc.paragraphs
    new_p = deepcopy(p[34]._element)
    p[33]._element.addnext(new_p)
    analytical_para = Paragraph(new_p, p[33]._parent)
    set_bullet(
        analytical_para,
        "Analytical Basics – ",
        "Introductory HPLC exposure and strong academic grounding in scientific analysis",
    )

    p = doc.paragraphs
    set_bullet(
        p[38],
        "Microbiology Techniques – ",
        "Bacterial culture, staining techniques, microscopy, and pure culture maintenance",
    )
    set_bullet(
        p[39],
        "Molecular Biology – ",
        "DNA extraction, gel electrophoresis, and PCR techniques",
    )
    set_bullet(
        p[40],
        "Immunology – ",
        "Basic principles of immune response and antigen-antibody interactions",
    )
    set_bullet(
        p[41],
        "Analytical Techniques – ",
        "Foundational familiarity with laboratory analysis workflows and data interpretation",
    )

    return doc


def export_pdf(docx_path: Path, pdf_path: Path) -> None:
    outdir = pdf_path.parent
    subprocess.run(
        [
            "libreoffice",
            "--headless",
            "--convert-to",
            "pdf",
            str(docx_path),
            "--outdir",
            str(outdir),
        ],
        check=True,
        capture_output=True,
        text=True,
    )
    generated = outdir / f"{docx_path.stem}.pdf"
    if generated != pdf_path:
        generated.replace(pdf_path)


def main() -> None:
    doc = build_document()
    doc.save(OUTPUT_DOCX)
    export_pdf(OUTPUT_DOCX, OUTPUT_PDF)

    for name in ("profile.pdf", "jessika_resume.pdf", "jessika_resume_print.pdf"):
        shutil.copy2(OUTPUT_PDF, ROOT / name)

    chitti = ROOT / "chitti-profile"
    if chitti.is_dir():
        shutil.copy2(OUTPUT_DOCX, chitti / "jessika_resume.docx")
        for name in (
            "Jessika_Seedarla_Profile.pdf",
            "profile.pdf",
            "jessika_resume.pdf",
            "jessika_resume_print.pdf",
        ):
            shutil.copy2(OUTPUT_PDF, chitti / name)

    print(f"Wrote {OUTPUT_PDF}")


if __name__ == "__main__":
    main()
