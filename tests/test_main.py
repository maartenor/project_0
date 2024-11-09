import main

def test_main(capsys):
    
    # Run the main function
    main.main()

    # Capture the printed output
    captured = capsys.readouterr()

    # Check that the correct output is printed
    assert "Starting... using 3" in captured.out
    assert "Calculated square root : 1.732" in captured.out
    assert "Calculated square : 9" in captured.out
    assert "Incrementing 3 ... :  4" in captured.out
    assert "Decrementing 3 ... :  2" in captured.out
    assert "Ran..." in captured.out
    # assert "Dit moet verkeerd gaan, want ontbreekt" in captured.out

