from pytest import CaptureFixture

from project2.main import get_message, main


def test_get_message() -> None:
    assert get_message() == "Hello from project2"


def test_main_prints_message(capsys: CaptureFixture[str]) -> None:
    main()
    captured = capsys.readouterr()
    assert captured.out.strip() == "Hello from project2"
