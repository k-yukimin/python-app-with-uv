from pytest import CaptureFixture

from sample_project.main import get_message, main


def test_get_message() -> None:
    assert get_message() == "Hello from sample_project"


def test_main_prints_message(capsys: CaptureFixture[str]) -> None:
    main()
    captured = capsys.readouterr()
    assert captured.out.strip() == "Hello from sample_project"
