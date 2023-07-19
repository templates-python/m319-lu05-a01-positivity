from positivity import main


def test_positive(capsys, monkeypatch):
    inputs = iter([3])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    main()
    captured = capsys.readouterr()
    assert captured.out == 'The number is positive.\n'


def test_negative(capsys, monkeypatch):
    inputs = iter([-7])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    main()
    captured = capsys.readouterr()
    assert captured.out == 'The number is not positive.\n'


def test_zero(capsys, monkeypatch):
    inputs = iter([0])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    main()
    captured = capsys.readouterr()
    assert captured.out == 'The number is not positive.\n'
