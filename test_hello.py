
from hello import main


def test_main(capsys):
    main()
    captured = capsys.readouterr()
    assert captured.out.strip() == "Hello, DevOps UAT Environment!"
