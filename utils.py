from pybtex.database import Person, Entry
from pybtex.textutils import abbreviate


def parse_entry(entry: Entry) -> str:

    key = entry.key
    title = entry.fields["title"]
    reading_date = entry.fields["urldate"]

    authors = [_format_author(author) for author in entry.persons["author"]]
    authors = ", ".join(authors)

    pdf_file = entry.fields["file"]
    pdf_file = _parse_pdf_path(pdf_file)

    md_entry_str = _format_string(key, title, reading_date, authors, pdf_file)
    return md_entry_str


def _format_author(author: Person) -> str:
    name = abbreviate(str(author))
    name = name.split(",")
    name = f"{name[-1]} {name[0]}".lstrip()
    return name


def _parse_pdf_path(pdf_file: str) -> str:
    return f"<{pdf_file.split(':')[1]}>"


def _format_string(key, title, reading_date, authors, pdf_file):
    writeup_file = f"notes/{key}.md"
    md_str = (
        f"**{reading_date}:** [{title}]({writeup_file}) {authors} [[PDF]]({pdf_file})"
    )

    return md_str
