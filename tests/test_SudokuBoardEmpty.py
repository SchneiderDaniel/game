import pytest
from board.SudokuBoard import SudokuBoard

emptyBoard = SudokuBoard(9)

def testSize():
    assert emptyBoard.size==9

def testCellAmount():
    assert emptyBoard.cellAmount==81

def testGridSize():
    assert emptyBoard.gridSize==3

def testGridAmount():
    assert emptyBoard.gridAmount==9

def testIsFilled():
    assert emptyBoard.isFilled()==False

def testIsEnterValid():
    assert emptyBoard.isEnterValid(0,0,1)==True

def testGet():
    assert emptyBoard.get(0,0)==-1

def testgridCoord1():
    assert emptyBoard.gridCoordToCell(0,0)==(0,0) 

def testgridCoord2():
    assert emptyBoard.gridCoordToCell(2,2)==(0,0)

def testgridCoord3():
    assert emptyBoard.gridCoordToCell(8,8)==(2,2)  

def testgridCoord4():
    assert emptyBoard.gridCoordToCell(0,8)==(0,2) 

# import pytest
# from wallet import Wallet, InsufficientAmount


# def test_default_initial_amount():
#     wallet = Wallet()
#     assert wallet.balance == 0

# def test_setting_initial_amount():
#     wallet = Wallet(100)
#     assert wallet.balance == 100

# def test_wallet_add_cash():
#     wallet = Wallet(10)
#     wallet.add_cash(90)
#     assert wallet.balance == 100

# def test_wallet_spend_cash():
#     wallet = Wallet(20)
#     wallet.spend_cash(10)
#     assert wallet.balance == 10

# def test_wallet_spend_cash_raises_exception_on_insufficient_amount():
#     wallet = Wallet()
#     with pytest.raises(InsufficientAmount):
#         wallet.spend_cash(100)