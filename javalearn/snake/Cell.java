package javalearn.snake;

public class Cell {
    private final int row, col;
    private CellType celltype;

    public Cell(int row, int col){
        this.row = row;
        this.col = col;
    }

    public CellType getCellType(){
        return celltype;
    }

    public void setCellType(CellType celltype){
        this.celltype = celltype;
    }

    public int getrow(){
        return row;
    }

    public int getcol(){
        return col;
    }
}

//www.geeksforgeeks.org/design-snake-game/