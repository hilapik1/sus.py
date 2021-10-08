using System;

public class Room
{
	private int roomNum;
	private int roomType;
	private nigthReserved;
	public Room(int roomType, int roomNum)
	{
		this.roomType = roomType;
		this.roomNum = roomNum;
		this.nightReserved = 0;
	}
	public int Income()
    {
		return this.roomType * 50 * this.nightReserved;
    }
}
