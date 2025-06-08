from __future__ import annotations

from pathlib import Path

from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph
from reportlab.platypus import SimpleDocTemplate


def create_test_files():
    test_dir = Path('test_files')
    test_dir.mkdir(exist_ok=True)

    text_file = test_dir / 'sample.txt'
    text_content = """LEGAL DOCUMENT SAMPLE

CONTRACT AGREEMENT

This agreement is made and entered into on this day, between Party A and Party B.

1. DEFINITIONS
   "Agreement" means this contract and all its attachments.
   "Parties" means Party A and Party B collectively.

2. SCOPE OF WORK
   Party A agrees to provide services as described in Appendix A.
   Party B agrees to compensate Party A as outlined in Section 3.

3. PAYMENT TERMS
   Payment shall be made within 30 days of invoice date.
   Late payments shall incur a 2% monthly interest.

4. TERMINATION
   Either party may terminate this agreement with 30 days written notice.

Signed by:
_________________
Party A

_________________
Party B
"""

    with open(text_file, 'w', encoding='utf-8') as f:
        f.write(text_content)
    print(f"Created text file: {text_file}")

    pdf_file = test_dir / 'sample.pdf'
    doc = SimpleDocTemplate(str(pdf_file), pagesize=letter)
    styles = getSampleStyleSheet()
    story = []

    title = Paragraph('LEGAL DOCUMENT SAMPLE', styles['Title'])
    story.append(title)
    story.append(Paragraph('<br/><br/>', styles['Normal']))

    content = """CONTRACT AGREEMENT

This agreement is made and entered into on this day, between Party A and Party B.

1. DEFINITIONS
   "Agreement" means this contract and all its attachments.
   "Parties" means Party A and Party B collectively.

2. SCOPE OF WORK
   Party A agrees to provide services as described in Appendix A.
   Party B agrees to compensate Party A as outlined in Section 3.

3. PAYMENT TERMS
   Payment shall be made within 30 days of invoice date.
   Late payments shall incur a 2% monthly interest.

4. TERMINATION
   Either party may terminate this agreement with 30 days written notice.

Signed by:
_________________
Party A

_________________
Party B"""

    for paragraph in content.split('\n\n'):
        p = Paragraph(paragraph, styles['Normal'])
        story.append(p)
        story.append(Paragraph('<br/>', styles['Normal']))

    doc.build(story)
    print(f"Created PDF file: {pdf_file}")


if __name__ == '__main__':
    create_test_files()
