#!/usr/bin/env python3
"""Render the review manuscript's Markdown to a typeset PDF.

Requires reportlab and pypdf (document tooling only, not website dependencies).
The evidence snapshot is frozen separately; rendering does not update it.
"""
import html
import re
from pathlib import Path
from reportlab.lib import colors
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / 'manuscript/co-speech-gesture-atlas.md'
OUTPUT = ROOT / 'output/pdf/co-speech-gesture-atlas.pdf'
INK = colors.HexColor('#123b38')
STYLES = {
    'body': ParagraphStyle('body',fontName='Times-Roman',fontSize=10.2,leading=13.1,alignment=TA_JUSTIFY,spaceAfter=8),
    'title': ParagraphStyle('title',fontName='Times-Bold',fontSize=24,leading=27,textColor=INK,spaceAfter=14),
    'h2': ParagraphStyle('h2',fontName='Helvetica-Bold',fontSize=13,leading=16,textColor=INK,spaceBefore=12,spaceAfter=8,keepWithNext=True),
    'h3': ParagraphStyle('h3',fontName='Helvetica-Bold',fontSize=10.4,leading=13,textColor=INK,spaceBefore=8,spaceAfter=5,keepWithNext=True),
    'cell': ParagraphStyle('cell',fontName='Times-Roman',fontSize=9,leading=11),
    'thead': ParagraphStyle('thead',fontName='Helvetica-Bold',fontSize=8.5,leading=10.5,textColor=colors.white),
    'meta': ParagraphStyle('meta',fontName='Helvetica',fontSize=9,leading=12,textColor=colors.HexColor('#62716e'),spaceAfter=13),
    'ref': ParagraphStyle('ref',fontName='Times-Roman',fontSize=8.8,leading=11,spaceAfter=5),
}

def inline(text):
    text = html.escape(text)
    text = re.sub(r'\[([^]]+)\]\(([^)]+)\)',r'<a href="\2" color="#096c64">\1</a>',text)
    text = re.sub(r'\*\*(.+?)\*\*',r'<b>\1</b>',text)
    text = re.sub(r'`([^`]+)`',r'<font name="Courier">\1</font>',text)
    return text


def footer(canvas, document):
    canvas.saveState()
    width, height = A4
    canvas.setStrokeColor(colors.HexColor('#cad6cf')); canvas.line(48, height-34, width-48,height-34)
    canvas.setFont('Helvetica',7.5); canvas.setFillColor(INK)
    canvas.drawString(48,height-25,'CO-SPEECH GESTURE ATLAS')
    canvas.drawRightString(width-48,height-25,'REVIEW DRAFT / 12 OCTOBER 2026')
    canvas.setFillColor(colors.HexColor('#62716e'))
    canvas.drawString(48,27,'Collection snapshot: 12 October 2026 | Application audit: 3 October 2026')
    canvas.drawRightString(width-48,27,str(document.page))
    canvas.restoreState()


def main():
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    story=[]; lines=SOURCE.read_text(encoding='utf-8-sig').splitlines(); i=0; references=False
    usable=A4[0]-96
    while i<len(lines):
        line=lines[i].strip()
        if not line: i+=1; continue
        if line=='<!-- pagebreak -->': story.append(PageBreak()); i+=1; continue
        if line.startswith('|'):
            rows=[]
            while i<len(lines) and lines[i].strip().startswith('|'):
                cells=[v.strip() for v in lines[i].strip().strip('|').split('|')]
                if not all(re.fullmatch(r':?-+:?',v) for v in cells): rows.append(cells)
                i+=1
            n=len(rows[0]); ratios=([.38,.14,.48] if n==3 else [.48,.16,.12,.12,.12] if n==5 and rows[0][0]=='Method group' else [.28,.18,.11,.27,.16] if n==5 else [1/n]*n)
            table=Table([[Paragraph(inline(c),STYLES['thead'] if ri==0 else STYLES['cell']) for c in row] for ri,row in enumerate(rows)],colWidths=[usable*r for r in ratios],repeatRows=1,hAlign='LEFT')
            table.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),INK),('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),7),('RIGHTPADDING',(0,0),(-1,-1),7),('TOPPADDING',(0,0),(-1,-1),6),('BOTTOMPADDING',(0,0),(-1,-1),6),('ROWBACKGROUNDS',(0,1),(-1,-1),[colors.HexColor('#f1f5f1'),colors.white]),('LINEBELOW',(0,-1),(-1,-1),.5,colors.HexColor('#cad6cf'))]))
            story.extend([table,Spacer(1,10)]); continue
        if line.startswith('#'):
            level=len(line)-len(line.lstrip('#')); heading=line[level:].strip()
            references=heading=='References' or references
            story.append(Paragraph(inline(heading),STYLES['title' if level==1 else 'h2' if level==2 else 'h3'])); i+=1; continue
        paragraph=[line]; i+=1
        while i<len(lines) and lines[i].strip() and not lines[i].startswith(('#','|','<!--')):
            paragraph.append(lines[i].strip()); i+=1
        text=' '.join(paragraph)
        style=STYLES['meta'] if text.startswith('Review draft') else STYLES['ref'] if references else STYLES['body']
        story.append(Paragraph(inline(text),style))
    doc=SimpleDocTemplate(str(OUTPUT),pagesize=A4,leftMargin=48,rightMargin=48,topMargin=48,bottomMargin=45,title='Co-Speech Gesture Atlas: An Open, Living Map of Gesture Generation Research and Its Use',author='Co-Speech Gesture Atlas project')
    doc.build(story,onFirstPage=footer,onLaterPages=footer)
    reader=PdfReader(OUTPUT)
    print(f'{OUTPUT}: {len(reader.pages)} pages; {sum(len(p.extract_text()) for p in reader.pages)} text characters')

if __name__=='__main__': main()
