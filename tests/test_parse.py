import pytest
from unittest.mock import MagicMock, patch
from parse import parse_with_ollama


@patch("parse.ChatPromptTemplate.from_template")
@patch("parse.model")
def test_parse_with_ollama(mock_model, mock_prompt_template):
    # Mock the prompt and chain behavior
    mock_prompt = MagicMock()
    mock_chain = MagicMock()

    # Mock the template to return the prompt
    mock_prompt_template.return_value = mock_prompt

    # Mock the chain to return our expected output
    mock_prompt.__or__.return_value = mock_chain
    mock_chain.invoke.return_value = "Extracted Data"

    dom_chunks = ["<p>Sample content</p>"]
    parse_description = "Sample"
    result = parse_with_ollama(dom_chunks, parse_description)

    # The result should match the mocked output
    assert result == "Extracted Data" * len(dom_chunks)
