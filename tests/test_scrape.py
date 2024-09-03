import pytest
from scrape import extract_body_content, clean_body_content, split_dom_content

# Example HTML content for testing
html_content = """
<html>
<body>
    <h1>Title</h1>
    <p>This is a paragraph.</p>
    <script>console.log('This is a script');</script>
</body>
</html>
"""


def test_extract_body_content():
    body_content = extract_body_content(html_content)
    assert "<body>" in body_content
    assert "<script>" in body_content


def test_clean_body_content():
    body_content = extract_body_content(html_content)
    cleaned_content = clean_body_content(body_content)
    assert "This is a paragraph" in cleaned_content
    assert "console.log" not in cleaned_content


def test_split_dom_content():
    long_content = "A" * 12000
    chunks = split_dom_content(long_content, max_length=6000)
    assert len(chunks) == 2
    assert len(chunks[0]) == 6000
