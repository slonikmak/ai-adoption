#!/usr/bin/env python3
"""Export the static HTML's main document to a plain Markdown reading copy.

Uses only the Python standard library. The HTML remains canonical. The output
preserves headings, paragraphs, cards, diagram labels, collapsible content,
and lists; graphical layout and arrows are represented as text.
"""
from html.parser import HTMLParser
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent


class MarkdownExporter(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.in_main = False
        self.depth = 0
        self.out = []
        self.pre = False
        self.skip_depth = 0
        self.bold = 0
        self.link_href = None

    def add(self, text):
        self.out.append(text)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'main':
            self.in_main = True
            self.depth = 1
            return
        if not self.in_main:
            return
        if self.skip_depth:
            if tag not in ('br', 'hr', 'img', 'input', 'meta', 'link'):
                self.skip_depth += 1
            return
        classes = set(attrs.get('class', '').split())
        if 'arrow' in classes or 'tiny-arrow' in classes:
            self.skip_depth = 1
            return
        if tag in ('h2', 'h3', 'h4'):
            self.add('\n\n' + '#' * int(tag[1]) + ' ')
        elif tag == 'a' and attrs.get('href'):
            self.link_href = attrs['href']
            self.add('[')
        elif tag == 'summary':
            self.add('\n\n#### ')
        elif tag == 'blockquote':
            self.add('\n\n> ')
        elif tag == 'li':
            self.add('\n- ')
        elif tag == 'pre':
            self.pre = True
            self.add('\n\n```text\n')
        elif tag == 'br':
            self.add(' ')
        elif tag in ('b', 'strong'):
            self.add('**')
            self.bold += 1
        elif tag in ('div', 'p', 'figure', 'section', 'figcaption', 'details', 'ul'):
            self.add('\n\n')

    def handle_endtag(self, tag):
        if not self.in_main:
            return
        if self.skip_depth:
            self.skip_depth -= 1
            return
        if tag == 'main':
            self.in_main = False
        elif tag == 'a' and self.link_href:
            self.add(f']({self.link_href})')
            self.link_href = None
        elif tag == 'pre':
            self.pre = False
            self.add('\n```\n\n')
        elif tag in ('b', 'strong') and self.bold:
            self.add('** ')
            self.bold -= 1
        elif tag in ('p', 'h2', 'h3', 'h4', 'div', 'section', 'figure', 'figcaption', 'details', 'summary', 'blockquote', 'ul'):
            self.add('\n\n')

    def handle_data(self, data):
        if self.in_main and not self.skip_depth:
            self.add(data if self.pre else re.sub(r'\s+', ' ', data))

    def result(self):
        # Normalize block whitespace outside fenced code, preserving code indentation.
        parts = ''.join(self.out).split('```')
        for i in range(0, len(parts), 2):
            s = parts[i]
            s = re.sub(r'[ \t]+\n', '\n', s)
            s = re.sub(r'\n[ \t]+', '\n', s)
            s = re.sub(r'\n{3,}', '\n\n', s)
            parts[i] = s
        return '```'.join(parts).strip()


def export(directory, intro):
    exporter = MarkdownExporter()
    exporter.feed((directory / 'index.html').read_text(encoding='utf-8'))
    (directory / 'content.md').write_text(intro + exporter.result() + '\n', encoding='utf-8')


def main():
    export(ROOT, (
        '# Engineering the AI-Ready Organization\n\n'
        '**Anton Mashkov · White paper v0.3 · 2026**\n\n'
        'AI adoption starts where a team loses time or has to redo work. '
        'The people who own that part of the process decide what AI can help with, which decisions stay in their hands, and what evidence justifies wider use.\n\n'
        '<!-- Generated from index.html. The HTML is canonical. -->\n\n'
    ))
    export(ROOT / 'ru', (
        '# Как внедрить ИИ в работу команды разработки\n\n'
        '**Антон Машков · Записка v0.3 · 2026**\n\n'
        'Где команда теряет время? Если требования приходится уточнять уже во время тестирования, стоит '
        'попробовать ассистента ещё на обсуждении макета. Участники команды решают, что ему поручить, за какие '
        'решения они отвечают сами и как проверят, помогло ли это в работе.\n\n'
        '<!-- Источник текста — ru/index.html. -->\n\n'
    ))


if __name__ == '__main__':
    main()
