from helpers.randomInteger import randomInteger
from helpers.shouldHappenWithProbability import shouldHappenWithProbability
from direction import Direction
from piece import Piece


class Game:
    board = []

    def __init__(self) -> None:
        """Inits the game"""
        self.prepareBoard()

    """
    Random generation functions
    """

    def shouldBeFour(self) -> bool:
        """Defines the chance of getting a new 4 into the game."""
        return shouldHappenWithProbability(10)  # 10% probability

    def randomAxisPosition(self) -> int:
        """Creates a new integer between 0 and 3."""
        return randomInteger(0, 3)

    """
    Board related functions
    """

    def prepareBoard(self) -> None:
        """Prepares the board for the game => creates the full matrix"""
        for i in range(4):
            self.board.append([Piece(0), Piece(0), Piece(0), Piece(0)])

    """
    Game dynamic functions
    """

    def insertNewPiece(self) -> None:
        """Creates a new `2` (or `4`) into the board."""
        newNumber = 2
        if (self.shouldBeFour()):
            newNumber = 4

        newNumberXPos = -1
        newNumberYPos = -1

        while newNumberXPos == -1 and newNumberYPos == -1:
            newNumberXPosCandidate = self.randomAxisPosition()
            newNumberYPosCandidate = self.randomAxisPosition()

            if self.board[newNumberXPosCandidate][newNumberYPosCandidate] == 0:
                newNumberXPos = newNumberXPosCandidate
                newNumberYPos = newNumberYPosCandidate

        self.board[newNumberXPos][newNumberYPos] = Piece(newNumber)

        """
        Continuar daqui: ver dinâmica de mover peças para cima, ocupando os
        espaços com number = 0 ou number != 0 e isCombined = False.

        se number != 0 e isCombined = False, juntar peças se tiverem number iguais.
        se isCombined = True, parar 1 posição antes independente da situação.
        """

    # def _moveUpUntilPossible(self):

    # def _executePiecesMoving(self):
    #     for x in range(3):
    #         for y in range(3):

    # def movePiecesTo(self, direction: int) -> None:
    #     if direction == Direction.UP:
