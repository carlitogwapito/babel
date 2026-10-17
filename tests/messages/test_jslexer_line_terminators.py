import pytest

from babel.messages import jslexer


@pytest.mark.parametrize(
    "terminator",
    ["\n", "\r", "\u2028", "\u2029"],
    ids=["LF", "CR", "LS", "PS"],
)
@pytest.mark.parametrize("escaped", [False, True], ids=["raw", "escaped"])
def test_regexp_literal_rejects_line_terminators(terminator, escaped):
    prefix = "a\\" if escaped else "a"
    literal = "/" + prefix + terminator + "b/"

    assert jslexer.regex_re.fullmatch(literal) is None


def test_regexp_literal_without_line_terminator():
    assert jslexer.regex_re.fullmatch("/ab+/g") is not None
